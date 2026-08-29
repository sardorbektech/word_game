"""Deterministic Adaptive Difficulty Engine."""
import math
from typing import Dict, Any, Tuple


class DifficultyEngine:
    """Calculates deterministic difficulty updates based on player performance."""

    # Baseline difficulty scores per CEFR level
    LEVEL_BASELINES = {
        "A1": 0.20,
        "A2": 0.35,
        "B1": 0.50,
        "B2": 0.65,
        "C1": 0.80
    }

    # Level boundaries
    LEVEL_BOUNDS = {
        "A1": (0.05, 0.40),
        "A2": (0.25, 0.55),
        "B1": (0.40, 0.70),
        "B2": (0.55, 0.85),
        "C1": (0.70, 0.99)
    }

    @classmethod
    def calculate_round_performance(
        cls,
        word_count: int,
        letter_count: int,
        mistake_count: int,
        active_time_seconds: float
    ) -> Tuple[float, float]:
        """Calculates accuracy (0-100%) and speed factor.
        
        Returns:
            accuracy: 0.0 to 100.0
            expected_time: target seconds for this sentence
        """
        # Baseline expected time: ~1.5s per word + 0.4s per letter
        expected_time = max(4.0, (word_count * 1.5) + (letter_count * 0.4))

        # Accuracy formula: 100 - (mistakes * penalty)
        penalty_per_mistake = 18.0 if word_count <= 4 else 14.0
        accuracy = max(10.0, 100.0 - (mistake_count * penalty_per_mistake))

        return round(accuracy, 1), round(expected_time, 1)

    @classmethod
    def update_difficulty(
        cls,
        current_difficulty: float,
        level: str,
        accuracy: float,
        mistakes: int,
        active_time: float,
        expected_time: float
    ) -> Tuple[float, float, str]:
        """Calculates the new difficulty score and delta.
        
        Returns:
            new_difficulty: float (0.05 to 0.99)
            difficulty_delta: float (-0.10 to +0.10)
            feedback_message: explanation of the change
        """
        min_bound, max_bound = cls.LEVEL_BOUNDS.get(level, (0.05, 0.99))
        time_ratio = active_time / max(expected_time, 1.0)

        delta = 0.0

        if mistakes == 0:
            if time_ratio <= 0.8:
                # Fast & flawless
                delta = +0.05
                feedback = "Ajoyib tezlik va aniqlik! Qiyinlik darajasi oshirildi."
            elif time_ratio <= 1.2:
                # Good & clean
                delta = +0.03
                feedback = "Toza natija! Qiyinlik biroz oshirildi."
            else:
                # Clean but careful
                delta = +0.01
                feedback = "Yaxshi natija! Qiyinlik deyarli o'zgarishsiz qoldi."
        elif mistakes == 1:
            if time_ratio <= 1.0:
                delta = +0.01
                feedback = "Yaxshi! Qiyinlik joriy darajada ushlab turildi."
            else:
                delta = -0.01
                feedback = "Kichik xatolik. Qiyinlik moslashtirildi."
        elif mistakes == 2:
            delta = -0.03
            feedback = "Bir nechta xatolik. Qiyinlik biroz kamaytirildi."
        else:
            # 3 or more mistakes
            delta = -0.06
            feedback = "Murakkablik sezildi. Keyingi gaplar osonlashtiriladi."

        new_difficulty = current_difficulty + delta
        # Clamp within level bounds
        new_difficulty = max(min_bound, min(max_bound, new_difficulty))
        actual_delta = round(new_difficulty - current_difficulty, 3)

        return round(new_difficulty, 3), actual_delta, feedback
