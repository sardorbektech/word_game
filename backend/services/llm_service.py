"""LLM Content Generation Service using OpenAI GPT-5.6 Luna with 1000 Sentences Offline Fallback."""
import json
import re
import random
from typing import Dict, Any, List, Optional
from openai import OpenAI
from backend.config import settings
from backend.data.dataset import DATASET


# Diverse creative situational contexts to prevent LLM from repeating default textbook sentences
DIVERSE_SCENARIOS = [
    "at a vibrant morning cafe or bakery drinking tea",
    "talking about daily morning routines and healthy breakfast",
    "family gathering and cooking a traditional evening dinner",
    "planning a weekend nature trip or walk near the mountains",
    "meeting a friendly new friend or neighbor in the green park",
    "buying ripe fresh fruits and vegetables at a local bazaar",
    "enjoying cozy rainy weather at home with a hot drink",
    "discussing an exciting creative hobby, sport, or game",
    "riding a bicycle through the clean and sunny city streets",
    "reading an inspiring adventure book in a quiet library",
    "caring for a playful pet or watching birds in the garden",
    "arriving at a modern railway station or bright airport",
    "learning something fascinating and useful in a classroom",
    "listening to beautiful relaxing melodies in the evening",
    "making a handmade art piece or repairing household items",
    "celebrating a cheerful birthday gathering with close friends",
    "ordering delicious meal and desserts at a cozy restaurant",
    "visiting a historic architectural museum or modern exhibition",
    "cleaning and decorating a bright and welcoming room",
    "watching an interesting nature documentary about oceans",
    "watering colorful garden flowers and tall green trees",
    "taking a refreshing brisk walk in the cool morning air",
    "discussing memorable journeys and visiting famous cities",
    "shopping for comfortable seasonal clothes and warm shoes"
]


RECENT_SERVED_SENTENCES: List[str] = []


class LLMService:
    """Generates adaptive game content via OpenAI API or curated dataset with 100% diversity."""

    @classmethod
    def generate_sentence(
        cls,
        level: str = "A1",
        difficulty: float = 0.35,
        topic: str = "General",
        weak_words: Optional[List[str]] = None,
        recent_sentences: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Requests fresh unique content from OpenAI or returns non-repeated sentence from curated dataset."""
        combined_recent = list(set((recent_sentences or []) + RECENT_SERVED_SENTENCES[-25:]))

        if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY.strip():
            try:
                res = cls._call_openai(
                    level=level,
                    difficulty=difficulty,
                    topic=topic,
                    weak_words=weak_words or [],
                    recent_sentences=combined_recent
                )
                # If OpenAI happens to return a recent sentence, retry once
                recent_lower = set(s.strip().lower() for s in combined_recent)
                if res.get("target_text", "").strip().lower() in recent_lower:
                    res = cls._call_openai(
                        level=level,
                        difficulty=difficulty,
                        topic=topic,
                        weak_words=weak_words or [],
                        recent_sentences=combined_recent
                    )

                res["content_source"] = "ai"
                cls._record_served_sentence(res.get("target_text", ""))
                return res
            except Exception as e:
                print(f"[LLMService] OpenAI call error: {e}. Using offline dataset.")

        res = cls._get_fallback_sentence(level, topic, weak_words or [], combined_recent)
        res["content_source"] = "dataset"
        cls._record_served_sentence(res.get("target_text", ""))
        return res

    @classmethod
    def _record_served_sentence(cls, text: str):
        if text and text.strip():
            RECENT_SERVED_SENTENCES.append(text.strip())
            if len(RECENT_SERVED_SENTENCES) > 50:
                RECENT_SERVED_SENTENCES.pop(0)

    @classmethod
    def _call_openai(
        cls,
        level: str,
        difficulty: float,
        topic: str,
        weak_words: List[str],
        recent_sentences: List[str]
    ) -> Dict[str, Any]:
        """Calls OpenAI API with strict JSON schema and dynamic context to prevent repetitive sentences."""
        client_kwargs = {
            "api_key": settings.OPENAI_API_KEY,
            "timeout": 4.5
        }
        if settings.OPENAI_BASE_URL and settings.OPENAI_BASE_URL.strip():
            client_kwargs["base_url"] = settings.OPENAI_BASE_URL.strip()

        client = OpenAI(**client_kwargs)

        weak_words_str = ", ".join(weak_words) if weak_words else "none"
        scenario = random.choice(DIVERSE_SCENARIOS)
        random_seed = random.randint(10000, 999999)

        level_guidance = {
            "A1": "Beginner level: Simple basic grammar (e.g. Present Simple), daily life words, 4-6 words.",
            "A2": "Elementary level: Past simple, basic conjunctions, 5-7 words.",
            "B1": "Intermediate level: Future forms, modal verbs, present perfect, 6-8 words.",
            "B2": "Upper-intermediate: Conditionals, passive voice, phrasal verbs, 7-9 words.",
            "C1": "Advanced level: Sophisticated vocabulary, subjunctive/inversion, nuanced idioms, 7-10 words."
        }.get(level.upper(), "Adaptive CEFR English sentence, 5-9 words.")

        avoid_clause = ""
        if recent_sentences:
            avoid_list_str = "; ".join([f'"{s}"' for s in recent_sentences[-6:]])
            avoid_clause = f"\n- CRITICAL DIVERSITY: DO NOT repeat or resemble any of these recently played sentences: [{avoid_list_str}]."

        system_prompt = (
            "You are an expert English language educational engine. "
            "Your output must be a single valid JSON object with the exact keys: "
            "'topic', 'source_text' (in natural Uzbek), 'target_text' (in grammatically correct English), and 'words' (array of English word tokens in exact sequence). "
            "Do NOT include any commentary, explanations, or text outside the JSON object."
        )

        user_prompt = f"""Generate a unique and engaging English-Uzbek learning pair for an adaptive puzzle game.
- CEFR Level: {level.upper()} ({level_guidance})
- Difficulty Metric: {difficulty:.2f}
- Topic: {topic}
- Situational Scene / Creative Prompt: {scenario}
- Random Session Seed: #{random_seed}
- Priority words to include if suitable: [{weak_words_str}]{avoid_clause}

CRITICAL RULES:
1. Every generated sentence must be unique, natural, and distinct.
2. The Uzbek sentence must be a natural, idiomatically accurate translation.
3. Words in the 'words' array must match the English sentence in exact order without punctuation.

Output format strictly adhering to JSON:
{{
  "topic": "{topic}",
  "source_text": "Tabiiy o'zbekcha gap shu yerga yoziladi.",
  "target_text": "Natural and precise English translation here.",
  "words": ["Natural", "and", "precise", "English", "translation", "here"]
}}"""

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            max_completion_tokens=800
        )

        raw_content = response.choices[0].message.content or ""
        raw_content = raw_content.strip()

        # Robust JSON extraction
        json_match = re.search(r"\{.*\}", raw_content, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group(0))
        else:
            data = json.loads(raw_content)

        source_text = data.get("source_text", "").strip()
        target_text = data.get("target_text", "").strip()

        # Extract and sanitize words
        raw_words = data.get("words", [])
        if not raw_words and target_text:
            raw_words = target_text.split()

        clean_words = [re.sub(r"[^a-zA-Z0-9'-]", "", w) for w in raw_words if re.sub(r"[^a-zA-Z0-9'-]", "", w)]

        if not source_text or not target_text or len(clean_words) < 2:
            raise ValueError(f"Invalid generated sentence structure: {data}")

        return {
            "topic": data.get("topic", topic),
            "source_text": source_text,
            "target_text": target_text,
            "words": clean_words
        }

    @classmethod
    def _get_fallback_sentence(
        cls,
        level: str,
        topic: str,
        weak_words: List[str],
        recent_sentences: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Provides a truly random sentence from the curated dataset for the given CEFR level avoiding repeats."""
        lvl_key = (level or "A1").strip().upper()
        if lvl_key not in DATASET or not DATASET[lvl_key]:
            lvl_key = "A1"

        level_items = list(DATASET[lvl_key])
        recent_set = set(s.strip().lower() for s in (recent_sentences or []))

        # Filter out recently used sentences if possible
        unseen_items = [item for item in level_items if item["target_text"].strip().lower() not in recent_set]
        pool = unseen_items if unseen_items else level_items

        # If user picked a specific topic (and it's not General), prioritize sentences matching topic
        if topic and topic.lower() != "general":
            topic_matches = [item for item in pool if item.get("topic", "").lower() == topic.lower()]
            if topic_matches:
                chosen = random.choice(topic_matches)
                return {
                    "topic": chosen.get("topic", topic),
                    "source_text": chosen["source_text"],
                    "target_text": chosen["target_text"],
                    "words": list(chosen["words"])
                }

        # Otherwise random selection from the candidate pool
        chosen = random.choice(pool)
        return {
            "topic": chosen.get("topic", topic),
            "source_text": chosen["source_text"],
            "target_text": chosen["target_text"],
            "words": list(chosen["words"])
        }
