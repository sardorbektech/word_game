"""LLM Content Generation Service using OpenAI GPT-5.6 Luna with 1000 Sentences Offline Fallback."""
import json
import re
import random
from typing import Dict, Any, List, Optional
from openai import OpenAI
from backend.config import settings
from backend.data.dataset import DATASET


class LLMService:
    """Generates adaptive game content via OpenAI API or 1000-sentence offline curated dataset."""

    @classmethod
    def generate_sentence(
        cls,
        level: str = "A1",
        difficulty: float = 0.35,
        topic: str = "General",
        weak_words: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Requests new content from GPT-5.6 Luna or returns random sentence from curated dataset."""
        if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY.strip():
            try:
                res = cls._call_openai(level, difficulty, topic, weak_words or [])
                res["content_source"] = "ai"
                return res
            except Exception as e:
                print(f"[LLMService] OpenAI call error: {e}. Using offline dataset.")

        res = cls._get_fallback_sentence(level, topic, weak_words or [])
        res["content_source"] = "dataset"
        return res

    @classmethod
    def _call_openai(
        cls,
        level: str,
        difficulty: float,
        topic: str,
        weak_words: List[str]
    ) -> Dict[str, Any]:
        """Calls OpenAI GPT-5.6 Luna API with structured prompt."""
        client = OpenAI(api_key=settings.OPENAI_API_KEY, timeout=3.0)

        weak_words_str = ", ".join(weak_words) if weak_words else "none"

        system_prompt = (
            "You are an expert adaptive English language curriculum engine. "
            "Your task is to generate ONE engaging, natural Uzbek sentence and its precise grammatically correct English translation. "
            "You must return ONLY a valid JSON object without markdown fences, matching the requested schema."
        )

        user_prompt = f"""
Generate an English sentence for an adaptive sentence reconstruction game.
- Target CEFR Level: {level}
- Target Difficulty Score: {difficulty:.2f} (0.00 is simplest A1, 1.00 is advanced C1)
- Topic preference: {topic}
- Priority vocabulary to include naturally if possible: [{weak_words_str}]

CRITICAL REQUIREMENTS:
1. The English sentence must match {level} level grammatical structures.
2. The Uzbek sentence must be a natural, idiomatic translation of the English sentence.
3. Sentence length should be between 4 and 10 words.
4. Words must only contain alphabetic characters (remove trailing punctuation in word tokens).

Return ONLY JSON:
{{
  "topic": "{topic}",
  "source_text": "Uzbek sentence here",
  "target_text": "English sentence here.",
  "words": ["Word1", "Word2", "Word3", "Word4"]
}}
"""

        response = client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_completion_tokens=400
        )

        raw_content = response.choices[0].message.content.strip()
        cleaned_json = re.sub(r"^```json\s*", "", raw_content)
        cleaned_json = re.sub(r"^```\s*", "", cleaned_json)
        cleaned_json = re.sub(r"\s*```$", "", cleaned_json).strip()

        data = json.loads(cleaned_json)

        raw_words = data.get("words", [])
        clean_words = [re.sub(r"[^a-zA-Z0-9'-]", "", w) for w in raw_words if re.sub(r"[^a-zA-Z0-9'-]", "", w)]

        return {
            "topic": data.get("topic", topic),
            "source_text": data.get("source_text"),
            "target_text": data.get("target_text"),
            "words": clean_words
        }

    @classmethod
    def _get_fallback_sentence(
        cls,
        level: str,
        topic: str,
        weak_words: List[str]
    ) -> Dict[str, Any]:
        """Provides a truly random sentence from the curated dataset for the given CEFR level."""
        lvl_key = (level or "A1").strip().upper()
        if lvl_key not in DATASET or not DATASET[lvl_key]:
            lvl_key = "A1"

        level_items = DATASET[lvl_key]

        # If user picked a specific topic (and it's not General), prioritize sentences matching topic
        if topic and topic.lower() != "general":
            topic_matches = [item for item in level_items if item.get("topic", "").lower() == topic.lower()]
            if topic_matches:
                chosen = random.choice(topic_matches)
                return {
                    "topic": chosen.get("topic", topic),
                    "source_text": chosen["source_text"],
                    "target_text": chosen["target_text"],
                    "words": list(chosen["words"])
                }

        # Otherwise random selection from the sentences in this level
        chosen = random.choice(level_items)
        return {
            "topic": chosen.get("topic", topic),
            "source_text": chosen["source_text"],
            "target_text": chosen["target_text"],
            "words": list(chosen["words"])
        }
