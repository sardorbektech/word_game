"""Grid Embedding Engine for Word Hunt / Boggle Letter Matrix.

Guarantees that every target word in the sentence is embeddable as an
adjacent connected path (8-directional) on an NxN grid, and fills the
remaining cells with smart distractor characters.
"""
import random
import math
from typing import List, Tuple, Optional, Set, Dict

# English letter frequency distribution for natural distractor generation
LETTER_WEIGHTS = {
    'E': 12.0, 'T': 9.1, 'A': 8.1, 'O': 7.7, 'I': 7.3, 'N': 7.0, 'S': 6.3,
    'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4,
    'W': 2.4, 'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0,
    'K': 0.8, 'J': 0.15, 'X': 0.15, 'Q': 0.1, 'Z': 0.07
}

# 4 orthogonal adjacent directions (Up, Down, Left, Right) - strictly NO diagonals
DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


class GridEmbeddingEngine:
    """Generates an NxN matrix with guaranteed connected paths for all target words."""

    LEVEL_BASE_DIMENSIONS = {
        "A1": 6,   # 6x6 (36 cells)
        "A2": 7,   # 7x7 (49 cells)
        "B1": 8,   # 8x8 (64 cells)
        "B2": 8,   # 8x8 (64 cells)
        "C1": 9    # 9x9 (81 cells, max 10x10)
    }

    @classmethod
    def calculate_optimal_dimension(cls, total_letters_needed: int, level: str = "A1") -> int:
        """Determines the grid dimension automatically scaled per CEFR level and sentence length."""
        base_dim = cls.LEVEL_BASE_DIMENSIONS.get(level.upper(), 6)
        
        # Calculate needed cells with margin for distractors
        needed_cells = int(total_letters_needed * 1.25)
        capacity_dim = math.ceil(math.sqrt(needed_cells))
        
        dimension = max(base_dim, capacity_dim)
        return min(dimension, 10)  # Max 10x10 (100 cells) to guarantee optimal layout on mobile & desktop

    @classmethod
    def generate_matrix(
        cls,
        words: List[str],
        level: str = "A1",
        requested_size: str = "auto",
        max_attempts: int = 100
    ) -> Tuple[List[List[str]], int, Dict[str, List[Tuple[int, int]]]]:
        """Embeds all target words into a 2D grid with guaranteed adjacent paths.
        
        Returns:
            grid: 2D list of characters (uppercase)
            dimension: grid size N
            word_paths: dictionary mapping word -> list of (row, col) coordinates
        """
        # Clean words and count letters (remove punctuation/hyphens for letter grid)
        cleaned_words = ["".join(ch for ch in w if ch.isalnum()).upper() for w in words]
        cleaned_words = [w for w in cleaned_words if w]
        total_letters = sum(len(w) for w in cleaned_words)
        dimension = cls.calculate_optimal_dimension(total_letters, level=level)

        for attempt in range(max_attempts):
            # Create empty grid
            grid = [[None for _ in range(dimension)] for _ in range(dimension)]
            occupied_cells: Set[Tuple[int, int]] = set()
            word_paths: Dict[str, List[Tuple[int, int]]] = {}
            success = True

            # Sort words longer first to place tricky ones first
            indexed_words = list(enumerate(cleaned_words))
            indexed_words.sort(key=lambda item: len(item[1]), reverse=True)

            for original_idx, word in indexed_words:
                path = cls._embed_word(word, grid, dimension, occupied_cells)
                if not path:
                    success = False
                    break
                word_paths[f"{original_idx}_{word}"] = path

            if success:
                # Fill remaining empty cells with distractors
                cls._fill_distractors(grid, dimension, cleaned_words)
                return grid, dimension, word_paths

            # If failed, on subsequent attempts try a slightly larger grid if needed
            if attempt > max_attempts // 2 and dimension < 12:
                dimension += 1

        # Fallback safe placement (snake/linear packing if dense)
        grid, dimension, word_paths = cls._fallback_guaranteed_matrix(cleaned_words, dimension)
        cls._fill_distractors(grid, dimension, cleaned_words)
        return grid, dimension, word_paths

    @classmethod
    def _embed_word(
        cls,
        word: str,
        grid: List[List[Optional[str]]],
        dimension: int,
        occupied_cells: Set[Tuple[int, int]]
    ) -> Optional[List[Tuple[int, int]]]:
        """Tries to place a single word in available connected cells using backtracking."""
        all_positions = [(r, c) for r in range(dimension) for c in range(dimension)]
        random.shuffle(all_positions)

        for start_r, start_c in all_positions:
            # Check if starting cell is free or matches first letter
            if grid[start_r][start_c] is not None and grid[start_r][start_c] != word[0]:
                continue

            path = [(start_r, start_c)]
            used_in_word = {(start_r, start_c)}

            if cls._dfs_place(word, 1, start_r, start_c, path, used_in_word, grid, dimension):
                # Apply word to grid
                for idx, (r, c) in enumerate(path):
                    grid[r][c] = word[idx]
                    occupied_cells.add((r, c))
                return path

        return None

    @classmethod
    def _dfs_place(
        cls,
        word: str,
        letter_idx: int,
        curr_r: int,
        curr_c: int,
        path: List[Tuple[int, int]],
        used_in_word: Set[Tuple[int, int]],
        grid: List[List[Optional[str]]],
        dimension: int
    ) -> bool:
        """DFS recursive step to place the next letter of the word."""
        if letter_idx >= len(word):
            return True

        target_char = word[letter_idx]
        shuffled_dirs = list(DIRECTIONS)
        random.shuffle(shuffled_dirs)

        for dr, dc in shuffled_dirs:
            nr, nc = curr_r + dr, curr_c + dc

            if 0 <= nr < dimension and 0 <= nc < dimension:
                if (nr, nc) not in used_in_word:
                    # Cell can be empty or already have the same character
                    cell_val = grid[nr][nc]
                    if cell_val is None or cell_val == target_char:
                        used_in_word.add((nr, nc))
                        path.append((nr, nc))

                        if cls._dfs_place(word, letter_idx + 1, nr, nc, path, used_in_word, grid, dimension):
                            return True

                        path.pop()
                        used_in_word.remove((nr, nc))

        return False

    @classmethod
    def _fill_distractors(cls, grid: List[List[Optional[str]]], dimension: int, target_words: List[str]):
        """Fills empty cells with realistic English letters or common word fragments."""
        # Extract letters from target words to make distractors naturally deceptive
        seed_letters = list("".join(target_words)) if target_words else []
        all_alphabet = list(LETTER_WEIGHTS.keys())
        weights = list(LETTER_WEIGHTS.values())

        for r in range(dimension):
            for c in range(dimension):
                if grid[r][c] is None:
                    if seed_letters and random.random() < 0.40:
                        grid[r][c] = random.choice(seed_letters)
                    else:
                        grid[r][c] = random.choices(all_alphabet, weights=weights, k=1)[0]

    @classmethod
    def _fallback_guaranteed_matrix(
        cls,
        words: List[str],
        dimension: int
    ) -> Tuple[List[List[str]], int, Dict[str, List[Tuple[int, int]]]]:
        """Guaranteed fallback that lays words out in continuous serpentine rows/cols."""
        total_needed = sum(len(w) for w in words)
        dimension = max(dimension, math.ceil(math.sqrt(total_needed)))
        grid = [[None for _ in range(dimension)] for _ in range(dimension)]
        word_paths = {}

        current_r, current_c = 0, 0
        direction_right = True

        for idx, word in enumerate(words):
            path = []
            for ch in word:
                grid[current_r][current_c] = ch
                path.append((current_r, current_c))

                # Step to adjacent cell
                if direction_right:
                    if current_c + 1 < dimension:
                        current_c += 1
                    else:
                        current_r += 1
                        direction_right = False
                else:
                    if current_c - 1 >= 0:
                        current_c -= 1
                    else:
                        current_r += 1
                        direction_right = True

                if current_r >= dimension:
                    break

            word_paths[f"{idx}_{word}"] = path

        return grid, dimension, word_paths

    @classmethod
    def verify_word_in_grid(cls, word: str, grid: List[List[str]]) -> bool:
        """Verifies whether a given word can be formed by an adjacent path on the grid."""
        word = word.strip().upper()
        if not word:
            return True

        dim = len(grid)
        for r in range(dim):
            for c in range(dim):
                if grid[r][c] == word[0]:
                    visited = {(r, c)}
                    if cls._dfs_verify(word, 1, r, c, visited, grid, dim):
                        return True
        return False

    @classmethod
    def _dfs_verify(
        cls,
        word: str,
        idx: int,
        r: int,
        c: int,
        visited: Set[Tuple[int, int]],
        grid: List[List[str]],
        dim: int
    ) -> bool:
        if idx >= len(word):
            return True

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < dim and 0 <= nc < dim:
                if (nr, nc) not in visited and grid[nr][nc] == word[idx]:
                    visited.add((nr, nc))
                    if cls._dfs_verify(word, idx + 1, nr, nc, visited, grid, dim):
                        return True
                    visited.remove((nr, nc))

        return False
