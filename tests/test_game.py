"""Unit and Integration Tests for Adaptive English Sentence Reconstruction Game."""
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.services.grid_engine import GridEmbeddingEngine
from backend.services.difficulty_engine import DifficultyEngine
from backend.services.srs_service import SpacedRepetitionService
from backend.database import SessionLocal, Base, engine
from backend.models import User

client = TestClient(app)


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_grid_embedding_solvability():
    """Verifies that all target words have guaranteed connected paths in the generated grid."""
    words = ["I", "DRINK", "COFFEE", "EVERY", "MORNING"]
    
    # Test Auto size
    grid, dim, paths = GridEmbeddingEngine.generate_matrix(words, requested_size="auto")
    assert len(grid) == dim
    assert len(grid[0]) == dim
    for word in words:
        assert GridEmbeddingEngine.verify_word_in_grid(word, grid) is True, f"Word {word} not found in grid!"

    # Test fixed sizes: 6x6, 7x7, 8x8
    for size_str in ["6x6", "7x7", "8x8"]:
        grid, dim, paths = GridEmbeddingEngine.generate_matrix(words, requested_size=size_str)
        assert len(grid) == dim
        for word in words:
            assert GridEmbeddingEngine.verify_word_in_grid(word, grid) is True, f"Word {word} not found in {size_str} grid!"


def test_difficulty_engine_calculations():
    """Verifies deterministic adaptive difficulty scoring."""
    # Flawless fast response
    new_diff, delta, msg = DifficultyEngine.update_difficulty(
        current_difficulty=0.35,
        level="A2",
        accuracy=100.0,
        mistakes=0,
        active_time=5.0,
        expected_time=10.0
    )
    assert delta > 0
    assert new_diff > 0.35

    # Multiple mistakes response
    new_diff_bad, delta_bad, msg_bad = DifficultyEngine.update_difficulty(
        current_difficulty=0.35,
        level="A2",
        accuracy=40.0,
        mistakes=4,
        active_time=25.0,
        expected_time=10.0
    )
    assert delta_bad < 0
    assert new_diff_bad < 0.35


def test_auth_and_game_lifecycle_api():
    """End-to-end integration test of registration, game generation, and round submission."""
    # 1. Register
    username = f"testuser_{int(pytest.__file__.__hash__()) % 100000}"
    reg_res = client.post("/api/auth/register", json={
        "username": username,
        "password": "testpassword123"
    })
    assert reg_res.status_code == 200
    token_data = reg_res.json()
    token = token_data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Get profile
    profile_res = client.get("/api/auth/me", headers=headers)
    assert profile_res.status_code == 200
    assert profile_res.json()["username"] == username

    # 3. Generate Game
    gen_res = client.post("/api/game/generate", json={"level": "A1", "matrix_size": "5x5"}, headers=headers)
    assert gen_res.status_code == 200
    game_data = gen_res.json()
    assert "round_id" in game_data
    assert "grid" in game_data
    assert len(game_data["words"]) > 0

    round_id = game_data["round_id"]

    # 4. Submit Round
    sub_res = client.post("/api/game/submit-round", json={
        "round_id": round_id,
        "active_time": 6.5,
        "mistake_count": 0,
        "is_correct": True,
        "learned_words": []
    }, headers=headers)
    assert sub_res.status_code == 200
    sub_data = sub_res.json()
    assert sub_data["is_success"] is True
    assert sub_data["accuracy"] == 100.0
    assert sub_data["difficulty_delta"] > 0

    # 5. Progress summary
    prog_res = client.get("/api/progress/summary", headers=headers)
    assert prog_res.status_code == 200
    prog_data = prog_res.json()
    assert prog_data["total_games_played"] == 1


def test_frontend_static_serving():
    """Verifies that the frontend static UI (index.html) is served at root."""
    res = client.get("/")
    assert res.status_code == 200
    assert "Adaptive English Matrix" in res.text
    assert "matrix-wrapper" in res.text


def test_500_dataset_integrity():
    """Verifies that each of the 5 CEFR levels has exactly 100 high quality sentences (500 total)."""
    from backend.data.dataset import DATASET, get_word_translation

    assert "A1" in DATASET and len(DATASET["A1"]) == 100
    assert "A2" in DATASET and len(DATASET["A2"]) == 100
    assert "B1" in DATASET and len(DATASET["B1"]) == 100
    assert "B2" in DATASET and len(DATASET["B2"]) == 100
    assert "C1" in DATASET and len(DATASET["C1"]) == 100

    total_count = sum(len(DATASET[lvl]) for lvl in ["A1", "A2", "B1", "B2", "C1"])
    assert total_count == 500

    # Verify A1 sample structure
    sample_a1 = DATASET["A1"][0]
    assert "source_text" in sample_a1 and len(sample_a1["source_text"]) > 0
    assert "target_text" in sample_a1 and len(sample_a1["target_text"]) > 0
    assert "words" in sample_a1 and len(sample_a1["words"]) > 0

    # Verify automatic grid dimension scaling per level
    assert GridEmbeddingEngine.calculate_optimal_dimension(15, level="A1") == 6
    assert GridEmbeddingEngine.calculate_optimal_dimension(25, level="A2") == 7
    assert GridEmbeddingEngine.calculate_optimal_dimension(35, level="B1") == 8
    assert GridEmbeddingEngine.calculate_optimal_dimension(50, level="B2") in [8, 9]
    assert GridEmbeddingEngine.calculate_optimal_dimension(80, level="C1") in [9, 10]

    # Verify translation helper
    tr = get_word_translation("coffee")
    assert tr == "qahva"


def test_content_source_and_weak_word_translations():
    """Verifies content_source indicator and Uzbek translation in weak words."""
    username = f"truser_{int(pytest.__file__.__hash__()) % 100000}"
    reg_res = client.post("/api/auth/register", json={
        "username": username,
        "password": "testpassword123"
    })
    token = reg_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Generate Game and check content_source
    gen_res = client.post("/api/game/generate", json={"level": "A2"}, headers=headers)
    assert gen_res.status_code == 200
    data = gen_res.json()
    assert "content_source" in data
    assert data["content_source"] in ["ai", "dataset"]

    # 2. Mark weak word
    mark_res = client.post("/api/progress/words/coffee/mark", headers=headers)
    assert mark_res.status_code == 200
    assert mark_res.json()["translation"] == "qahva"

    # 3. Query weak words list
    list_res = client.get("/api/progress/weak-words", headers=headers)
    assert list_res.status_code == 200
    words = list_res.json()
    assert any(w["word"] == "coffee" and w["translation"] == "qahva" for w in words)



