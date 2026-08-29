"""LLM Content Generation Service using OpenAI GPT-5.6 Luna with 1000 Sentences Offline Fallback."""
import json
import re
import random
from typing import Dict, Any, List, Optional
from openai import OpenAI
from backend.config import settings
from backend.data.dataset import DATASET


# Diverse high-value IT, AI, science, and cognitive growth contexts to generate rich educational sentences
DIVERSE_SCENARIOS = [
    # AI & Modern Technology
    "explaining how neural networks and large language models process human text",
    "discussing ethical AI development, algorithmic bias, and data privacy",
    "building an intelligent automation workflow to eliminate repetitive tasks",
    "analyzing how autonomous systems and robotics are transforming smart cities",
    "evaluating computer vision algorithms used in medical diagnostics",

    # Software Engineering & Computing
    "debugging a complex asynchronous API service and optimizing response latency",
    "comparing microservices architecture versus modular monolithic backend design",
    "implementing robust database indexing to speed up multi-table SQL queries",
    "collaborating on a Git version control branch during an open-source code review",
    "setting up secure continuous integration and automated deployment pipelines",

    # Space, Physics & Deep Science
    "exploring how Earth observation satellites monitor global climate and agriculture",
    "discussing quantum computing principles like superposition and cryptography",
    "analyzing how renewable energy grids store excess solar and wind power",
    "studying the mechanics of black holes, gravity waves, and deep space exploration",
    "understanding how CRISPR gene editing could eliminate hereditary diseases",

    # Human Biology, Psychology & Brain Science
    "examining how deep sleep stages help the human brain consolidate long-term memory",
    "discussing dopamine pathways, habit formation, and digital detox strategies",
    "explaining neuroplasticity and how adults effectively acquire complex new skills",
    "analyzing how proper hydration and nutrition directly boost daily cognitive focus",
    "understanding how mindfulness and deliberate breathing lower stress hormones",

    # Critical Thinking, Economics & Mental Models
    "applying first-principles thinking to break down difficult modern challenges",
    "discussing the power of compound interest and foundational financial literacy",
    "analyzing cognitive biases like confirmation bias during decision-making",
    "debating the balance between rapid technological innovation and societal safety"
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
    "A1": (
        "Beginner level: Focus on simple everyday vocabulary (food, family, routines), "
        "basic sentence structures (Subject + Verb + Object), and Present Simple/Continuous. "
        "Keep sentences clear, direct, and limited to 4-5 words."
    ),
    "A2": (
        "Elementary level: Focus on familiar topics, past routines, and simple future plans. "
        "Use Past Simple, basic modal verbs (can, must, should), and simple conjunctions "
        "(and, but, because, so). Length: 5-6 words."
    ),
    "B1": (
        "Intermediate level: Focus on personal opinions, experiences, and ambitions. "
        "Use Present Perfect, comparative/superlative structures, modal verbs of deduction, "
        "and basic complex clauses (relative clauses, 'if' clauses). Length: 6-7 words."
    ),
    "B2": (
        "Upper-Intermediate level: Focus on abstract ideas, formal/informal nuances, "
        "and technical context. Use mixed conditionals, passive voice, phrasal verbs, "
        "and complex linkers (although, whereas, in spite of). Length: 7-8 words."
    ),
    "C1": (
        "Advanced level: Focus on high-level fluency, subtle tone, and professional/academic contexts. "
        "Use advanced collocations, idiomatic expressions, inversion, subjunctive mood, "
        "and varied cleft sentences. Length: 7-9 words."
    )
    }.get(level.upper(), "Adaptive CEFR English sentence, 5-7 words.")

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
