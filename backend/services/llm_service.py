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
        """Calls OpenAI API with strict JSON schema and robust parsing for all CEFR levels (A1 to C1)."""
        client = OpenAI(api_key=settings.OPENAI_API_KEY, timeout=4.0)

        weak_words_str = ", ".join(weak_words) if weak_words else "none"

        level_guidance = {
            "A1": "Beginner level: Simple basic grammar (e.g. Present Simple), daily life words, 4-6 words.",
            "A2": "Elementary level: Past simple, basic conjunctions, 5-7 words.",
            "B1": "Intermediate level: Future forms, modal verbs, present perfect, 6-8 words.",
            "B2": "Upper-intermediate: Conditionals, passive voice, phrasal verbs, 7-9 words.",
            "C1": "Advanced level: Sophisticated vocabulary, subjunctive/inversion, nuanced idioms, 7-10 words."
        }.get(level.upper(), "Adaptive CEFR English sentence, 5-9 words.")

        system_prompt = (
            "You are an expert English language educational engine. "
            "Your output must be a single valid JSON object with the exact keys: "
            "'topic', 'source_text' (in natural Uzbek), 'target_text' (in grammatically correct English), and 'words' (array of English word tokens in exact sequence). "
            "Do NOT include any commentary, explanations, or text outside the JSON object."
        )

        user_prompt = f"""Generate an English-Uzbek learning pair for an adaptive puzzle game.
- CEFR Level: {level.upper()} ({level_guidance})
- Difficulty Metric: {difficulty:.2f}
- Topic: {topic}
- Priority words to include if suitable: [{weak_words_str}]

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
