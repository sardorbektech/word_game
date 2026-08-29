"""Comprehensive 1000 Sentences Dataset (200 per CEFR Level) + English-Uzbek Dictionary."""

# English to Uzbek word translations dictionary for SRS and weak word mastery
WORD_TRANSLATIONS = {
    # Basic / Core
    "i": "men", "you": "sen / siz", "he": "u (o'g'il)", "she": "u (qiz)", "it": "u (narsa)",
    "we": "biz", "they": "ular", "my": "mening", "your": "sizning", "his": "uning",
    "her": "uning", "our": "bizning", "their": "ularning", "this": "bu", "that": "ana u",
    "these": "bular", "those": "anavi", "am": "bo'lmoq", "is": "bo'lmoq / dir", "are": "bo'lmoq",
    "was": "edi", "were": "edilar", "have": "ega bo'lmoq", "has": "bor", "had": "bor edi",
    "do": "qilmoq", "does": "bajarmoq", "did": "qildi", "will": "bo'ladi (kelasi)", "can": "qila olmoq",
    "could": "qila olar edi", "should": "kerak / lozim", "would": "bo'lardi", "must": "shart",
    "go": "bormoq", "went": "bordi", "come": "kelmoq", "came": "keldi", "see": "ko'rmoq",
    "saw": "ko'rdi", "know": "bilmoq", "knew": "bildi", "think": "o'ylamoq", "thought": "o'yladi",
    "take": "olmoq", "took": "oldi", "make": "yasamoq / qilmoq", "made": "yasadi", "get": "olmoq / yetishmoq",
    "got": "oldi", "give": "bermoq", "gave": "berdi", "find": "topmoq", "found": "topdi",
    "tell": "aytmoq", "told": "aytdi", "ask": "so'ramoq", "work": "ishlamoq", "seem": "tuyulmoq",
    "feel": "his qilmoq", "try": "harakat qilmoq", "leave": "tark etmoq", "call": "qo'ng'iroq qilmoq",

    # Common Nouns & Adjectives
    "time": "vaqt", "year": "yil", "people": "odamlar", "way": "yo'l / usul", "day": "kun",
    "man": "erkak", "world": "dunyo", "life": "hayot", "hand": "qo'l", "part": "qism",
    "child": "bola", "eye": "ko'z", "woman": "ayol", "place": "joy", "work": "ish",
    "week": "hafta", "case": "holat", "point": "nuqta", "government": "hukumat", "company": "kompaniya",
    "number": "raqam", "group": "guruh", "problem": "muammo", "fact": "fakt", "good": "yaxshi",
    "new": "yangi", "first": "birinchi", "last": "oxirgi", "long": "uzun", "great": "buyuk / ajoyib",
    "little": "kichik", "own": "shaxsiy", "other": "boshqa", "old": "eski / qari", "right": "to'g'ri",
    "big": "katta", "high": "baland", "different": "har xil", "small": "kichik", "large": "yirik",
    "next": "keyingi", "early": "erta", "young": "yosh", "important": "muhim", "few": "ozgina",
    "public": "ommaviy", "bad": "yomon", "same": "bir xil", "able": "qodir",

    # Adverbs & Prepositions
    "to": "ga", "of": "ning", "in": "ichida", "for": "uchun", "on": "ustida", "with": "bilan",
    "at": "da", "by": "orqali / tomonidan", "from": "dan", "up": "yuqoriga", "about": "haqida",
    "into": "ichiga", "over": "ustidan", "after": "keyin", "beneath": "ostida", "under": "ostida",
    "above": "yuqorisida", "not": "emas / yo'q", "also": "shuningdek", "very": "juda", "often": "tez-tez",
    "always": "doimo", "never": "hech qachon", "sometimes": "ba'zan", "usually": "odatda",
    "already": "allaqachon", "almost": "deyarli", "enough": "yetarli", "together": "birgalikda",
    "although": "garchi / garchand", "because": "chunki", "instead": "o'rniga", "however": "ammo / biroq",
    "therefore": "shuning uchun", "moreover": "bundan tashqari", "meanwhile": "shu vaqtda",

    # Technology & Science
    "computer": "kompyuter", "internet": "internet", "software": "dasturiy ta'minot", "hardware": "qurilmalar",
    "algorithm": "algoritm", "data": "ma'lumotlar", "network": "tarmoq", "security": "xavfsizlik",
    "artificial": "sun'iy", "intelligence": "intellekt / aql", "machine": "mashina", "learning": "o'rganish",
    "neural": "neyron", "technology": "texnologiya", "science": "fan", "research": "tadqiqot",
    "scientist": "olim", "planet": "sayyora", "universe": "koinot", "energy": "energiya",
    "renewable": "qayta tiklanadigan", "quantum": "kvant", "accuracy": "aniqlik", "discovery": "kashfiyot",
    "development": "rivojlanish", "innovation": "innovatsiya", "analysis": "tahlil", "database": "ma'lumotlar bazasi",

    # Education & Daily Life
    "university": "universitet", "school": "maktab", "student": "talaba / o'quvchi", "teacher": "o'qituvchi",
    "library": "kutubxona", "book": "kitob", "lesson": "dars", "exam": "imtihon", "knowledge": "bilim",
    "language": "til", "practice": "mashq / amaliyot", "coffee": "qahva", "tea": "choy", "water": "suv",
    "breakfast": "nonushta", "lunch": "tushlik", "dinner": "kechki ovqat", "morning": "ertalab",
    "evening": "kechqurun", "night": "tun", "friend": "do'st", "family": "oila", "travel": "sayohat",
    "city": "shahar", "country": "mamlakat", "modern": "zamonaviy", "famous": "mashhur",
    "beautiful": "chiroyli", "tashkent": "Toshkent", "samarkand": "Samarqand", "uzbekistan": "O'zbekiston",
    "germany": "Germaniya", "berlin": "Berlin", "fast": "tez", "faster": "tezroq", "easy": "oson"
}


def get_word_translation(word: str) -> str:
    """Finds Uzbek translation for given English word with cleaning and fallbacks."""
    clean = word.strip().lower().replace("'", "").replace(".", "").replace(",", "")
    if clean in WORD_TRANSLATIONS:
        return WORD_TRANSLATIONS[clean]

    # Try singular if ends with s
    if clean.endswith("s") and clean[:-1] in WORD_TRANSLATIONS:
        return WORD_TRANSLATIONS[clean[:-1]] + "lar"

    # Try verb base if ends with ing / ed
    if clean.endswith("ing") and clean[:-3] in WORD_TRANSLATIONS:
        return WORD_TRANSLATIONS[clean[:-3]] + "moqda"
    if clean.endswith("ed") and clean[:-2] in WORD_TRANSLATIONS:
        return WORD_TRANSLATIONS[clean[:-2]] + "gan"

    return "o'rganilayotgan so'z"

# 500 High-Quality Curated Sentences (100 per CEFR level, rewritten by CEFR level)
DATASET = {
  "A1": [
    {
      "source_text": "Men har kuni ertalab soat yettida uyg'onaman.",
      "target_text": "I wake up at seven every morning.",
      "words": [
        "I",
        "wake",
        "up",
        "at",
        "seven",
        "every",
        "morning"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Men maktabga piyoda boraman.",
      "target_text": "I walk to school.",
      "words": [
        "I",
        "walk",
        "to",
        "school"
      ],
      "topic": "School"
    },
    {
      "source_text": "Uning ukasi futbol o'ynashni yaxshi ko'radi.",
      "target_text": "His brother likes playing football.",
      "words": [
        "His",
        "brother",
        "likes",
        "playing",
        "football"
      ],
      "topic": "Family"
    },
    {
      "source_text": "Biz kechqurun birga choy ichamiz.",
      "target_text": "We drink tea together in the evening.",
      "words": [
        "We",
        "drink",
        "tea",
        "together",
        "in",
        "the",
        "evening"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Mening xonam kichik, lekin qulay.",
      "target_text": "My room is small but comfortable.",
      "words": [
        "My",
        "room",
        "is",
        "small",
        "but",
        "comfortable"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "U bugun yangi ko'ylak kiydi.",
      "target_text": "She wore a new dress today.",
      "words": [
        "She",
        "wore",
        "a",
        "new",
        "dress",
        "today"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Ular parkda velosiped haydashadi.",
      "target_text": "They ride bicycles in the park.",
      "words": [
        "They",
        "ride",
        "bicycles",
        "in",
        "the",
        "park"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Men dam olish kunlari kitob o'qiyman.",
      "target_text": "I read books at the weekend.",
      "words": [
        "I",
        "read",
        "books",
        "at",
        "the",
        "weekend"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Bizning uyimiz universitetga yaqin.",
      "target_text": "Our house is near the university.",
      "words": [
        "Our",
        "house",
        "is",
        "near",
        "the",
        "university"
      ],
      "topic": "City Life"
    },
    {
      "source_text": "Bugun osmon juda bulutsiz.",
      "target_text": "The sky is very clear today.",
      "words": [
        "The",
        "sky",
        "is",
        "very",
        "clear",
        "today"
      ],
      "topic": "Weather"
    },
    {
      "source_text": "Men singlimga uy vazifasida yordam beraman.",
      "target_text": "I help my sister with her homework.",
      "words": [
        "I",
        "help",
        "my",
        "sister",
        "with",
        "her",
        "homework"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U har kuni avtobusda ishga boradi.",
      "target_text": "He goes to work by bus every day.",
      "words": [
        "He",
        "goes",
        "to",
        "work",
        "by",
        "bus",
        "every",
        "day"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Mushuk divan ustida uxlayapti.",
      "target_text": "The cat is sleeping on the sofa.",
      "words": [
        "The",
        "cat",
        "is",
        "sleeping",
        "on",
        "the",
        "sofa"
      ],
      "topic": "Animals"
    },
    {
      "source_text": "Men sovuq suvni yaxshi ko'raman.",
      "target_text": "I like cold water.",
      "words": [
        "I",
        "like",
        "cold",
        "water"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Biz kecha yangi film ko'rdik.",
      "target_text": "We watched a new movie yesterday.",
      "words": [
        "We",
        "watched",
        "a",
        "new",
        "movie",
        "yesterday"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Otam har kuni mashina haydaydi.",
      "target_text": "My father drives a car every day.",
      "words": [
        "My",
        "father",
        "drives",
        "a",
        "car",
        "every",
        "day"
      ],
      "topic": "Family"
    },
    {
      "source_text": "Ular yakshanba kuni buvisinikiga borishadi.",
      "target_text": "They visit their grandmother on Sunday.",
      "words": [
        "They",
        "visit",
        "their",
        "grandmother",
        "on",
        "Sunday"
      ],
      "topic": "Family"
    },
    {
      "source_text": "Men inglizcha yangi so'zlarni yozaman.",
      "target_text": "I write new English words.",
      "words": [
        "I",
        "write",
        "new",
        "English",
        "words"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Bu do'kon ertalab soat to'qqizda ochiladi.",
      "target_text": "This shop opens at nine in the morning.",
      "words": [
        "This",
        "shop",
        "opens",
        "at",
        "nine",
        "in",
        "the",
        "morning"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Men telefonimdan musiqa tinglayman.",
      "target_text": "I listen to music on my phone.",
      "words": [
        "I",
        "listen",
        "to",
        "music",
        "on",
        "my",
        "phone"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "U yangi kompyuter sotib oldi.",
      "target_text": "He bought a new computer.",
      "words": [
        "He",
        "bought",
        "a",
        "new",
        "computer"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Biz oshxonada nonushta qilamiz.",
      "target_text": "We have breakfast in the kitchen.",
      "words": [
        "We",
        "have",
        "breakfast",
        "in",
        "the",
        "kitchen"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Mening do'stim juda yaxshi shaxmatchi.",
      "target_text": "My friend is a very good chess player.",
      "words": [
        "My",
        "friend",
        "is",
        "a",
        "very",
        "good",
        "chess",
        "player"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Ular daryo yaqinida yashashadi.",
      "target_text": "They live near the river.",
      "words": [
        "They",
        "live",
        "near",
        "the",
        "river"
      ],
      "topic": "Nature"
    },
    {
      "source_text": "Qishda biz issiq kiyim kiyamiz.",
      "target_text": "We wear warm clothes in winter.",
      "words": [
        "We",
        "wear",
        "warm",
        "clothes",
        "in",
        "winter"
      ],
      "topic": "Weather"
    },
    {
      "source_text": "Men har kuni ikki stakan choy ichaman.",
      "target_text": "I drink two cups of tea every day.",
      "words": [
        "I",
        "drink",
        "two",
        "cups",
        "of",
        "tea",
        "every",
        "day"
      ],
      "topic": "Food"
    },
    {
      "source_text": "U maktabda ingliz tilini o'rganadi.",
      "target_text": "She learns English at school.",
      "words": [
        "She",
        "learns",
        "English",
        "at",
        "school"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Biz kecha bozordan olma oldik.",
      "target_text": "We bought apples at the market yesterday.",
      "words": [
        "We",
        "bought",
        "apples",
        "at",
        "the",
        "market",
        "yesterday"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Mening akam universitet talabasi.",
      "target_text": "My brother is a university student.",
      "words": [
        "My",
        "brother",
        "is",
        "a",
        "university",
        "student"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular hozir bog'da ishlashyapti.",
      "target_text": "They are working in the garden now.",
      "words": [
        "They",
        "are",
        "working",
        "in",
        "the",
        "garden",
        "now"
      ],
      "topic": "Nature"
    },
    {
      "source_text": "Men ertalab yuzimni yuvaman.",
      "target_text": "I wash my face in the morning.",
      "words": [
        "I",
        "wash",
        "my",
        "face",
        "in",
        "the",
        "morning"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Bu xona juda yorug'.",
      "target_text": "This room is very bright.",
      "words": [
        "This",
        "room",
        "is",
        "very",
        "bright"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "U har shanba kuni tennis o'ynaydi.",
      "target_text": "He plays tennis every Saturday.",
      "words": [
        "He",
        "plays",
        "tennis",
        "every",
        "Saturday"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Men do'stim bilan kafeda uchrashdim.",
      "target_text": "I met my friend at a cafe.",
      "words": [
        "I",
        "met",
        "my",
        "friend",
        "at",
        "a",
        "cafe"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Biz yozda tog'larga boramiz.",
      "target_text": "We go to the mountains in summer.",
      "words": [
        "We",
        "go",
        "to",
        "the",
        "mountains",
        "in",
        "summer"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "U samolyotda Toshkentga uchdi.",
      "target_text": "She flew to Tashkent by plane.",
      "words": [
        "She",
        "flew",
        "to",
        "Tashkent",
        "by",
        "plane"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Men yangi ruchkamni stolga qo'ydim.",
      "target_text": "I put my new pen on the table.",
      "words": [
        "I",
        "put",
        "my",
        "new",
        "pen",
        "on",
        "the",
        "table"
      ],
      "topic": "School"
    },
    {
      "source_text": "Bolalar hovlida kulishyapti.",
      "target_text": "The children are laughing in the yard.",
      "words": [
        "The",
        "children",
        "are",
        "laughing",
        "in",
        "the",
        "yard"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Quyosh ertalab sharqdan chiqadi.",
      "target_text": "The sun rises in the east in the morning.",
      "words": [
        "The",
        "sun",
        "rises",
        "in",
        "the",
        "east",
        "in",
        "the",
        "morning"
      ],
      "topic": "Facts"
    },
    {
      "source_text": "Men bugun juda bandman.",
      "target_text": "I am very busy today.",
      "words": [
        "I",
        "am",
        "very",
        "busy",
        "today"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Ular kecha bog'da suratga tushishdi.",
      "target_text": "They took pictures in the park yesterday.",
      "words": [
        "They",
        "took",
        "pictures",
        "in",
        "the",
        "park",
        "yesterday"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Mening onam mazali sho'rva pishiradi.",
      "target_text": "My mother cooks delicious soup.",
      "words": [
        "My",
        "mother",
        "cooks",
        "delicious",
        "soup"
      ],
      "topic": "Food"
    },
    {
      "source_text": "U har doim menga yordam beradi.",
      "target_text": "He always helps me.",
      "words": [
        "He",
        "always",
        "helps",
        "me"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Biz yangi o'qituvchimiz bilan tanishdik.",
      "target_text": "We met our new teacher.",
      "words": [
        "We",
        "met",
        "our",
        "new",
        "teacher"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men kecha soat o'nda uxladim.",
      "target_text": "I went to bed at ten last night.",
      "words": [
        "I",
        "went",
        "to",
        "bed",
        "at",
        "ten",
        "last",
        "night"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Uning telefoni stol ustida.",
      "target_text": "Her phone is on the table.",
      "words": [
        "Her",
        "phone",
        "is",
        "on",
        "the",
        "table"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Men har kuni kompyuterimdan foydalanaman.",
      "target_text": "I use my computer every day.",
      "words": [
        "I",
        "use",
        "my",
        "computer",
        "every",
        "day"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ular darsdan keyin futbol o'ynashadi.",
      "target_text": "They play football after class.",
      "words": [
        "They",
        "play",
        "football",
        "after",
        "class"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Bugun havo kechagidan issiqroq.",
      "target_text": "The weather is warmer than yesterday.",
      "words": [
        "The",
        "weather",
        "is",
        "warmer",
        "than",
        "yesterday"
      ],
      "topic": "Weather"
    },
    {
      "source_text": "Men yangi poyabzal kiyib ko'rdim.",
      "target_text": "I tried on new shoes.",
      "words": [
        "I",
        "tried",
        "on",
        "new",
        "shoes"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Bizning shahrimizda katta park bor.",
      "target_text": "There is a big park in our city.",
      "words": [
        "There",
        "is",
        "a",
        "big",
        "park",
        "in",
        "our",
        "city"
      ],
      "topic": "City Life"
    },
    {
      "source_text": "Mening itim to'p bilan o'ynaydi.",
      "target_text": "My dog plays with a ball.",
      "words": [
        "My",
        "dog",
        "plays",
        "with",
        "a",
        "ball"
      ],
      "topic": "Animals"
    },
    {
      "source_text": "U daraxt tagida kitob o'qiyapti.",
      "target_text": "She is reading a book under a tree.",
      "words": [
        "She",
        "is",
        "reading",
        "a",
        "book",
        "under",
        "a",
        "tree"
      ],
      "topic": "Nature"
    },
    {
      "source_text": "Men ingliz tilida oddiy gaplar tuza olaman.",
      "target_text": "I can make simple sentences in English.",
      "words": [
        "I",
        "can",
        "make",
        "simple",
        "sentences",
        "in",
        "English"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular bugun uyda qolishadi.",
      "target_text": "They are staying at home today.",
      "words": [
        "They",
        "are",
        "staying",
        "at",
        "home",
        "today"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Men kecha do'stimdan xabar oldim.",
      "target_text": "I got a message from my friend yesterday.",
      "words": [
        "I",
        "got",
        "a",
        "message",
        "from",
        "my",
        "friend",
        "yesterday"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "U nonushtaga tuxum va non yeydi.",
      "target_text": "He eats eggs and bread for breakfast.",
      "words": [
        "He",
        "eats",
        "eggs",
        "and",
        "bread",
        "for",
        "breakfast"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Bizning o'qituvchimiz juda mehribon.",
      "target_text": "Our teacher is very kind.",
      "words": [
        "Our",
        "teacher",
        "is",
        "very",
        "kind"
      ],
      "topic": "School"
    },
    {
      "source_text": "Men har oy yangi kitob sotib olaman.",
      "target_text": "I buy a new book every month.",
      "words": [
        "I",
        "buy",
        "a",
        "new",
        "book",
        "every",
        "month"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular yangi uyga ko'chib o'tishdi.",
      "target_text": "They moved to a new house.",
      "words": [
        "They",
        "moved",
        "to",
        "a",
        "new",
        "house"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Men bugun avtobusni kutyapman.",
      "target_text": "I am waiting for the bus today.",
      "words": [
        "I",
        "am",
        "waiting",
        "for",
        "the",
        "bus",
        "today"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "U tez yugura oladi.",
      "target_text": "She can run fast.",
      "words": [
        "She",
        "can",
        "run",
        "fast"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Biz Samarqandda uch kun qoldik.",
      "target_text": "We stayed in Samarkand for three days.",
      "words": [
        "We",
        "stayed",
        "in",
        "Samarkand",
        "for",
        "three",
        "days"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Toshkentda ko'plab chiroyli binolar bor.",
      "target_text": "There are many beautiful buildings in Tashkent.",
      "words": [
        "There",
        "are",
        "many",
        "beautiful",
        "buildings",
        "in",
        "Tashkent"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Men kecha muzqaymoq yedim.",
      "target_text": "I ate ice cream yesterday.",
      "words": [
        "I",
        "ate",
        "ice",
        "cream",
        "yesterday"
      ],
      "topic": "Food"
    },
    {
      "source_text": "U derazani ochdi.",
      "target_text": "He opened the window.",
      "words": [
        "He",
        "opened",
        "the",
        "window"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Bolalar rangli rasmlar chizishyapti.",
      "target_text": "The children are drawing colorful pictures.",
      "words": [
        "The",
        "children",
        "are",
        "drawing",
        "colorful",
        "pictures"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Men ertaga kutubxonaga boraman.",
      "target_text": "I will go to the library tomorrow.",
      "words": [
        "I",
        "will",
        "go",
        "to",
        "the",
        "library",
        "tomorrow"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Biz kechqurun televizor ko'ramiz.",
      "target_text": "We watch television in the evening.",
      "words": [
        "We",
        "watch",
        "television",
        "in",
        "the",
        "evening"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "U yangi qo'shiqni yaxshi ko'radi.",
      "target_text": "She likes the new song.",
      "words": [
        "She",
        "likes",
        "the",
        "new",
        "song"
      ],
      "topic": "Music"
    },
    {
      "source_text": "Men do'stimga tug'ilgan kun sovg'asi berdim.",
      "target_text": "I gave my friend a birthday present.",
      "words": [
        "I",
        "gave",
        "my",
        "friend",
        "a",
        "birthday",
        "present"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Ular katta stol atrofida o'tirishdi.",
      "target_text": "They sat around a big table.",
      "words": [
        "They",
        "sat",
        "around",
        "a",
        "big",
        "table"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Mening otam ertalab gazeta o'qiydi.",
      "target_text": "My father reads the newspaper in the morning.",
      "words": [
        "My",
        "father",
        "reads",
        "the",
        "newspaper",
        "in",
        "the",
        "morning"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Bu sumka juda yengil.",
      "target_text": "This bag is very light.",
      "words": [
        "This",
        "bag",
        "is",
        "very",
        "light"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Men har kuni tishlarimni tozalayman.",
      "target_text": "I brush my teeth every day.",
      "words": [
        "I",
        "brush",
        "my",
        "teeth",
        "every",
        "day"
      ],
      "topic": "Health"
    },
    {
      "source_text": "U ko'p suv ichadi.",
      "target_text": "He drinks a lot of water.",
      "words": [
        "He",
        "drinks",
        "a",
        "lot",
        "of",
        "water"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Biz yakshanba kuni uyimizni tozalaymiz.",
      "target_text": "We clean our house on Sunday.",
      "words": [
        "We",
        "clean",
        "our",
        "house",
        "on",
        "Sunday"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Qushlar daraxtlarda sayrayapti.",
      "target_text": "The birds are singing in the trees.",
      "words": [
        "The",
        "birds",
        "are",
        "singing",
        "in",
        "the",
        "trees"
      ],
      "topic": "Nature"
    },
    {
      "source_text": "Men yangi til o'rganishni xohlayman.",
      "target_text": "I want to learn a new language.",
      "words": [
        "I",
        "want",
        "to",
        "learn",
        "a",
        "new",
        "language"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular Germaniyaga sayohat qilishni xohlashadi.",
      "target_text": "They want to travel to Germany.",
      "words": [
        "They",
        "want",
        "to",
        "travel",
        "to",
        "Germany"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Berlin Germaniyaning poytaxti.",
      "target_text": "Berlin is the capital of Germany.",
      "words": [
        "Berlin",
        "is",
        "the",
        "capital",
        "of",
        "Germany"
      ],
      "topic": "Germany"
    },
    {
      "source_text": "Men kecha yangi o'yin o'ynadim.",
      "target_text": "I played a new game yesterday.",
      "words": [
        "I",
        "played",
        "a",
        "new",
        "game",
        "yesterday"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "U har kuni ofisda ishlaydi.",
      "target_text": "She works in an office every day.",
      "words": [
        "She",
        "works",
        "in",
        "an",
        "office",
        "every",
        "day"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Biz ertalab bog'da yuguramiz.",
      "target_text": "We run in the park in the morning.",
      "words": [
        "We",
        "run",
        "in",
        "the",
        "park",
        "in",
        "the",
        "morning"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Men darsda o'qituvchini tinglayman.",
      "target_text": "I listen to the teacher in class.",
      "words": [
        "I",
        "listen",
        "to",
        "the",
        "teacher",
        "in",
        "class"
      ],
      "topic": "School"
    },
    {
      "source_text": "Ular hozir tushlik tayyorlashyapti.",
      "target_text": "They are preparing lunch now.",
      "words": [
        "They",
        "are",
        "preparing",
        "lunch",
        "now"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Men telefonimni uyda qoldirib ketdim.",
      "target_text": "I left my phone at home.",
      "words": [
        "I",
        "left",
        "my",
        "phone",
        "at",
        "home"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "U kecha menga qo'ng'iroq qildi.",
      "target_text": "He called me yesterday.",
      "words": [
        "He",
        "called",
        "me",
        "yesterday"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Biz yangi loyiha haqida gaplashdik.",
      "target_text": "We talked about the new project.",
      "words": [
        "We",
        "talked",
        "about",
        "the",
        "new",
        "project"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Men chiroyli gullarni yaxshi ko'raman.",
      "target_text": "I like beautiful flowers.",
      "words": [
        "I",
        "like",
        "beautiful",
        "flowers"
      ],
      "topic": "Nature"
    },
    {
      "source_text": "Yozda kunlar uzun bo'ladi.",
      "target_text": "The days are long in summer.",
      "words": [
        "The",
        "days",
        "are",
        "long",
        "in",
        "summer"
      ],
      "topic": "Weather"
    },
    {
      "source_text": "Men har kuni yangi narsalarni o'rganaman.",
      "target_text": "I learn new things every day.",
      "words": [
        "I",
        "learn",
        "new",
        "things",
        "every",
        "day"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular stadionda futbol tomosha qilishdi.",
      "target_text": "They watched football at the stadium.",
      "words": [
        "They",
        "watched",
        "football",
        "at",
        "the",
        "stadium"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Men bugun qora ko'ylak kiydim.",
      "target_text": "I wore a black shirt today.",
      "words": [
        "I",
        "wore",
        "a",
        "black",
        "shirt",
        "today"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Bizning oilamiz besh kishidan iborat.",
      "target_text": "There are five people in my family.",
      "words": [
        "There",
        "are",
        "five",
        "people",
        "in",
        "my",
        "family"
      ],
      "topic": "Family"
    },
    {
      "source_text": "U kecha juda chiroyli rasm chizdi.",
      "target_text": "She drew a very beautiful picture yesterday.",
      "words": [
        "She",
        "drew",
        "a",
        "very",
        "beautiful",
        "picture",
        "yesterday"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Men ertaga do'stim bilan uchrashaman.",
      "target_text": "I will meet my friend tomorrow.",
      "words": [
        "I",
        "will",
        "meet",
        "my",
        "friend",
        "tomorrow"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Men yangi telefonimda inglizcha lug'atdan foydalanaman.",
      "target_text": "I use an English dictionary on my new phone.",
      "words": [
        "I",
        "use",
        "an",
        "English",
        "dictionary",
        "on",
        "my",
        "new",
        "phone"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "U avtobusga chiqishdan oldin chipta sotib oldi.",
      "target_text": "She bought a ticket before getting on the bus.",
      "words": [
        "She",
        "bought",
        "a",
        "ticket",
        "before",
        "getting",
        "on",
        "the",
        "bus"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Biz o'tgan yozda O'zbekistonning bir nechta shaharlarini ko'rdik.",
      "target_text": "We visited several cities in Uzbekistan last summer.",
      "words": [
        "We",
        "visited",
        "several",
        "cities",
        "in",
        "Uzbekistan",
        "last",
        "summer"
      ],
      "topic": "Uzbekistan"
    }
  ],
  "A2": [
    {
      "source_text": "Men o'tgan oy ingliz tili kursiga yozildim.",
      "target_text": "I joined an English course last month.",
      "words": [
        "I",
        "joined",
        "an",
        "English",
        "course",
        "last",
        "month"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Biz dam olish kunlari yangi muzeyga borishni rejalashtiryapmiz.",
      "target_text": "We are planning to visit a new museum at the weekend.",
      "words": [
        "We",
        "are",
        "planning",
        "to",
        "visit",
        "a",
        "new",
        "museum",
        "at",
        "the",
        "weekend"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "U kecha kompyuteridagi eski fayllarni o'chirdi.",
      "target_text": "He deleted the old files from his computer yesterday.",
      "words": [
        "He",
        "deleted",
        "the",
        "old",
        "files",
        "from",
        "his",
        "computer",
        "yesterday"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Agar vaqtim bo'lsa, kechqurun kitob o'qiyman.",
      "target_text": "If I have time, I will read a book in the evening.",
      "words": [
        "If",
        "I",
        "have",
        "time",
        "I",
        "will",
        "read",
        "a",
        "book",
        "in",
        "the",
        "evening"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Mening singlim mendan ko'ra tezroq yuguradi.",
      "target_text": "My sister runs faster than I do.",
      "words": [
        "My",
        "sister",
        "runs",
        "faster",
        "than",
        "I",
        "do"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Bu restoran shahardagi boshqa restoranlarga qaraganda arzonroq.",
      "target_text": "This restaurant is cheaper than the others in the city.",
      "words": [
        "This",
        "restaurant",
        "is",
        "cheaper",
        "than",
        "the",
        "others",
        "in",
        "the",
        "city"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Ular yangi kvartiraga o'tgan haftada ko'chib o'tishdi.",
      "target_text": "They moved to a new apartment last week.",
      "words": [
        "They",
        "moved",
        "to",
        "a",
        "new",
        "apartment",
        "last",
        "week"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Men hali bu filmni ko'rmaganman.",
      "target_text": "I have not seen this film yet.",
      "words": [
        "I",
        "have",
        "not",
        "seen",
        "this",
        "film",
        "yet"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "U bugun ertalab kalitlarini topa olmadi.",
      "target_text": "She could not find her keys this morning.",
      "words": [
        "She",
        "could",
        "not",
        "find",
        "her",
        "keys",
        "this",
        "morning"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Biz dars boshlanishidan oldin barcha kitoblarni tayyorladik.",
      "target_text": "We prepared all the books before the lesson started.",
      "words": [
        "We",
        "prepared",
        "all",
        "the",
        "books",
        "before",
        "the",
        "lesson",
        "started"
      ],
      "topic": "School"
    },
    {
      "source_text": "Samarqanddagi tarixiy binolar ko'plab sayyohlarni jalb qiladi.",
      "target_text": "The historic buildings in Samarkand attract many tourists.",
      "words": [
        "The",
        "historic",
        "buildings",
        "in",
        "Samarkand",
        "attract",
        "many",
        "tourists"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Menimcha, onlayn ta'lim band odamlar uchun juda qulay.",
      "target_text": "I think online education is very convenient for busy people.",
      "words": [
        "I",
        "think",
        "online",
        "education",
        "is",
        "very",
        "convenient",
        "for",
        "busy",
        "people"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U yangi dasturdan foydalanishni tezda o'rgandi.",
      "target_text": "He quickly learned how to use the new program.",
      "words": [
        "He",
        "quickly",
        "learned",
        "how",
        "to",
        "use",
        "the",
        "new",
        "program"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "O'qituvchi topshiriqni tushuntirgandan keyin talabalar ishlay boshlashdi.",
      "target_text": "The students started working after the teacher explained the task.",
      "words": [
        "The",
        "students",
        "started",
        "working",
        "after",
        "the",
        "teacher",
        "explained",
        "the",
        "task"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Biz kecha yomg'ir yog'ayotgani uchun uyda qoldik.",
      "target_text": "We stayed at home yesterday because it was raining.",
      "words": [
        "We",
        "stayed",
        "at",
        "home",
        "yesterday",
        "because",
        "it",
        "was",
        "raining"
      ],
      "topic": "Weather"
    },
    {
      "source_text": "Men kelajakda boshqa davlatlarda ishlashni xohlayman.",
      "target_text": "I want to work in other countries in the future.",
      "words": [
        "I",
        "want",
        "to",
        "work",
        "in",
        "other",
        "countries",
        "in",
        "the",
        "future"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U sog'lom bo'lish uchun har kuni piyoda yuradi.",
      "target_text": "She walks every day to stay healthy.",
      "words": [
        "She",
        "walks",
        "every",
        "day",
        "to",
        "stay",
        "healthy"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Do'stim menga yangi ish topishda yordam berdi.",
      "target_text": "My friend helped me find a new job.",
      "words": [
        "My",
        "friend",
        "helped",
        "me",
        "find",
        "a",
        "new",
        "job"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Men bu kitobni ikki kun ichida tugatdim.",
      "target_text": "I finished this book in two days.",
      "words": [
        "I",
        "finished",
        "this",
        "book",
        "in",
        "two",
        "days"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Ular maktabdan keyin kutubxonada uchrashishdi.",
      "target_text": "They met in the library after school.",
      "words": [
        "They",
        "met",
        "in",
        "the",
        "library",
        "after",
        "school"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Agar ertaga yomg'ir yog'masa, biz tog'ga chiqamiz.",
      "target_text": "If it does not rain tomorrow, we will go to the mountains.",
      "words": [
        "If",
        "it",
        "does",
        "not",
        "rain",
        "tomorrow",
        "we",
        "will",
        "go",
        "to",
        "the",
        "mountains"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Men yangi noutbuk sotib olish uchun pul yig'yapman.",
      "target_text": "I am saving money to buy a new laptop.",
      "words": [
        "I",
        "am",
        "saving",
        "money",
        "to",
        "buy",
        "a",
        "new",
        "laptop"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Bu yo'l avvalgidan ancha xavfsizroq.",
      "target_text": "This road is much safer than before.",
      "words": [
        "This",
        "road",
        "is",
        "much",
        "safer",
        "than",
        "before"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "U kecha menga nima bo'lganini aytib berdi.",
      "target_text": "He told me what happened yesterday.",
      "words": [
        "He",
        "told",
        "me",
        "what",
        "happened",
        "yesterday"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "Bizning jamoamiz o'tgan yili musobaqada g'olib bo'ldi.",
      "target_text": "Our team won the competition last year.",
      "words": [
        "Our",
        "team",
        "won",
        "the",
        "competition",
        "last",
        "year"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Olimlar suvning sifatini muntazam tekshirishmoqda.",
      "target_text": "Scientists regularly test the quality of the water.",
      "words": [
        "Scientists",
        "regularly",
        "test",
        "the",
        "quality",
        "of",
        "the",
        "water"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Quyosh energiyasi ko'plab mamlakatlarda tobora ommalashmoqda.",
      "target_text": "Solar energy is becoming more popular in many countries.",
      "words": [
        "Solar",
        "energy",
        "is",
        "becoming",
        "more",
        "popular",
        "in",
        "many",
        "countries"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Men inglizcha filmlarni subtitr bilan ko'rishni yoqtiraman.",
      "target_text": "I like watching English films with subtitles.",
      "words": [
        "I",
        "like",
        "watching",
        "English",
        "films",
        "with",
        "subtitles"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U yangi velosipedini ehtiyotkorlik bilan haydaydi.",
      "target_text": "He rides his new bicycle carefully.",
      "words": [
        "He",
        "rides",
        "his",
        "new",
        "bicycle",
        "carefully"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Biz restoranga kelganimizda, barcha stollar band edi.",
      "target_text": "When we arrived at the restaurant, all the tables were occupied.",
      "words": [
        "When",
        "we",
        "arrived",
        "at",
        "the",
        "restaurant",
        "all",
        "the",
        "tables",
        "were",
        "occupied"
      ],
      "topic": "Food"
    },
    {
      "source_text": "U menga tug'ilgan kunida chiroyli daftar sovg'a qildi.",
      "target_text": "She gave me a beautiful notebook for my birthday.",
      "words": [
        "She",
        "gave",
        "me",
        "a",
        "beautiful",
        "notebook",
        "for",
        "my",
        "birthday"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Men ilgari hech qachon Buxoroga bormagan edim.",
      "target_text": "I had never been to Bukhara before.",
      "words": [
        "I",
        "had",
        "never",
        "been",
        "to",
        "Bukhara",
        "before"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Ular yangi mobil ilovani sinab ko'rishmoqda.",
      "target_text": "They are trying a new mobile application.",
      "words": [
        "They",
        "are",
        "trying",
        "a",
        "new",
        "mobile",
        "application"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Akam ishini tugatgach, do'stlari bilan uchrashadi.",
      "target_text": "My brother meets his friends after he finishes work.",
      "words": [
        "My",
        "brother",
        "meets",
        "his",
        "friends",
        "after",
        "he",
        "finishes",
        "work"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Menimcha, muntazam mashq qilish energiyani oshiradi.",
      "target_text": "I think regular exercise increases energy.",
      "words": [
        "I",
        "think",
        "regular",
        "exercise",
        "increases",
        "energy"
      ],
      "topic": "Health"
    },
    {
      "source_text": "U sovuq havoga qaramay ertalab yugurdi.",
      "target_text": "She went running in the morning despite the cold weather.",
      "words": [
        "She",
        "went",
        "running",
        "in",
        "the",
        "morning",
        "despite",
        "the",
        "cold",
        "weather"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Biz o'qituvchimizdan imtihon haqida qo'shimcha ma'lumot so'radik.",
      "target_text": "We asked our teacher for more information about the exam.",
      "words": [
        "We",
        "asked",
        "our",
        "teacher",
        "for",
        "more",
        "information",
        "about",
        "the",
        "exam"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Telefonim buzilgani uchun do'stimning telefonidan foydalandim.",
      "target_text": "I used my friend's phone because mine was broken.",
      "words": [
        "I",
        "used",
        "my",
        "friend's",
        "phone",
        "because",
        "mine",
        "was",
        "broken"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ular ta'til vaqtida dengiz bo'yidagi kichik shaharda qolishdi.",
      "target_text": "They stayed in a small seaside town during their holiday.",
      "words": [
        "They",
        "stayed",
        "in",
        "a",
        "small",
        "seaside",
        "town",
        "during",
        "their",
        "holiday"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Bu masalani hal qilish uchun ko'proq vaqt kerak.",
      "target_text": "We need more time to solve this problem.",
      "words": [
        "We",
        "need",
        "more",
        "time",
        "to",
        "solve",
        "this",
        "problem"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men har kuni yangi beshta so'zni yodlashga harakat qilaman.",
      "target_text": "I try to learn five new words every day.",
      "words": [
        "I",
        "try",
        "to",
        "learn",
        "five",
        "new",
        "words",
        "every",
        "day"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U kecha juda charchagan edi, shuning uchun erta uxlagan.",
      "target_text": "He was very tired yesterday, so he went to bed early.",
      "words": [
        "He",
        "was",
        "very",
        "tired",
        "yesterday",
        "so",
        "he",
        "went",
        "to",
        "bed",
        "early"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Biz yangi uyimiz uchun mebel tanladik.",
      "target_text": "We chose furniture for our new house.",
      "words": [
        "We",
        "chose",
        "furniture",
        "for",
        "our",
        "new",
        "house"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Qishloqda havo shahardagidan tozaroq.",
      "target_text": "The air in the countryside is cleaner than in the city.",
      "words": [
        "The",
        "air",
        "in",
        "the",
        "countryside",
        "is",
        "cleaner",
        "than",
        "in",
        "the",
        "city"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Men do'stim bilan birga kichik loyiha boshladim.",
      "target_text": "I started a small project with my friend.",
      "words": [
        "I",
        "started",
        "a",
        "small",
        "project",
        "with",
        "my",
        "friend"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U o'tgan hafta yangi kursni tugatgan.",
      "target_text": "She finished the new course last week.",
      "words": [
        "She",
        "finished",
        "the",
        "new",
        "course",
        "last",
        "week"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ko'plab odamlar ishga borishda jamoat transportidan foydalanadi.",
      "target_text": "Many people use public transport to get to work.",
      "words": [
        "Many",
        "people",
        "use",
        "public",
        "transport",
        "to",
        "get",
        "to",
        "work"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Biz ovqatni tayyorlaganimizdan keyin oshxonani tozaladik.",
      "target_text": "We cleaned the kitchen after we prepared the food.",
      "words": [
        "We",
        "cleaned",
        "the",
        "kitchen",
        "after",
        "we",
        "prepared",
        "the",
        "food"
      ],
      "topic": "Food"
    },
    {
      "source_text": "U ingliz tilida gapirishdan oldin ko'p mashq qildi.",
      "target_text": "He practiced a lot before speaking English.",
      "words": [
        "He",
        "practiced",
        "a",
        "lot",
        "before",
        "speaking",
        "English"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men bu shaharni avvalgidan yaxshiroq taniyman.",
      "target_text": "I know this city better than I did before.",
      "words": [
        "I",
        "know",
        "this",
        "city",
        "better",
        "than",
        "I",
        "did",
        "before"
      ],
      "topic": "City Life"
    },
    {
      "source_text": "Ular yangi sport markazida suzishni boshlashdi.",
      "target_text": "They started swimming at the new sports center.",
      "words": [
        "They",
        "started",
        "swimming",
        "at",
        "the",
        "new",
        "sports",
        "center"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Agar sen muntazam o'qisang, ingliz tiling yaxshilanadi.",
      "target_text": "If you study regularly, your English will improve.",
      "words": [
        "If",
        "you",
        "study",
        "regularly",
        "your",
        "English",
        "will",
        "improve"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men kecha do'kondan kerakli narsalarning hammasini topdim.",
      "target_text": "I found everything I needed at the shop yesterday.",
      "words": [
        "I",
        "found",
        "everything",
        "I",
        "needed",
        "at",
        "the",
        "shop",
        "yesterday"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Uning ota-onasi universitet tanlashiga yordam berishdi.",
      "target_text": "Her parents helped her choose a university.",
      "words": [
        "Her",
        "parents",
        "helped",
        "her",
        "choose",
        "a",
        "university"
      ],
      "topic": "Family"
    },
    {
      "source_text": "Biz yangi qo'shnilarimiz bilan tezda do'stlashdik.",
      "target_text": "We quickly became friends with our new neighbors.",
      "words": [
        "We",
        "quickly",
        "became",
        "friends",
        "with",
        "our",
        "new",
        "neighbors"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "O'qituvchi talabalarni guruhlarga bo'lib, vazifa berdi.",
      "target_text": "The teacher divided the students into groups and gave them a task.",
      "words": [
        "The",
        "teacher",
        "divided",
        "the",
        "students",
        "into",
        "groups",
        "and",
        "gave",
        "them",
        "a",
        "task"
      ],
      "topic": "School"
    },
    {
      "source_text": "Men sayohatdan oldin mehmonxonani onlayn band qildim.",
      "target_text": "I booked the hotel online before the trip.",
      "words": [
        "I",
        "booked",
        "the",
        "hotel",
        "online",
        "before",
        "the",
        "trip"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Ular loyiha uchun kerakli ma'lumotlarni internetdan topishdi.",
      "target_text": "They found the information they needed for the project online.",
      "words": [
        "They",
        "found",
        "the",
        "information",
        "they",
        "needed",
        "for",
        "the",
        "project",
        "online"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Olimlar yangi o'simlik turini o'rganishni boshlashdi.",
      "target_text": "Scientists started studying a new plant species.",
      "words": [
        "Scientists",
        "started",
        "studying",
        "a",
        "new",
        "plant",
        "species"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Men yomg'irli kunlarda uyda film ko'rishni afzal ko'raman.",
      "target_text": "I prefer watching films at home on rainy days.",
      "words": [
        "I",
        "prefer",
        "watching",
        "films",
        "at",
        "home",
        "on",
        "rainy",
        "days"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "U bu vazifani o'zi bajara olganidan xursand bo'ldi.",
      "target_text": "She was happy that she could do the task herself.",
      "words": [
        "She",
        "was",
        "happy",
        "that",
        "she",
        "could",
        "do",
        "the",
        "task",
        "herself"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Bizning shaharda yangi kutubxona o'tgan yili ochilgan.",
      "target_text": "A new library was opened in our city last year.",
      "words": [
        "A",
        "new",
        "library",
        "was",
        "opened",
        "in",
        "our",
        "city",
        "last",
        "year"
      ],
      "topic": "City Life"
    },
    {
      "source_text": "Men hali universitetdagi yangi professorim bilan gaplashmadim.",
      "target_text": "I have not spoken to my new university professor yet.",
      "words": [
        "I",
        "have",
        "not",
        "spoken",
        "to",
        "my",
        "new",
        "university",
        "professor",
        "yet"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U har kuni ishga ketishdan oldin nonushta qiladi.",
      "target_text": "He has breakfast before going to work every day.",
      "words": [
        "He",
        "has",
        "breakfast",
        "before",
        "going",
        "to",
        "work",
        "every",
        "day"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Sayyohlar qadimiy shaharning tor ko'chalarida sayr qilishdi.",
      "target_text": "The tourists walked through the narrow streets of the ancient city.",
      "words": [
        "The",
        "tourists",
        "walked",
        "through",
        "the",
        "narrow",
        "streets",
        "of",
        "the",
        "ancient",
        "city"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Men telefonimda juda ko'p surat saqlamayman.",
      "target_text": "I do not keep many photos on my phone.",
      "words": [
        "I",
        "do",
        "not",
        "keep",
        "many",
        "photos",
        "on",
        "my",
        "phone"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ular musobaqaga tayyorgarlik ko'rish uchun har kuni mashq qilishdi.",
      "target_text": "They trained every day to prepare for the competition.",
      "words": [
        "They",
        "trained",
        "every",
        "day",
        "to",
        "prepare",
        "for",
        "the",
        "competition"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Bu kitob menga yangi g'oyalar haqida o'ylashga yordam berdi.",
      "target_text": "This book helped me think about new ideas.",
      "words": [
        "This",
        "book",
        "helped",
        "me",
        "think",
        "about",
        "new",
        "ideas"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Agar avtobus kechiksa, men taksiga o'tiraman.",
      "target_text": "If the bus is late, I will take a taxi.",
      "words": [
        "If",
        "the",
        "bus",
        "is",
        "late",
        "I",
        "will",
        "take",
        "a",
        "taxi"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Biz kecha yangi kafeda juda mazali ovqat yedik.",
      "target_text": "We ate very tasty food at a new cafe yesterday.",
      "words": [
        "We",
        "ate",
        "very",
        "tasty",
        "food",
        "at",
        "a",
        "new",
        "cafe",
        "yesterday"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Ular tabiatni himoya qilish haqida maktabda loyiha tayyorlashdi.",
      "target_text": "They prepared a school project about protecting nature.",
      "words": [
        "They",
        "prepared",
        "a",
        "school",
        "project",
        "about",
        "protecting",
        "nature"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Men inglizcha gapirishda xato qilishdan qo'rqmayman.",
      "target_text": "I am not afraid of making mistakes when I speak English.",
      "words": [
        "I",
        "am",
        "not",
        "afraid",
        "of",
        "making",
        "mistakes",
        "when",
        "I",
        "speak",
        "English"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U yangi ishiga birinchi kundanoq qiziqib qoldi.",
      "target_text": "He became interested in his new job from the first day.",
      "words": [
        "He",
        "became",
        "interested",
        "in",
        "his",
        "new",
        "job",
        "from",
        "the",
        "first",
        "day"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Biz oilamiz bilan bayramni uyda nishonladik.",
      "target_text": "We celebrated the holiday at home with our family.",
      "words": [
        "We",
        "celebrated",
        "the",
        "holiday",
        "at",
        "home",
        "with",
        "our",
        "family"
      ],
      "topic": "Family"
    },
    {
      "source_text": "Men bu masalani o'qituvchim bilan muhokama qilishni rejalashtiryapman.",
      "target_text": "I am planning to discuss this problem with my teacher.",
      "words": [
        "I",
        "am",
        "planning",
        "to",
        "discuss",
        "this",
        "problem",
        "with",
        "my",
        "teacher"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U yangi telefonining barcha imkoniyatlarini hali bilmaydi.",
      "target_text": "She does not know all the features of her new phone yet.",
      "words": [
        "She",
        "does",
        "not",
        "know",
        "all",
        "the",
        "features",
        "of",
        "her",
        "new",
        "phone",
        "yet"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Kecha shamol kuchli bo'lgani uchun daraxtlar egildi.",
      "target_text": "The trees bent because the wind was strong yesterday.",
      "words": [
        "The",
        "trees",
        "bent",
        "because",
        "the",
        "wind",
        "was",
        "strong",
        "yesterday"
      ],
      "topic": "Weather"
    },
    {
      "source_text": "Menimcha, Toshkentda velosiped haydash uchun ko'proq joy kerak.",
      "target_text": "I think Tashkent needs more places for cycling.",
      "words": [
        "I",
        "think",
        "Tashkent",
        "needs",
        "more",
        "places",
        "for",
        "cycling"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Ular o'tgan oy yangi sport zaliga a'zo bo'lishdi.",
      "target_text": "They joined a new gym last month.",
      "words": [
        "They",
        "joined",
        "a",
        "new",
        "gym",
        "last",
        "month"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Men do'stimning maslahatini tinglab, qarorimni o'zgartirdim.",
      "target_text": "I changed my decision after listening to my friend's advice.",
      "words": [
        "I",
        "changed",
        "my",
        "decision",
        "after",
        "listening",
        "to",
        "my",
        "friend's",
        "advice"
      ],
      "topic": "Friendship"
    },
    {
      "source_text": "U o'qishni tugatgandan keyin boshqa shaharga ko'chmoqchi.",
      "target_text": "He wants to move to another city after finishing his studies.",
      "words": [
        "He",
        "wants",
        "to",
        "move",
        "to",
        "another",
        "city",
        "after",
        "finishing",
        "his",
        "studies"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Biz muzeyga kirganimizda, ekskursiya allaqachon boshlangan edi.",
      "target_text": "When we entered the museum, the tour had already started.",
      "words": [
        "When",
        "we",
        "entered",
        "the",
        "museum",
        "the",
        "tour",
        "had",
        "already",
        "started"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Men yangi dastur yordamida vaqtimni yaxshiroq rejalashtiraman.",
      "target_text": "I plan my time better with the help of a new app.",
      "words": [
        "I",
        "plan",
        "my",
        "time",
        "better",
        "with",
        "the",
        "help",
        "of",
        "a",
        "new",
        "app"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ular mahalliy bozordan yangi meva va sabzavotlar sotib olishdi.",
      "target_text": "They bought fresh fruit and vegetables from the local market.",
      "words": [
        "They",
        "bought",
        "fresh",
        "fruit",
        "and",
        "vegetables",
        "from",
        "the",
        "local",
        "market"
      ],
      "topic": "Food"
    },
    {
      "source_text": "O'tgan yili men hozirgidan kamroq inglizcha gapirardim.",
      "target_text": "Last year, I spoke English less than I do now.",
      "words": [
        "Last",
        "year",
        "I",
        "spoke",
        "English",
        "less",
        "than",
        "I",
        "do",
        "now"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Uning jamoasi muhim o'yinda kichik farq bilan g'alaba qozondi.",
      "target_text": "His team won the important match by a small margin.",
      "words": [
        "His",
        "team",
        "won",
        "the",
        "important",
        "match",
        "by",
        "a",
        "small",
        "margin"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Men sog'lom ovqatlanish haqida ko'proq bilishni xohlayman.",
      "target_text": "I want to learn more about healthy eating.",
      "words": [
        "I",
        "want",
        "to",
        "learn",
        "more",
        "about",
        "healthy",
        "eating"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Ular yomg'irdan keyin parkda ko'plab qushlarni ko'rishdi.",
      "target_text": "They saw many birds in the park after the rain.",
      "words": [
        "They",
        "saw",
        "many",
        "birds",
        "in",
        "the",
        "park",
        "after",
        "the",
        "rain"
      ],
      "topic": "Nature"
    },
    {
      "source_text": "Biz dam olish kunlari oilamiz bilan tog'ga chiqishga qaror qildik.",
      "target_text": "We decided to go to the mountains with our family at the weekend.",
      "words": [
        "We",
        "decided",
        "to",
        "go",
        "to",
        "the",
        "mountains",
        "with",
        "our",
        "family",
        "at",
        "the",
        "weekend"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Men bu maqolani o'qib, yangi texnologiya haqida bilib oldim.",
      "target_text": "I learned about a new technology by reading this article.",
      "words": [
        "I",
        "learned",
        "about",
        "a",
        "new",
        "technology",
        "by",
        "reading",
        "this",
        "article"
      ],
      "topic": "Science"
    },
    {
      "source_text": "U yangi dasturda hisob yaratgandan keyin barcha ma'lumotlarini saqladi.",
      "target_text": "After creating an account in the new program, she saved all her information.",
      "words": [
        "After",
        "creating",
        "an",
        "account",
        "in",
        "the",
        "new",
        "program",
        "she",
        "saved",
        "all",
        "her",
        "information"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Biz o'qituvchining savollariga javob berish uchun guruh bo'lib ishladik.",
      "target_text": "We worked as a group to answer the teacher's questions.",
      "words": [
        "We",
        "worked",
        "as",
        "a",
        "group",
        "to",
        "answer",
        "the",
        "teacher's",
        "questions"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men avtobusni o'tkazib yuborganim uchun universitetga kech bordim.",
      "target_text": "I arrived late at university because I missed the bus.",
      "words": [
        "I",
        "arrived",
        "late",
        "at",
        "university",
        "because",
        "I",
        "missed",
        "the",
        "bus"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Ular kelajakda quyosh energiyasidan ko'proq foydalanishga umid qilishmoqda.",
      "target_text": "They hope to use more solar energy in the future.",
      "words": [
        "They",
        "hope",
        "to",
        "use",
        "more",
        "solar",
        "energy",
        "in",
        "the",
        "future"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Bu filmni ko'rganimdan keyin kitobni ham o'qishga qaror qildim.",
      "target_text": "After watching the film, I decided to read the book too.",
      "words": [
        "After",
        "watching",
        "the",
        "film",
        "I",
        "decided",
        "to",
        "read",
        "the",
        "book",
        "too"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "U sog'lig'ini yaxshilash uchun shirinliklarni kamroq yeyishni boshladi.",
      "target_text": "She started eating fewer sweets to improve her health.",
      "words": [
        "She",
        "started",
        "eating",
        "fewer",
        "sweets",
        "to",
        "improve",
        "her",
        "health"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Biz Buxoroga borganda, mahalliy odamlar bilan suhbatlashdik.",
      "target_text": "When we went to Bukhara, we talked with local people.",
      "words": [
        "When",
        "we",
        "went",
        "to",
        "Bukhara",
        "we",
        "talked",
        "with",
        "local",
        "people"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Menimcha, yangi ish topishdan oldin ko'proq tajriba orttirishim kerak.",
      "target_text": "I think I need to gain more experience before finding a new job.",
      "words": [
        "I",
        "think",
        "I",
        "need",
        "to",
        "gain",
        "more",
        "experience",
        "before",
        "finding",
        "a",
        "new",
        "job"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U do'stining tug'ilgan kuniga borish uchun yangi ko'ylak sotib oldi.",
      "target_text": "He bought a new shirt to go to his friend's birthday party.",
      "words": [
        "He",
        "bought",
        "a",
        "new",
        "shirt",
        "to",
        "go",
        "to",
        "his",
        "friend's",
        "birthday",
        "party"
      ],
      "topic": "Shopping"
    },
    {
      "source_text": "Agar ko'proq mashq qilsangiz, keyingi musobaqada yaxshiroq natija ko'rsatishingiz mumkin.",
      "target_text": "If you practice more, you can get a better result in the next competition.",
      "words": [
        "If",
        "you",
        "practice",
        "more",
        "you",
        "can",
        "get",
        "a",
        "better",
        "result",
        "in",
        "the",
        "next",
        "competition"
      ],
      "topic": "Sports"
    }
  ],
  "B1": [
    {
      "source_text": "Zamonaviy sun'iy intellekt tizimlari katta hajmdagi ma'lumotlarni tez tahlil qila oladi.",
      "target_text": "Modern artificial intelligence systems can analyze large amounts of data quickly.",
      "words": [
        "Modern",
        "artificial",
        "intelligence",
        "systems",
        "can",
        "analyze",
        "large",
        "amounts",
        "of",
        "data",
        "quickly"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Bulutli xizmatlar kompaniyalarga ma'lumotlarni turli qurilmalardan boshqarish imkonini beradi.",
      "target_text": "Cloud services allow companies to manage data from different devices.",
      "words": [
        "Cloud",
        "services",
        "allow",
        "companies",
        "to",
        "manage",
        "data",
        "from",
        "different",
        "devices"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Universitet tadqiqotchilari qishloq xo'jaligida suv sarfini kamaytirishning yangi usulini sinab ko'rmoqda.",
      "target_text": "University researchers are testing a new way to reduce water use in agriculture.",
      "words": [
        "University",
        "researchers",
        "are",
        "testing",
        "a",
        "new",
        "way",
        "to",
        "reduce",
        "water",
        "use",
        "in",
        "agriculture"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Agar kompaniyalar xavfsizlikni e'tiborsiz qoldirsa, ular muhim ma'lumotlarni yo'qotishi mumkin.",
      "target_text": "If companies ignore security, they may lose important information.",
      "words": [
        "If",
        "companies",
        "ignore",
        "security",
        "they",
        "may",
        "lose",
        "important",
        "information"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Masofaviy ta'lim ko'plab talabalarga o'z vaqtini mustaqil boshqarish imkonini berdi.",
      "target_text": "Distance learning has allowed many students to manage their time independently.",
      "words": [
        "Distance",
        "learning",
        "has",
        "allowed",
        "many",
        "students",
        "to",
        "manage",
        "their",
        "time",
        "independently"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Samarqandga tashrif buyurgan sayyohlar shaharning tarixiy binolaridan hayratda qolishadi.",
      "target_text": "Tourists who visit Samarkand are impressed by its historic buildings.",
      "words": [
        "Tourists",
        "who",
        "visit",
        "Samarkand",
        "are",
        "impressed",
        "by",
        "its",
        "historic",
        "buildings"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Qayta tiklanadigan energiya manbalari tobora ko'proq mamlakatlarda qo'llanilmoqda.",
      "target_text": "Renewable energy sources are being used in more and more countries.",
      "words": [
        "Renewable",
        "energy",
        "sources",
        "are",
        "being",
        "used",
        "in",
        "more",
        "and",
        "more",
        "countries"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Men yangi loyiha boshlashdan oldin uning asosiy maqsadlarini aniqlab oldim.",
      "target_text": "I identified the main goals of the project before starting it.",
      "words": [
        "I",
        "identified",
        "the",
        "main",
        "goals",
        "of",
        "the",
        "project",
        "before",
        "starting",
        "it"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U ishga qabul qilinishidan oldin bir nechta texnik savollarga javob berdi.",
      "target_text": "She answered several technical questions before she was hired.",
      "words": [
        "She",
        "answered",
        "several",
        "technical",
        "questions",
        "before",
        "she",
        "was",
        "hired"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Olimlar iqlim o'zgarishi o'simliklarning o'sishiga qanday ta'sir qilishini o'rganmoqda.",
      "target_text": "Scientists are studying how climate change affects plant growth.",
      "words": [
        "Scientists",
        "are",
        "studying",
        "how",
        "climate",
        "change",
        "affects",
        "plant",
        "growth"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Menimcha, yaxshi natijaga erishish uchun muntazam mashq qilish kerak.",
      "target_text": "I think regular practice is necessary to achieve a good result.",
      "words": [
        "I",
        "think",
        "regular",
        "practice",
        "is",
        "necessary",
        "to",
        "achieve",
        "a",
        "good",
        "result"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Agar internet tezligi yaxshilansa, onlayn darslar ancha qulay bo'ladi.",
      "target_text": "If the internet speed improves, online lessons will be much more convenient.",
      "words": [
        "If",
        "the",
        "internet",
        "speed",
        "improves",
        "online",
        "lessons",
        "will",
        "be",
        "much",
        "more",
        "convenient"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "U yangi dasturga ko'nikishi uchun bir necha kun kerak bo'ldi.",
      "target_text": "It took him several days to get used to the new software.",
      "words": [
        "It",
        "took",
        "him",
        "several",
        "days",
        "to",
        "get",
        "used",
        "to",
        "the",
        "new",
        "software"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Biz loyiha haqida gaplashayotganimizda menejer muhim taklif berdi.",
      "target_text": "The manager made an important suggestion while we were discussing the project.",
      "words": [
        "The",
        "manager",
        "made",
        "an",
        "important",
        "suggestion",
        "while",
        "we",
        "were",
        "discussing",
        "the",
        "project"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ko'plab yoshlar tajriba orttirish uchun universitet vaqtida amaliyot o'tashadi.",
      "target_text": "Many young people do internships while at university to gain experience.",
      "words": [
        "Many",
        "young",
        "people",
        "do",
        "internships",
        "while",
        "at",
        "university",
        "to",
        "gain",
        "experience"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men avvalgi xatolarimdan saboq olib, ish uslubimni o'zgartirdim.",
      "target_text": "I learned from my previous mistakes and changed the way I work.",
      "words": [
        "I",
        "learned",
        "from",
        "my",
        "previous",
        "mistakes",
        "and",
        "changed",
        "the",
        "way",
        "I",
        "work"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U sog'lom turmush tarzini boshlaganidan beri o'zini ancha yaxshi his qilmoqda.",
      "target_text": "She has felt much better since she started a healthy lifestyle.",
      "words": [
        "She",
        "has",
        "felt",
        "much",
        "better",
        "since",
        "she",
        "started",
        "a",
        "healthy",
        "lifestyle"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Biz avtobus kechikkanligi sababli uchrashuvga piyoda bordik.",
      "target_text": "We walked to the meeting because the bus was late.",
      "words": [
        "We",
        "walked",
        "to",
        "the",
        "meeting",
        "because",
        "the",
        "bus",
        "was",
        "late"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Yangi velosiped yo'laklari shaharda harakatlanishni xavfsizroq qilishi mumkin.",
      "target_text": "New bicycle lanes could make travelling around the city safer.",
      "words": [
        "New",
        "bicycle",
        "lanes",
        "could",
        "make",
        "travelling",
        "around",
        "the",
        "city",
        "safer"
      ],
      "topic": "City Life"
    },
    {
      "source_text": "Men bu kitobni do'stim tavsiya qilgani uchun o'qidim.",
      "target_text": "I read this book because my friend recommended it.",
      "words": [
        "I",
        "read",
        "this",
        "book",
        "because",
        "my",
        "friend",
        "recommended",
        "it"
      ],
      "topic": "Hobbies"
    },
    {
      "source_text": "Ular musobaqaga tayyorlanish uchun bir necha oy davomida mashq qilishdi.",
      "target_text": "They trained for several months to prepare for the competition.",
      "words": [
        "They",
        "trained",
        "for",
        "several",
        "months",
        "to",
        "prepare",
        "for",
        "the",
        "competition"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Tadqiqot natijalari suvning harorati hosilga ta'sir qilishini ko'rsatdi.",
      "target_text": "The research results showed that water temperature affects crops.",
      "words": [
        "The",
        "research",
        "results",
        "showed",
        "that",
        "water",
        "temperature",
        "affects",
        "crops"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Agar odamlar chiqindilarni saralasa, atrof-muhitni himoya qilish osonroq bo'ladi.",
      "target_text": "If people sort their waste, it will be easier to protect the environment.",
      "words": [
        "If",
        "people",
        "sort",
        "their",
        "waste",
        "it",
        "will",
        "be",
        "easier",
        "to",
        "protect",
        "the",
        "environment"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Kompaniya mijozlarning fikrlarini o'rganib, xizmatini yaxshiladi.",
      "target_text": "The company improved its service by studying customer feedback.",
      "words": [
        "The",
        "company",
        "improved",
        "its",
        "service",
        "by",
        "studying",
        "customer",
        "feedback"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men uchrashuvdan oldin barcha hujjatlarni tayyorlab qo'ygan edim.",
      "target_text": "I had prepared all the documents before the meeting.",
      "words": [
        "I",
        "had",
        "prepared",
        "all",
        "the",
        "documents",
        "before",
        "the",
        "meeting"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U menga yangi vazifani qanday bajarishni tushuntirib berdi.",
      "target_text": "He explained to me how to complete the new task.",
      "words": [
        "He",
        "explained",
        "to",
        "me",
        "how",
        "to",
        "complete",
        "the",
        "new",
        "task"
      ],
      "topic": "Education"
    },
    {
      "source_text": "O'qituvchi darsni tugatgach, talabalar savollar berishdi.",
      "target_text": "The students asked questions after the teacher finished the lesson.",
      "words": [
        "The",
        "students",
        "asked",
        "questions",
        "after",
        "the",
        "teacher",
        "finished",
        "the",
        "lesson"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Telefon ilovalari kundalik vazifalarni rejalashtirishni osonlashtirishi mumkin.",
      "target_text": "Phone applications can make it easier to plan daily tasks.",
      "words": [
        "Phone",
        "applications",
        "can",
        "make",
        "it",
        "easier",
        "to",
        "plan",
        "daily",
        "tasks"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Men internetdan foydalanganda shaxsiy ma'lumotlarimni himoya qilishga harakat qilaman.",
      "target_text": "I try to protect my personal information when I use the internet.",
      "words": [
        "I",
        "try",
        "to",
        "protect",
        "my",
        "personal",
        "information",
        "when",
        "I",
        "use",
        "the",
        "internet"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ular yangi mahsulotni bozorga chiqarishdan oldin uni sinab ko'rishdi.",
      "target_text": "They tested the new product before launching it on the market.",
      "words": [
        "They",
        "tested",
        "the",
        "new",
        "product",
        "before",
        "launching",
        "it",
        "on",
        "the",
        "market"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Agar ob-havo yaxshi bo'lsa, biz sayohatimizni bir kunga uzaytiramiz.",
      "target_text": "If the weather is good, we will extend our trip by one day.",
      "words": [
        "If",
        "the",
        "weather",
        "is",
        "good",
        "we",
        "will",
        "extend",
        "our",
        "trip",
        "by",
        "one",
        "day"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Buxoroning eski shahri o'zining tor ko'chalari va tarixiy binolari bilan mashhur.",
      "target_text": "The old city of Bukhara is famous for its narrow streets and historic buildings.",
      "words": [
        "The",
        "old",
        "city",
        "of",
        "Bukhara",
        "is",
        "famous",
        "for",
        "its",
        "narrow",
        "streets",
        "and",
        "historic",
        "buildings"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Men ingliz tilida gapirishni yaxshilash uchun har kuni qisqa suhbatlar qilaman.",
      "target_text": "I have short conversations every day to improve my spoken English.",
      "words": [
        "I",
        "have",
        "short",
        "conversations",
        "every",
        "day",
        "to",
        "improve",
        "my",
        "spoken",
        "English"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U kecha juda charchagan bo'lsa ham, loyihani tugatdi.",
      "target_text": "Although he was very tired yesterday, he finished the project.",
      "words": [
        "Although",
        "he",
        "was",
        "very",
        "tired",
        "yesterday",
        "he",
        "finished",
        "the",
        "project"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Yangi tizim ishchilarga ma'lumotni tezroq topishga yordam beradi.",
      "target_text": "The new system helps employees find information more quickly.",
      "words": [
        "The",
        "new",
        "system",
        "helps",
        "employees",
        "find",
        "information",
        "more",
        "quickly"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Olimlar tajribani bir necha marta takrorlab, natijalarni solishtirishdi.",
      "target_text": "The scientists repeated the experiment several times and compared the results.",
      "words": [
        "The",
        "scientists",
        "repeated",
        "the",
        "experiment",
        "several",
        "times",
        "and",
        "compared",
        "the",
        "results"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Men kelajakda ma'lumotlar tahlili bilan bog'liq sohada ishlashni rejalashtiryapman.",
      "target_text": "I am planning to work in a field related to data analysis in the future.",
      "words": [
        "I",
        "am",
        "planning",
        "to",
        "work",
        "in",
        "a",
        "field",
        "related",
        "to",
        "data",
        "analysis",
        "in",
        "the",
        "future"
      ],
      "topic": "Career"
    },
    {
      "source_text": "Uning jamoasi muhim o'yinda mag'lub bo'lgach, ko'proq mashq qila boshladi.",
      "target_text": "After his team lost an important match, they started training harder.",
      "words": [
        "After",
        "his",
        "team",
        "lost",
        "an",
        "important",
        "match",
        "they",
        "started",
        "training",
        "harder"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Shifokor unga ko'proq suv ichishni va muntazam yurishni tavsiya qildi.",
      "target_text": "The doctor advised him to drink more water and walk regularly.",
      "words": [
        "The",
        "doctor",
        "advised",
        "him",
        "to",
        "drink",
        "more",
        "water",
        "and",
        "walk",
        "regularly"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Biz yangi restoran ochilgandan beri u yerga bir necha marta bordik.",
      "target_text": "We have visited the new restaurant several times since it opened.",
      "words": [
        "We",
        "have",
        "visited",
        "the",
        "new",
        "restaurant",
        "several",
        "times",
        "since",
        "it",
        "opened"
      ],
      "topic": "Food"
    },
    {
      "source_text": "Agar men vazifani vaqtida tugatsam, kechqurun do'stlarim bilan uchrashaman.",
      "target_text": "If I finish my work on time, I will meet my friends in the evening.",
      "words": [
        "If",
        "I",
        "finish",
        "my",
        "work",
        "on",
        "time",
        "I",
        "will",
        "meet",
        "my",
        "friends",
        "in",
        "the",
        "evening"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "U yangi ishga o'tgandan keyin har kuni ertaroq turadigan bo'ldi.",
      "target_text": "After changing jobs, she started getting up earlier every day.",
      "words": [
        "After",
        "changing",
        "jobs",
        "she",
        "started",
        "getting",
        "up",
        "earlier",
        "every",
        "day"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Internet orqali bilim olish avvalgiga qaraganda ancha osonlashdi.",
      "target_text": "Learning through the internet has become much easier than before.",
      "words": [
        "Learning",
        "through",
        "the",
        "internet",
        "has",
        "become",
        "much",
        "easier",
        "than",
        "before"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Mahalliy fermerlar suvni tejash uchun tomchilatib sug'orishdan foydalanmoqda.",
      "target_text": "Local farmers are using drip irrigation to save water.",
      "words": [
        "Local",
        "farmers",
        "are",
        "using",
        "drip",
        "irrigation",
        "to",
        "save",
        "water"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Men bu masalani yolg'iz hal qila olmaganim uchun yordam so'radim.",
      "target_text": "I asked for help because I could not solve the problem alone.",
      "words": [
        "I",
        "asked",
        "for",
        "help",
        "because",
        "I",
        "could",
        "not",
        "solve",
        "the",
        "problem",
        "alone"
      ],
      "topic": "Daily Life"
    },
    {
      "source_text": "Uning taqdimoti juda aniq bo'lgani uchun hamma mavzuni tushundi.",
      "target_text": "Everyone understood the topic because her presentation was very clear.",
      "words": [
        "Everyone",
        "understood",
        "the",
        "topic",
        "because",
        "her",
        "presentation",
        "was",
        "very",
        "clear"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Kompaniya xodimlari yangi xavfsizlik qoidalariga rioya qilishlari kerak.",
      "target_text": "Company employees have to follow the new safety rules.",
      "words": [
        "Company",
        "employees",
        "have",
        "to",
        "follow",
        "the",
        "new",
        "safety",
        "rules"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ushbu qurilma energiyani tejash uchun avtomatik ravishda o'chadi.",
      "target_text": "This device turns off automatically to save energy.",
      "words": [
        "This",
        "device",
        "turns",
        "off",
        "automatically",
        "to",
        "save",
        "energy"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Men sayohat qilishdan oldin mahalliy transport haqida ma'lumot izladim.",
      "target_text": "I looked for information about local transport before travelling.",
      "words": [
        "I",
        "looked",
        "for",
        "information",
        "about",
        "local",
        "transport",
        "before",
        "travelling"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "O'qituvchi o'quvchilarga topshiriqni bajarish uchun ikki kun berdi.",
      "target_text": "The teacher gave the students two days to complete the assignment.",
      "words": [
        "The",
        "teacher",
        "gave",
        "the",
        "students",
        "two",
        "days",
        "to",
        "complete",
        "the",
        "assignment"
      ],
      "topic": "School"
    },
    {
      "source_text": "Ular qarorni qabul qilishdan oldin barcha variantlarni muhokama qilishdi.",
      "target_text": "They discussed all the options before making a decision.",
      "words": [
        "They",
        "discussed",
        "all",
        "the",
        "options",
        "before",
        "making",
        "a",
        "decision"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi tadqiqot sun'iy intellektdan ta'limda foydalanish imkoniyatlarini ko'rsatmoqda.",
      "target_text": "A new study is showing the possibilities of using artificial intelligence in education.",
      "words": [
        "A",
        "new",
        "study",
        "is",
        "showing",
        "the",
        "possibilities",
        "of",
        "using",
        "artificial",
        "intelligence",
        "in",
        "education"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Men dasturlashni o'rganganimdan beri texnologiyaga qiziqishim oshdi.",
      "target_text": "My interest in technology has increased since I started learning programming.",
      "words": [
        "My",
        "interest",
        "in",
        "technology",
        "has",
        "increased",
        "since",
        "I",
        "started",
        "learning",
        "programming"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Agar odamlar ko'proq daraxt eksa, shaharlardagi havo yaxshilanishi mumkin.",
      "target_text": "If people plant more trees, the air in cities may improve.",
      "words": [
        "If",
        "people",
        "plant",
        "more",
        "trees",
        "the",
        "air",
        "in",
        "cities",
        "may",
        "improve"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Ular o'tgan yili kichik biznes boshlashgan va hozir uni kengaytirmoqda.",
      "target_text": "They started a small business last year and are now expanding it.",
      "words": [
        "They",
        "started",
        "a",
        "small",
        "business",
        "last",
        "year",
        "and",
        "are",
        "now",
        "expanding",
        "it"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men ishdagi bosimni kamaytirish uchun vazifalarimni ustuvorlik bo'yicha ajrataman.",
      "target_text": "I prioritize my tasks to reduce pressure at work.",
      "words": [
        "I",
        "prioritize",
        "my",
        "tasks",
        "to",
        "reduce",
        "pressure",
        "at",
        "work"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Uning yangi kompyuteri avvalgisidan ancha tez ishlaydi.",
      "target_text": "Her new computer works much faster than the previous one.",
      "words": [
        "Her",
        "new",
        "computer",
        "works",
        "much",
        "faster",
        "than",
        "the",
        "previous",
        "one"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Biz mehmonxonaga kelganimizda, xodimlar xonamizni tayyorlab qo'yishgan edi.",
      "target_text": "When we arrived at the hotel, the staff had prepared our room.",
      "words": [
        "When",
        "we",
        "arrived",
        "at",
        "the",
        "hotel",
        "the",
        "staff",
        "had",
        "prepared",
        "our",
        "room"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Menimcha, sport bilan shug'ullanish odamning kayfiyatini yaxshilaydi.",
      "target_text": "I think doing sport improves a person's mood.",
      "words": [
        "I",
        "think",
        "doing",
        "sport",
        "improves",
        "a",
        "person's",
        "mood"
      ],
      "topic": "Health"
    },
    {
      "source_text": "U inglizcha maqolalarni o'qish orqali yangi so'zlarni o'rgandi.",
      "target_text": "He learned new words by reading English articles.",
      "words": [
        "He",
        "learned",
        "new",
        "words",
        "by",
        "reading",
        "English",
        "articles"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Tadqiqotchilar ma'lumotlarni yig'ib bo'lgach, ularni tahlil qilishdi.",
      "target_text": "The researchers analyzed the data after collecting it.",
      "words": [
        "The",
        "researchers",
        "analyzed",
        "the",
        "data",
        "after",
        "collecting",
        "it"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Bu xizmat foydalanuvchilarga muammolarini onlayn hal qilish imkonini beradi.",
      "target_text": "This service allows users to solve their problems online.",
      "words": [
        "This",
        "service",
        "allows",
        "users",
        "to",
        "solve",
        "their",
        "problems",
        "online"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Agar loyiha o'z vaqtida tugasa, kompaniya yangi mijozlarni qabul qiladi.",
      "target_text": "If the project is completed on time, the company will accept new clients.",
      "words": [
        "If",
        "the",
        "project",
        "is",
        "completed",
        "on",
        "time",
        "the",
        "company",
        "will",
        "accept",
        "new",
        "clients"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men yangi shaharni yaxshiroq bilish uchun mahalliy bozorni aylanib chiqdim.",
      "target_text": "I explored the local market to get to know the new city better.",
      "words": [
        "I",
        "explored",
        "the",
        "local",
        "market",
        "to",
        "get",
        "to",
        "know",
        "the",
        "new",
        "city",
        "better"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "Ular yangi sport markazida mashq qilishni boshlaganidan beri kuchliroq bo'lishdi.",
      "target_text": "They have become stronger since they started training at the new sports center.",
      "words": [
        "They",
        "have",
        "become",
        "stronger",
        "since",
        "they",
        "started",
        "training",
        "at",
        "the",
        "new",
        "sports",
        "center"
      ],
      "topic": "Sports"
    },
    {
      "source_text": "Maktabda guruh bo'lib ishlash o'quvchilarga bir-biridan o'rganishga yordam beradi.",
      "target_text": "Working in groups at school helps students learn from each other.",
      "words": [
        "Working",
        "in",
        "groups",
        "at",
        "school",
        "helps",
        "students",
        "learn",
        "from",
        "each",
        "other"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men telefonimni yangilaganimdan keyin ayrim eski ilovalar ishlamay qoldi.",
      "target_text": "After I updated my phone, some old applications stopped working.",
      "words": [
        "After",
        "I",
        "updated",
        "my",
        "phone",
        "some",
        "old",
        "applications",
        "stopped",
        "working"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Olimlar yangi dori usulini tasdiqlashdan oldin ko'proq dalil to'plashlari kerak.",
      "target_text": "Scientists need to collect more evidence before approving the new treatment.",
      "words": [
        "Scientists",
        "need",
        "to",
        "collect",
        "more",
        "evidence",
        "before",
        "approving",
        "the",
        "new",
        "treatment"
      ],
      "topic": "Science"
    },
    {
      "source_text": "U muammo haqida rahbariga aytishdan oldin bir nechta yechim topdi.",
      "target_text": "She found several solutions before telling her manager about the problem.",
      "words": [
        "She",
        "found",
        "several",
        "solutions",
        "before",
        "telling",
        "her",
        "manager",
        "about",
        "the",
        "problem"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Shaharda jamoat transporti yaxshilangani sababli odamlar mashinadan kamroq foydalanmoqda.",
      "target_text": "People are using cars less because public transport has improved in the city.",
      "words": [
        "People",
        "are",
        "using",
        "cars",
        "less",
        "because",
        "public",
        "transport",
        "has",
        "improved",
        "in",
        "the",
        "city"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Men bu kursni tugatganimdan keyin kichik loyiha yaratishni xohlayman.",
      "target_text": "I want to create a small project after I finish this course.",
      "words": [
        "I",
        "want",
        "to",
        "create",
        "a",
        "small",
        "project",
        "after",
        "I",
        "finish",
        "this",
        "course"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular tabiatni asrash bo'yicha mahalliy tadbirda ko'ngilli bo'lib ishlashdi.",
      "target_text": "They volunteered at a local event to protect nature.",
      "words": [
        "They",
        "volunteered",
        "at",
        "a",
        "local",
        "event",
        "to",
        "protect",
        "nature"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Kompaniya mijozlarga tezroq javob berish uchun yangi xizmat joriy qildi.",
      "target_text": "The company introduced a new service to respond to customers more quickly.",
      "words": [
        "The",
        "company",
        "introduced",
        "a",
        "new",
        "service",
        "to",
        "respond",
        "to",
        "customers",
        "more",
        "quickly"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men kecha o'qigan maqolamda qiziqarli statistik ma'lumotlarni topdim.",
      "target_text": "I found interesting statistics in the article I read yesterday.",
      "words": [
        "I",
        "found",
        "interesting",
        "statistics",
        "in",
        "the",
        "article",
        "I",
        "read",
        "yesterday"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Agar sen har kuni mashq qilsang, talaffuzing asta-sekin yaxshilanadi.",
      "target_text": "If you practice every day, your pronunciation will gradually improve.",
      "words": [
        "If",
        "you",
        "practice",
        "every",
        "day",
        "your",
        "pronunciation",
        "will",
        "gradually",
        "improve"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Uning fikricha, texnologiya odamlarning ish uslubini o'zgartirishda davom etadi.",
      "target_text": "In his opinion, technology will continue to change the way people work.",
      "words": [
        "In",
        "his",
        "opinion",
        "technology",
        "will",
        "continue",
        "to",
        "change",
        "the",
        "way",
        "people",
        "work"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Biz loyihani tugatgach, natijalarni mijozga taqdim etdik.",
      "target_text": "After we finished the project, we presented the results to the client.",
      "words": [
        "After",
        "we",
        "finished",
        "the",
        "project",
        "we",
        "presented",
        "the",
        "results",
        "to",
        "the",
        "client"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi algoritm ma'lumotlarni avvalgi usulga qaraganda tezroq qayta ishlaydi.",
      "target_text": "The new algorithm processes data faster than the previous method.",
      "words": [
        "The",
        "new",
        "algorithm",
        "processes",
        "data",
        "faster",
        "than",
        "the",
        "previous",
        "method"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Men xatoni topganimdan keyin dastur kodini tekshirib chiqdim.",
      "target_text": "I checked the program code after I found the error.",
      "words": [
        "I",
        "checked",
        "the",
        "program",
        "code",
        "after",
        "I",
        "found",
        "the",
        "error"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ular energiya sarfini kamaytirish uchun binoga yangi tizim o'rnatishdi.",
      "target_text": "They installed a new system in the building to reduce energy use.",
      "words": [
        "They",
        "installed",
        "a",
        "new",
        "system",
        "in",
        "the",
        "building",
        "to",
        "reduce",
        "energy",
        "use"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Sayohat davomida men bir nechta mahalliy taomlarni tatib ko'rdim.",
      "target_text": "During the trip, I tried several local dishes.",
      "words": [
        "During",
        "the",
        "trip",
        "I",
        "tried",
        "several",
        "local",
        "dishes"
      ],
      "topic": "Travel"
    },
    {
      "source_text": "O'qituvchi mavzuni misollar bilan tushuntirgani uchun dars qiziqarli bo'ldi.",
      "target_text": "The lesson was interesting because the teacher explained the topic with examples.",
      "words": [
        "The",
        "lesson",
        "was",
        "interesting",
        "because",
        "the",
        "teacher",
        "explained",
        "the",
        "topic",
        "with",
        "examples"
      ],
      "topic": "Education"
    },
    {
      "source_text": "U yangi ishida turli odamlar bilan muloqot qilishni o'rgandi.",
      "target_text": "She learned to communicate with different people in her new job.",
      "words": [
        "She",
        "learned",
        "to",
        "communicate",
        "with",
        "different",
        "people",
        "in",
        "her",
        "new",
        "job"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Tadqiqot guruhi natijalarni boshqa olimlar bilan baham ko'rdi.",
      "target_text": "The research group shared the results with other scientists.",
      "words": [
        "The",
        "research",
        "group",
        "shared",
        "the",
        "results",
        "with",
        "other",
        "scientists"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Men sog'lom odatlarni asta-sekin shakllantirishga harakat qilyapman.",
      "target_text": "I am trying to develop healthy habits gradually.",
      "words": [
        "I",
        "am",
        "trying",
        "to",
        "develop",
        "healthy",
        "habits",
        "gradually"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Agar kompaniya xizmat sifatini oshirsa, ko'proq mijozlarni jalb qilishi mumkin.",
      "target_text": "If the company improves its service quality, it may attract more customers.",
      "words": [
        "If",
        "the",
        "company",
        "improves",
        "its",
        "service",
        "quality",
        "it",
        "may",
        "attract",
        "more",
        "customers"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ular yangi mahsulotni reklama qilishdan oldin bozorni o'rganishdi.",
      "target_text": "They studied the market before advertising the new product.",
      "words": [
        "They",
        "studied",
        "the",
        "market",
        "before",
        "advertising",
        "the",
        "new",
        "product"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Menimcha, o'quvchilar texnologiyadan to'g'ri foydalanishni ham o'rganishi kerak.",
      "target_text": "I think students should also learn how to use technology properly.",
      "words": [
        "I",
        "think",
        "students",
        "should",
        "also",
        "learn",
        "how",
        "to",
        "use",
        "technology",
        "properly"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Yangi sensorlar fermerlarga ekinlarning holatini kuzatishda yordam beradi.",
      "target_text": "New sensors help farmers monitor the condition of their crops.",
      "words": [
        "New",
        "sensors",
        "help",
        "farmers",
        "monitor",
        "the",
        "condition",
        "of",
        "their",
        "crops"
      ],
      "topic": "Science"
    },
    {
      "source_text": "U kecha uchrashuvga kechikkan bo'lsa-da, muhim fikr bildirdi.",
      "target_text": "Although he was late for the meeting yesterday, he made an important point.",
      "words": [
        "Although",
        "he",
        "was",
        "late",
        "for",
        "the",
        "meeting",
        "yesterday",
        "he",
        "made",
        "an",
        "important",
        "point"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Bizning jamoamiz muammoni birgalikda muhokama qilib, yaxshi yechim topdi.",
      "target_text": "Our team discussed the problem together and found a good solution.",
      "words": [
        "Our",
        "team",
        "discussed",
        "the",
        "problem",
        "together",
        "and",
        "found",
        "a",
        "good",
        "solution"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Sun'iy intellektga asoslangan vositalar takroriy vazifalarni avtomatlashtirishi mumkin.",
      "target_text": "Artificial intelligence tools can automate repetitive tasks.",
      "words": [
        "Artificial",
        "intelligence",
        "tools",
        "can",
        "automate",
        "repetitive",
        "tasks"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Men yangi ko'nikmalarni rivojlantirish uchun qo'shimcha kurslarga qatnashyapman.",
      "target_text": "I am taking extra courses to develop new skills.",
      "words": [
        "I",
        "am",
        "taking",
        "extra",
        "courses",
        "to",
        "develop",
        "new",
        "skills"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ular suv tanqisligi muammosini hal qilishning yangi yo'llarini izlamoqda.",
      "target_text": "They are looking for new ways to solve the problem of water scarcity.",
      "words": [
        "They",
        "are",
        "looking",
        "for",
        "new",
        "ways",
        "to",
        "solve",
        "the",
        "problem",
        "of",
        "water",
        "scarcity"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Agar transport tizimi yaxshilansa, shahardagi tirbandlik kamayishi mumkin.",
      "target_text": "If the transport system improves, traffic congestion in the city may decrease.",
      "words": [
        "If",
        "the",
        "transport",
        "system",
        "improves",
        "traffic",
        "congestion",
        "in",
        "the",
        "city",
        "may",
        "decrease"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Men loyihaning birinchi bosqichini muvaffaqiyatli yakunlaganimizdan mamnunman.",
      "target_text": "I am pleased that we successfully completed the first stage of the project.",
      "words": [
        "I",
        "am",
        "pleased",
        "that",
        "we",
        "successfully",
        "completed",
        "the",
        "first",
        "stage",
        "of",
        "the",
        "project"
      ],
      "topic": "Work"
    },
    {
      "source_text": "U o'z fikrini aniq tushuntira olgani uchun suhbat yaxshi o'tdi.",
      "target_text": "The conversation went well because she could explain her ideas clearly.",
      "words": [
        "The",
        "conversation",
        "went",
        "well",
        "because",
        "she",
        "could",
        "explain",
        "her",
        "ideas",
        "clearly"
      ],
      "topic": "Communication"
    },
    {
      "source_text": "Olimlar yangi ma'lumotlar mavjud nazariyani qo'llab-quvvatlashini aniqlashdi.",
      "target_text": "Scientists found that the new data supports the existing theory.",
      "words": [
        "Scientists",
        "found",
        "that",
        "the",
        "new",
        "data",
        "supports",
        "the",
        "existing",
        "theory"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya xodimlarga yangi tizimdan foydalanishni o'rgatish uchun seminar o'tkazdi.",
      "target_text": "The company held a workshop to teach employees how to use the new system.",
      "words": [
        "The",
        "company",
        "held",
        "a",
        "workshop",
        "to",
        "teach",
        "employees",
        "how",
        "to",
        "use",
        "the",
        "new",
        "system"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men vaqtimni to'g'ri taqsimlasam, o'qish va dam olishga yetarli vaqt topaman.",
      "target_text": "If I manage my time well, I can find enough time for study and rest.",
      "words": [
        "If",
        "I",
        "manage",
        "my",
        "time",
        "well",
        "I",
        "can",
        "find",
        "enough",
        "time",
        "for",
        "study",
        "and",
        "rest"
      ],
      "topic": "Daily Life"
    }
  ],
  "B2": [
    {
      "source_text": "Sun'iy intellekt modellari tibbiy tasvirlarni tahlil qilib, ayrim kasalliklarni erta aniqlashga yordam bermoqda.",
      "target_text": "Artificial intelligence models are analyzing medical images and helping doctors detect some diseases earlier.",
      "words": [
        "Artificial",
        "intelligence",
        "models",
        "are",
        "analyzing",
        "medical",
        "images",
        "and",
        "helping",
        "doctors",
        "detect",
        "some",
        "diseases",
        "earlier"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Kvant hisoblashning rivojlanishi an'anaviy kompyuterlar uchun juda murakkab bo'lgan masalalarni hal qilish imkonini berishi mumkin.",
      "target_text": "The development of quantum computing could make it possible to solve problems that are too complex for conventional computers.",
      "words": [
        "The",
        "development",
        "of",
        "quantum",
        "computing",
        "could",
        "make",
        "it",
        "possible",
        "to",
        "solve",
        "problems",
        "that",
        "are",
        "too",
        "complex",
        "for",
        "conventional",
        "computers"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Generativ AI ijodiy ishlarni tezlashtirayotgan bo'lsa-da, uning natijalarini inson tomonidan tekshirish hali ham muhim.",
      "target_text": "Although generative AI is accelerating creative work, its output still needs to be reviewed by humans.",
      "words": [
        "Although",
        "generative",
        "AI",
        "is",
        "accelerating",
        "creative",
        "work",
        "its",
        "output",
        "still",
        "needs",
        "to",
        "be",
        "reviewed",
        "by",
        "humans"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Katta ma'lumotlar to'g'ri boshqarilmasa, tashkilotlar undan kutilgan foydani ololmasligi mumkin.",
      "target_text": "If big data is not managed properly, organizations may fail to gain the expected benefits from it.",
      "words": [
        "If",
        "big",
        "data",
        "is",
        "not",
        "managed",
        "properly",
        "organizations",
        "may",
        "fail",
        "to",
        "gain",
        "the",
        "expected",
        "benefits",
        "from",
        "it"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Yangi algoritm oldingi usulga qaraganda aniqroq natijalar bergani sababli tadqiqotchilar undan foydalanishga qaror qilishdi.",
      "target_text": "Because the new algorithm produced more accurate results than the previous method, the researchers decided to use it.",
      "words": [
        "Because",
        "the",
        "new",
        "algorithm",
        "produced",
        "more",
        "accurate",
        "results",
        "than",
        "the",
        "previous",
        "method",
        "the",
        "researchers",
        "decided",
        "to",
        "use",
        "it"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya mahsulotini xalqaro bozorga chiqarishdan oldin mahalliy talabni batafsil o'rgandi.",
      "target_text": "The company studied local demand in detail before launching its product on the international market.",
      "words": [
        "The",
        "company",
        "studied",
        "local",
        "demand",
        "in",
        "detail",
        "before",
        "launching",
        "its",
        "product",
        "on",
        "the",
        "international",
        "market"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Iqlim o'zgarishining ta'siri kuchayib borayotganligi sababli suv resurslarini samarali boshqarish zarur.",
      "target_text": "As the effects of climate change become more severe, water resources need to be managed efficiently.",
      "words": [
        "As",
        "the",
        "effects",
        "of",
        "climate",
        "change",
        "become",
        "more",
        "severe",
        "water",
        "resources",
        "need",
        "to",
        "be",
        "managed",
        "efficiently"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Masofaviy ishlash ommalashgan bo'lsa ham, ayrim jamoalar yuzma-yuz uchrashuvlarni samaraliroq deb hisoblaydi.",
      "target_text": "Although remote work has become popular, some teams consider face-to-face meetings more effective.",
      "words": [
        "Although",
        "remote",
        "work",
        "has",
        "become",
        "popular",
        "some",
        "teams",
        "consider",
        "face-to-face",
        "meetings",
        "more",
        "effective"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Tadqiqot natijalari shuni ko'rsatadiki, muntazam jismoniy faoliyat diqqatni jamlash qobiliyatiga ijobiy ta'sir qiladi.",
      "target_text": "The research findings suggest that regular physical activity has a positive effect on concentration.",
      "words": [
        "The",
        "research",
        "findings",
        "suggest",
        "that",
        "regular",
        "physical",
        "activity",
        "has",
        "a",
        "positive",
        "effect",
        "on",
        "concentration"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Agar ma'lumotlar sifatsiz bo'lsa, hatto eng murakkab model ham ishonchli bashorat bera olmaydi.",
      "target_text": "Even the most sophisticated model cannot make reliable predictions if the data is poor.",
      "words": [
        "Even",
        "the",
        "most",
        "sophisticated",
        "model",
        "cannot",
        "make",
        "reliable",
        "predictions",
        "if",
        "the",
        "data",
        "is",
        "poor"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Kiberxavfsizlikka sarmoya kiritish kompaniya uchun qo'shimcha xarajat bo'lib ko'rinishi mumkin, ammo u katta xavflarni kamaytiradi.",
      "target_text": "Investing in cybersecurity may seem like an additional cost, but it reduces significant risks for a company.",
      "words": [
        "Investing",
        "in",
        "cybersecurity",
        "may",
        "seem",
        "like",
        "an",
        "additional",
        "cost",
        "but",
        "it",
        "reduces",
        "significant",
        "risks",
        "for",
        "a",
        "company"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Olimlar tajriba natijalarini tasdiqlash uchun ma'lumotlarni mustaqil guruh yordamida qayta tekshirishdi.",
      "target_text": "Scientists rechecked the data with an independent group to confirm the experimental results.",
      "words": [
        "Scientists",
        "rechecked",
        "the",
        "data",
        "with",
        "an",
        "independent",
        "group",
        "to",
        "confirm",
        "the",
        "experimental",
        "results"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Yangi biznes modeli mijozlarning ehtiyojlari o'zgarganidan keyin ishlab chiqildi.",
      "target_text": "The new business model was developed after customer needs had changed.",
      "words": [
        "The",
        "new",
        "business",
        "model",
        "was",
        "developed",
        "after",
        "customer",
        "needs",
        "had",
        "changed"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Shahar jamoat transportini yaxshilagan sari odamlarning shaxsiy avtomobillarga bo'lgan ehtiyoji kamayishi mumkin.",
      "target_text": "As a city improves public transport, people's dependence on private cars may decrease.",
      "words": [
        "As",
        "a",
        "city",
        "improves",
        "public",
        "transport",
        "people's",
        "dependence",
        "on",
        "private",
        "cars",
        "may",
        "decrease"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Men loyihaning dastlabki natijalarini ko'rib chiqib, keyingi bosqich uchun bir nechta o'zgarishlarni taklif qildim.",
      "target_text": "After reviewing the project's initial results, I suggested several changes for the next stage.",
      "words": [
        "After",
        "reviewing",
        "the",
        "project's",
        "initial",
        "results",
        "I",
        "suggested",
        "several",
        "changes",
        "for",
        "the",
        "next",
        "stage"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Sun'iy intellektning tez rivojlanishi ta'lim tizimlaridan o'qitish usullarini qayta ko'rib chiqishni talab qilmoqda.",
      "target_text": "The rapid development of artificial intelligence is forcing education systems to reconsider teaching methods.",
      "words": [
        "The",
        "rapid",
        "development",
        "of",
        "artificial",
        "intelligence",
        "is",
        "forcing",
        "education",
        "systems",
        "to",
        "reconsider",
        "teaching",
        "methods"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ushbu texnologiya keng qo'llanilishidan oldin uning uzoq muddatli xavfsizligi chuqur baholanishi kerak.",
      "target_text": "The long-term safety of this technology should be assessed carefully before it is widely adopted.",
      "words": [
        "The",
        "long-term",
        "safety",
        "of",
        "this",
        "technology",
        "should",
        "be",
        "assessed",
        "carefully",
        "before",
        "it",
        "is",
        "widely",
        "adopted"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Energiya narxlari oshgani sayin, qayta tiklanadigan manbalarga bo'lgan qiziqish ham ortib bormoqda.",
      "target_text": "As energy prices rise, interest in renewable sources is also increasing.",
      "words": [
        "As",
        "energy",
        "prices",
        "rise",
        "interest",
        "in",
        "renewable",
        "sources",
        "is",
        "also",
        "increasing"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Tahlilchilar kompaniyaning daromadi oshganiga qaramay, xarajatlar ham tez sur'atda ko'payganini ta'kidlashdi.",
      "target_text": "Analysts noted that although the company's revenue had increased, its costs had also risen rapidly.",
      "words": [
        "Analysts",
        "noted",
        "that",
        "although",
        "the",
        "company's",
        "revenue",
        "had",
        "increased",
        "its",
        "costs",
        "had",
        "also",
        "risen",
        "rapidly"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men ma'lumotlar to'plamini tozalaganimdan keyin modelning aniqligi sezilarli darajada oshdi.",
      "target_text": "After I cleaned the dataset, the model's accuracy increased significantly.",
      "words": [
        "After",
        "I",
        "cleaned",
        "the",
        "dataset",
        "the",
        "model's",
        "accuracy",
        "increased",
        "significantly"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Agar hukumat raqamli infratuzilmaga yetarli mablag' ajratsa, kichik bizneslar ham yangi bozorlarga chiqishi mumkin.",
      "target_text": "If the government invests enough in digital infrastructure, small businesses may also reach new markets.",
      "words": [
        "If",
        "the",
        "government",
        "invests",
        "enough",
        "in",
        "digital",
        "infrastructure",
        "small",
        "businesses",
        "may",
        "also",
        "reach",
        "new",
        "markets"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi sensorlar ekinlarning holatini doimiy kuzatish imkonini berib, fermerlarning qarorlarini yaxshilaydi.",
      "target_text": "New sensors allow crops to be monitored continuously, improving farmers' decisions.",
      "words": [
        "New",
        "sensors",
        "allow",
        "crops",
        "to",
        "be",
        "monitored",
        "continuously",
        "improving",
        "farmers",
        "decisions"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Tadqiqotchilar iqlim ma'lumotlarini sun'iy yo'ldosh tasvirlari bilan birlashtirib, hosildorlikni aniqroq baholashdi.",
      "target_text": "Researchers combined climate data with satellite imagery to estimate crop yields more accurately.",
      "words": [
        "Researchers",
        "combined",
        "climate",
        "data",
        "with",
        "satellite",
        "imagery",
        "to",
        "estimate",
        "crop",
        "yields",
        "more",
        "accurately"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Texnologiya qanchalik tez rivojlanmasin, insonning tanqidiy fikrlashi uning natijalarini baholashda muhim bo'lib qoladi.",
      "target_text": "No matter how quickly technology develops, human critical thinking remains important for evaluating its results.",
      "words": [
        "No",
        "matter",
        "how",
        "quickly",
        "technology",
        "develops",
        "human",
        "critical",
        "thinking",
        "remains",
        "important",
        "for",
        "evaluating",
        "its",
        "results"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Kompaniya yangi xizmatni joriy etishdan avval mijozlarning fikrlarini bir necha oy davomida yig'di.",
      "target_text": "The company collected customer feedback for several months before introducing the new service.",
      "words": [
        "The",
        "company",
        "collected",
        "customer",
        "feedback",
        "for",
        "several",
        "months",
        "before",
        "introducing",
        "the",
        "new",
        "service"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Raqamli ta'lim vositalari to'g'ri ishlatilsa, talabalar o'zlashtirish tezligini o'z ehtiyojlariga moslashtira oladi.",
      "target_text": "When used properly, digital learning tools allow students to adapt their learning pace to their needs.",
      "words": [
        "When",
        "used",
        "properly",
        "digital",
        "learning",
        "tools",
        "allow",
        "students",
        "to",
        "adapt",
        "their",
        "learning",
        "pace",
        "to",
        "their",
        "needs"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Tadqiqot guruhi dastlabki gipoteza kutilgan natijani bermaganidan keyin yangi yondashuvni ishlab chiqdi.",
      "target_text": "The research team developed a new approach after the initial hypothesis failed to produce the expected result.",
      "words": [
        "The",
        "research",
        "team",
        "developed",
        "a",
        "new",
        "approach",
        "after",
        "the",
        "initial",
        "hypothesis",
        "failed",
        "to",
        "produce",
        "the",
        "expected",
        "result"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniyalar masofaviy xodimlar bilan samarali ishlashi uchun aniq aloqa qoidalarini belgilashi kerak.",
      "target_text": "Companies need to establish clear communication rules to work effectively with remote employees.",
      "words": [
        "Companies",
        "need",
        "to",
        "establish",
        "clear",
        "communication",
        "rules",
        "to",
        "work",
        "effectively",
        "with",
        "remote",
        "employees"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Qayta tiklanadigan energiya arzonlashgani sari undan foydalanish iqtisodiy jihatdan yanada jozibador bo'lmoqda.",
      "target_text": "As renewable energy becomes cheaper, using it is becoming more economically attractive.",
      "words": [
        "As",
        "renewable",
        "energy",
        "becomes",
        "cheaper",
        "using",
        "it",
        "is",
        "becoming",
        "more",
        "economically",
        "attractive"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "U yangi lavozimni qabul qilishdan oldin ishning uzoq muddatli imkoniyatlarini sinchiklab baholadi.",
      "target_text": "Before accepting the new position, she carefully evaluated its long-term opportunities.",
      "words": [
        "Before",
        "accepting",
        "the",
        "new",
        "position",
        "she",
        "carefully",
        "evaluated",
        "its",
        "long-term",
        "opportunities"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Sun'iy intellekt tizimi xatoni aniqlay olgan bo'lsa-da, uning sababini tushuntirish qiyin bo'ldi.",
      "target_text": "Although the artificial intelligence system detected the error, explaining its cause proved difficult.",
      "words": [
        "Although",
        "the",
        "artificial",
        "intelligence",
        "system",
        "detected",
        "the",
        "error",
        "explaining",
        "its",
        "cause",
        "proved",
        "difficult"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Kvant kompyuterlari amaliyotda keng tarqalishi uchun hali bir qator texnik muammolar hal qilinishi kerak.",
      "target_text": "Several technical problems still need to be solved before quantum computers become widely practical.",
      "words": [
        "Several",
        "technical",
        "problems",
        "still",
        "need",
        "to",
        "be",
        "solved",
        "before",
        "quantum",
        "computers",
        "become",
        "widely",
        "practical"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Bozor talabining o'zgarishi kompaniyani ishlab chiqarish strategiyasini qayta ko'rib chiqishga majbur qildi.",
      "target_text": "Changes in market demand forced the company to reconsider its production strategy.",
      "words": [
        "Changes",
        "in",
        "market",
        "demand",
        "forced",
        "the",
        "company",
        "to",
        "reconsider",
        "its",
        "production",
        "strategy"
      ],
      "topic": "Business"
    },
    {
      "source_text": "O'zbekistonning raqamli iqtisodiyoti rivojlanishi bilan texnologik mutaxassislarga talab ham ortishi kutilmoqda.",
      "target_text": "As Uzbekistan's digital economy develops, demand for technology specialists is also expected to increase.",
      "words": [
        "As",
        "Uzbekistan's",
        "digital",
        "economy",
        "develops",
        "demand",
        "for",
        "technology",
        "specialists",
        "is",
        "also",
        "expected",
        "to",
        "increase"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Samarqand turizmni rivojlantirish bilan birga tarixiy merosini asrab qolishga harakat qilmoqda.",
      "target_text": "Samarkand is trying to develop tourism while preserving its historical heritage.",
      "words": [
        "Samarkand",
        "is",
        "trying",
        "to",
        "develop",
        "tourism",
        "while",
        "preserving",
        "its",
        "historical",
        "heritage"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Agar shaharlar yashil hududlarni ko'paytirsa, yozgi issiqlikning ayrim salbiy ta'sirlari kamayishi mumkin.",
      "target_text": "If cities increase green spaces, some negative effects of summer heat could be reduced.",
      "words": [
        "If",
        "cities",
        "increase",
        "green",
        "spaces",
        "some",
        "negative",
        "effects",
        "of",
        "summer",
        "heat",
        "could",
        "be",
        "reduced"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Ma'lumotlar maxfiyligini ta'minlash uchun kompaniya foydalanuvchi ruxsatisiz shaxsiy ma'lumotlarni ulashmasligi kerak.",
      "target_text": "To protect data privacy, the company should not share personal information without user consent.",
      "words": [
        "To",
        "protect",
        "data",
        "privacy",
        "the",
        "company",
        "should",
        "not",
        "share",
        "personal",
        "information",
        "without",
        "user",
        "consent"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Yangi model avvalgi modeldan yaxshiroq ishlagan bo'lsa ham, uning ishlashi barcha holatlarda barqaror emas edi.",
      "target_text": "Although the new model performed better than the previous one, its performance was not consistent in every case.",
      "words": [
        "Although",
        "the",
        "new",
        "model",
        "performed",
        "better",
        "than",
        "the",
        "previous",
        "one",
        "its",
        "performance",
        "was",
        "not",
        "consistent",
        "in",
        "every",
        "case"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Olimlar yangi material yuqori haroratga chidamli ekanligini aniqlagach, uning sanoatdagi imkoniyatlarini o'rganishdi.",
      "target_text": "After discovering that the new material was resistant to high temperatures, scientists investigated its industrial potential.",
      "words": [
        "After",
        "discovering",
        "that",
        "the",
        "new",
        "material",
        "was",
        "resistant",
        "to",
        "high",
        "temperatures",
        "scientists",
        "investigated",
        "its",
        "industrial",
        "potential"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Men taqdimotimni qisqartirdim, chunki asosiy fikrlarni aniqroq yetkazishni xohlardim.",
      "target_text": "I shortened my presentation because I wanted to communicate the main ideas more clearly.",
      "words": [
        "I",
        "shortened",
        "my",
        "presentation",
        "because",
        "I",
        "wanted",
        "to",
        "communicate",
        "the",
        "main",
        "ideas",
        "more",
        "clearly"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Agar loyiha yetarli moliyalashtirilsa, tadqiqotchilar tajribani kengroq miqyosda o'tkazishi mumkin.",
      "target_text": "If the project receives sufficient funding, the researchers may conduct the experiment on a larger scale.",
      "words": [
        "If",
        "the",
        "project",
        "receives",
        "sufficient",
        "funding",
        "the",
        "researchers",
        "may",
        "conduct",
        "the",
        "experiment",
        "on",
        "a",
        "larger",
        "scale"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Iqtisodiy noaniqlik kuchaygan paytda kompaniyalar yangi xodimlarni yollashda ehtiyotkorroq bo'ladi.",
      "target_text": "When economic uncertainty increases, companies tend to be more cautious about hiring new employees.",
      "words": [
        "When",
        "economic",
        "uncertainty",
        "increases",
        "companies",
        "tend",
        "to",
        "be",
        "more",
        "cautious",
        "about",
        "hiring",
        "new",
        "employees"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ushbu dastur foydalanuvchi xatti-harakatlarini tahlil qilib, unga mos tavsiyalar yaratadi.",
      "target_text": "The program analyzes user behavior and generates personalized recommendations.",
      "words": [
        "The",
        "program",
        "analyzes",
        "user",
        "behavior",
        "and",
        "generates",
        "personalized",
        "recommendations"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Odamlar sog'lom odatlarni uzoq vaqt davomida saqlab qolishlari uchun maqsadlar real bo'lishi kerak.",
      "target_text": "Goals need to be realistic if people are to maintain healthy habits over a long period.",
      "words": [
        "Goals",
        "need",
        "to",
        "be",
        "realistic",
        "if",
        "people",
        "are",
        "to",
        "maintain",
        "healthy",
        "habits",
        "over",
        "a",
        "long",
        "period"
      ],
      "topic": "Health"
    },
    {
      "source_text": "Sun'iy yo'ldosh ma'lumotlari fermerlarga dala holatini masofadan kuzatish imkonini berib, vaqtni tejaydi.",
      "target_text": "Satellite data allows farmers to monitor field conditions remotely, saving time.",
      "words": [
        "Satellite",
        "data",
        "allows",
        "farmers",
        "to",
        "monitor",
        "field",
        "conditions",
        "remotely",
        "saving",
        "time"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Kompaniya raqobatchilarining narxlarini tahlil qilib, mahsulot strategiyasini o'zgartirdi.",
      "target_text": "The company analyzed its competitors' prices and changed its product strategy.",
      "words": [
        "The",
        "company",
        "analyzed",
        "its",
        "competitors",
        "prices",
        "and",
        "changed",
        "its",
        "product",
        "strategy"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi siyosat ishchilarning huquqlarini himoya qilish bilan birga kompaniyalarning moslashuvchanligini ham saqlashi kerak.",
      "target_text": "The new policy should protect workers' rights while maintaining companies' flexibility.",
      "words": [
        "The",
        "new",
        "policy",
        "should",
        "protect",
        "workers",
        "rights",
        "while",
        "maintaining",
        "companies",
        "flexibility"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Tadqiqotda qatnashganlarning aksariyati yangi tizimdan foydalanish osonroq ekanini aytdi.",
      "target_text": "Most participants in the study said that the new system was easier to use.",
      "words": [
        "Most",
        "participants",
        "in",
        "the",
        "study",
        "said",
        "that",
        "the",
        "new",
        "system",
        "was",
        "easier",
        "to",
        "use"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Texnologik taraqqiyot tezlashgani sari ta'lim dasturlarini muntazam yangilab borish zarur.",
      "target_text": "As technological progress accelerates, education programs need to be updated regularly.",
      "words": [
        "As",
        "technological",
        "progress",
        "accelerates",
        "education",
        "programs",
        "need",
        "to",
        "be",
        "updated",
        "regularly"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Men qaror qabul qilishdan oldin ma'lumotlarning bir nechta manbasini solishtirdim.",
      "target_text": "I compared several sources of data before making the decision.",
      "words": [
        "I",
        "compared",
        "several",
        "sources",
        "of",
        "data",
        "before",
        "making",
        "the",
        "decision"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Agar foydalanuvchilarga tizim qanday ishlashi tushuntirilmasa, ular unga ishonmasligi mumkin.",
      "target_text": "If users are not shown how the system works, they may not trust it.",
      "words": [
        "If",
        "users",
        "are",
        "not",
        "shown",
        "how",
        "the",
        "system",
        "works",
        "they",
        "may",
        "not",
        "trust",
        "it"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Kompaniya energiya sarfini kamaytirish maqsadida ishlab chiqarish jarayonini qayta loyihalashtirdi.",
      "target_text": "The company redesigned its production process in order to reduce energy consumption.",
      "words": [
        "The",
        "company",
        "redesigned",
        "its",
        "production",
        "process",
        "in",
        "order",
        "to",
        "reduce",
        "energy",
        "consumption"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Tadqiqotchilar kichik namunadan olingan natijalarni butun aholi uchun umumlashtirishdan oldin ehtiyotkor bo'lishdi.",
      "target_text": "The researchers were cautious about generalizing results from a small sample to the entire population.",
      "words": [
        "The",
        "researchers",
        "were",
        "cautious",
        "about",
        "generalizing",
        "results",
        "from",
        "a",
        "small",
        "sample",
        "to",
        "the",
        "entire",
        "population"
      ],
      "topic": "Science"
    },
    {
      "source_text": "U yangi ishga o'tganidan beri professional ko'nikmalarini ancha rivojlantirdi.",
      "target_text": "She has developed her professional skills considerably since changing jobs.",
      "words": [
        "She",
        "has",
        "developed",
        "her",
        "professional",
        "skills",
        "considerably",
        "since",
        "changing",
        "jobs"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Raqamli to'lovlarning kengayishi kichik biznes uchun xaridorlarga xizmat ko'rsatishni osonlashtirdi.",
      "target_text": "The expansion of digital payments has made it easier for small businesses to serve customers.",
      "words": [
        "The",
        "expansion",
        "of",
        "digital",
        "payments",
        "has",
        "made",
        "it",
        "easier",
        "for",
        "small",
        "businesses",
        "to",
        "serve",
        "customers"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Tadqiqot natijalarini mustaqil ravishda takrorlash mumkin bo'lmasa, ularning ishonchliligi savol ostida qoladi.",
      "target_text": "If research findings cannot be independently replicated, their reliability remains questionable.",
      "words": [
        "If",
        "research",
        "findings",
        "cannot",
        "be",
        "independently",
        "replicated",
        "their",
        "reliability",
        "remains",
        "questionable"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Sun'iy intellekt vositalaridan foydalanish vaqtni tejashi mumkin, biroq ular inson qarorlarini to'liq almashtirmasligi kerak.",
      "target_text": "Using artificial intelligence tools can save time, but they should not completely replace human judgment.",
      "words": [
        "Using",
        "artificial",
        "intelligence",
        "tools",
        "can",
        "save",
        "time",
        "but",
        "they",
        "should",
        "not",
        "completely",
        "replace",
        "human",
        "judgment"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Yangi transport siyosati joriy etilgach, shahar markazidagi tirbandlik asta-sekin kamaydi.",
      "target_text": "After the new transport policy was introduced, congestion in the city center gradually decreased.",
      "words": [
        "After",
        "the",
        "new",
        "transport",
        "policy",
        "was",
        "introduced",
        "congestion",
        "in",
        "the",
        "city",
        "center",
        "gradually",
        "decreased"
      ],
      "topic": "Transport"
    },
    {
      "source_text": "Kompaniya xalqaro bozorga chiqishdan oldin mahsulotining mahalliy madaniyatga mosligini tekshirdi.",
      "target_text": "Before entering the international market, the company checked whether its product suited the local culture.",
      "words": [
        "Before",
        "entering",
        "the",
        "international",
        "market",
        "the",
        "company",
        "checked",
        "whether",
        "its",
        "product",
        "suited",
        "the",
        "local",
        "culture"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Iqlim ma'lumotlari uzoq muddatli tendensiyalarni ko'rsatishi mumkin, ammo qisqa muddatli o'zgarishlarni aniq bashorat qilish qiyin.",
      "target_text": "Climate data can reveal long-term trends, but short-term changes are difficult to predict accurately.",
      "words": [
        "Climate",
        "data",
        "can",
        "reveal",
        "long-term",
        "trends",
        "but",
        "short-term",
        "changes",
        "are",
        "difficult",
        "to",
        "predict",
        "accurately"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Universitet yangi laboratoriyani ochib, talabalar uchun amaliy tadqiqot imkoniyatlarini kengaytirdi.",
      "target_text": "The university opened a new laboratory, expanding opportunities for practical research.",
      "words": [
        "The",
        "university",
        "opened",
        "a",
        "new",
        "laboratory",
        "expanding",
        "opportunities",
        "for",
        "practical",
        "research"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Uchrashuv bekor qilinganligi sababli, jamoa qarorni elektron pochta orqali muhokama qildi.",
      "target_text": "Since the meeting had been cancelled, the team discussed the decision by email.",
      "words": [
        "Since",
        "the",
        "meeting",
        "had",
        "been",
        "cancelled",
        "the",
        "team",
        "discussed",
        "the",
        "decision",
        "by",
        "email"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Modelning aniqligi oshirilishi bilan birga uning hisoblash xarajati ham ortdi.",
      "target_text": "As the model's accuracy was improved, its computational cost also increased.",
      "words": [
        "As",
        "the",
        "model's",
        "accuracy",
        "was",
        "improved",
        "its",
        "computational",
        "cost",
        "also",
        "increased"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Yangi dastur bir nechta tillarni qo'llab-quvvatlashi sababli xalqaro foydalanuvchilar uchun qulayroq bo'ldi.",
      "target_text": "The new application became more convenient for international users because it supports several languages.",
      "words": [
        "The",
        "new",
        "application",
        "became",
        "more",
        "convenient",
        "for",
        "international",
        "users",
        "because",
        "it",
        "supports",
        "several",
        "languages"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Fermerlar ob-havo prognozlaridan foydalanib, ekish vaqtini yanada samarali rejalashtirishmoqda.",
      "target_text": "Farmers are using weather forecasts to plan planting periods more efficiently.",
      "words": [
        "Farmers",
        "are",
        "using",
        "weather",
        "forecasts",
        "to",
        "plan",
        "planting",
        "periods",
        "more",
        "efficiently"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Agar kompaniya o'zgaruvchan bozor sharoitlariga moslasha olmasa, raqobatchilaridan ortda qolishi mumkin.",
      "target_text": "If a company cannot adapt to changing market conditions, it may fall behind its competitors.",
      "words": [
        "If",
        "a",
        "company",
        "cannot",
        "adapt",
        "to",
        "changing",
        "market",
        "conditions",
        "it",
        "may",
        "fall",
        "behind",
        "its",
        "competitors"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men ushbu usulni tanladim, chunki u kichik ma'lumotlar to'plamida ham yaxshi natija bergan.",
      "target_text": "I chose this method because it had performed well even on a small dataset.",
      "words": [
        "I",
        "chose",
        "this",
        "method",
        "because",
        "it",
        "had",
        "performed",
        "well",
        "even",
        "on",
        "a",
        "small",
        "dataset"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Olimlar yangi nazariya mavjud dalillarni avvalgisiga qaraganda yaxshiroq tushuntirishini ta'kidlashdi.",
      "target_text": "The scientists argued that the new theory explained the existing evidence better than the previous one.",
      "words": [
        "The",
        "scientists",
        "argued",
        "that",
        "the",
        "new",
        "theory",
        "explained",
        "the",
        "existing",
        "evidence",
        "better",
        "than",
        "the",
        "previous",
        "one"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Raqamli texnologiyalar imkoniyatlarni kengaytirishi bilan birga yangi axloqiy savollarni ham yuzaga keltirmoqda.",
      "target_text": "While digital technologies expand opportunities, they are also raising new ethical questions.",
      "words": [
        "While",
        "digital",
        "technologies",
        "expand",
        "opportunities",
        "they",
        "are",
        "also",
        "raising",
        "new",
        "ethical",
        "questions"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Kompaniya qarorlarini faqat qisqa muddatli foydaga asoslamasdan, uzoq muddatli ta'sirni ham hisobga olishi kerak.",
      "target_text": "The company should consider long-term effects rather than basing its decisions only on short-term profit.",
      "words": [
        "The",
        "company",
        "should",
        "consider",
        "long-term",
        "effects",
        "rather",
        "than",
        "basing",
        "its",
        "decisions",
        "only",
        "on",
        "short-term",
        "profit"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Tadqiqot davomida ishtirokchilar bir xil sharoitda sinovdan o'tkazildi, shunda natijalarni taqqoslash mumkin edi.",
      "target_text": "During the study, participants were tested under the same conditions so that the results could be compared.",
      "words": [
        "During",
        "the",
        "study",
        "participants",
        "were",
        "tested",
        "under",
        "the",
        "same",
        "conditions",
        "so",
        "that",
        "the",
        "results",
        "could",
        "be",
        "compared"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Sun'iy intellekt yordamida yaratilgan kontent ko'paygani sari uning manbasini ko'rsatish yanada muhimlashmoqda.",
      "target_text": "As AI-generated content becomes more common, identifying its source is becoming increasingly important.",
      "words": [
        "As",
        "AI-generated",
        "content",
        "becomes",
        "more",
        "common",
        "identifying",
        "its",
        "source",
        "is",
        "becoming",
        "increasingly",
        "important"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Yangi siyosat energiya samaradorligini oshirishga qaratilgan bo'lsa-da, uning amaliy natijalari hali baholanmagan.",
      "target_text": "Although the new policy aims to improve energy efficiency, its practical effects have not yet been assessed.",
      "words": [
        "Although",
        "the",
        "new",
        "policy",
        "aims",
        "to",
        "improve",
        "energy",
        "efficiency",
        "its",
        "practical",
        "effects",
        "have",
        "not",
        "yet",
        "been",
        "assessed"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Men loyiha muvaffaqiyatli bo'lishi uchun texnik yechim bilan bir qatorda foydalanuvchi ehtiyojlarini ham hisobga oldim.",
      "target_text": "I considered user needs alongside the technical solution to make the project successful.",
      "words": [
        "I",
        "considered",
        "user",
        "needs",
        "alongside",
        "the",
        "technical",
        "solution",
        "to",
        "make",
        "the",
        "project",
        "successful"
      ],
      "topic": "Work"
    },
    {
      "source_text": "O'zbekistonda texnologik startaplar ko'payib borayotgani yosh mutaxassislar uchun yangi imkoniyatlar yaratmoqda.",
      "target_text": "The growing number of technology startups in Uzbekistan is creating new opportunities for young professionals.",
      "words": [
        "The",
        "growing",
        "number",
        "of",
        "technology",
        "startups",
        "in",
        "Uzbekistan",
        "is",
        "creating",
        "new",
        "opportunities",
        "for",
        "young",
        "professionals"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Agar ma'lumotlar muntazam yangilanib turmasa, tizimning bashoratlari vaqt o'tishi bilan ishonchsiz bo'lib qolishi mumkin.",
      "target_text": "If the data is not updated regularly, the system's predictions may become unreliable over time.",
      "words": [
        "If",
        "the",
        "data",
        "is",
        "not",
        "updated",
        "regularly",
        "the",
        "system's",
        "predictions",
        "may",
        "become",
        "unreliable",
        "over",
        "time"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Tadqiqotchilar yangi usulni joriy etishdan oldin uning mavjud tizim bilan mosligini tekshirishdi.",
      "target_text": "The researchers checked the new method's compatibility with the existing system before implementing it.",
      "words": [
        "The",
        "researchers",
        "checked",
        "the",
        "new",
        "method's",
        "compatibility",
        "with",
        "the",
        "existing",
        "system",
        "before",
        "implementing",
        "it"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Bozorning keskin o'zgarishiga qaramay, kompaniya o'zining asosiy strategiyasini saqlab qoldi.",
      "target_text": "Despite the sharp change in the market, the company maintained its core strategy.",
      "words": [
        "Despite",
        "the",
        "sharp",
        "change",
        "in",
        "the",
        "market",
        "the",
        "company",
        "maintained",
        "its",
        "core",
        "strategy"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ta'lim sifatini yaxshilash uchun faqat texnologiya emas, balki malakali o'qituvchilar ham zarur.",
      "target_text": "Improving educational quality requires not only technology but also qualified teachers.",
      "words": [
        "Improving",
        "educational",
        "quality",
        "requires",
        "not",
        "only",
        "technology",
        "but",
        "also",
        "qualified",
        "teachers"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Uzoq muddatli ekologik siyosat qisqa muddatli iqtisodiy manfaatlardan ustun qo'yilishi kerak.",
      "target_text": "Long-term environmental policy should be given greater priority than short-term economic interests.",
      "words": [
        "Long-term",
        "environmental",
        "policy",
        "should",
        "be",
        "given",
        "greater",
        "priority",
        "than",
        "short-term",
        "economic",
        "interests"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Modelni real sharoitda qo'llashdan oldin uning turli guruhlarda bir xil ishlashi tekshirildi.",
      "target_text": "Before the model was used in real conditions, its performance across different groups was tested.",
      "words": [
        "Before",
        "the",
        "model",
        "was",
        "used",
        "in",
        "real",
        "conditions",
        "its",
        "performance",
        "across",
        "different",
        "groups",
        "was",
        "tested"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Men natijalarni taqdim etishda noaniqliklarni yashirish o'rniga ularni ochiq ko'rsatishni ma'qul ko'raman.",
      "target_text": "When presenting results, I prefer to show uncertainties openly rather than hide them.",
      "words": [
        "When",
        "presenting",
        "results",
        "I",
        "prefer",
        "to",
        "show",
        "uncertainties",
        "openly",
        "rather",
        "than",
        "hide",
        "them"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Kompaniya xodimlarning fikrlarini hisobga olganidan keyin yangi ish jarayonini joriy qildi.",
      "target_text": "The company introduced a new workflow after taking employees' opinions into account.",
      "words": [
        "The",
        "company",
        "introduced",
        "a",
        "new",
        "workflow",
        "after",
        "taking",
        "employees",
        "opinions",
        "into",
        "account"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Sun'iy intellektning foydasi uning texnik imkoniyatlaridan ko'ra qanday qo'llanilishiga ko'proq bog'liq bo'lishi mumkin.",
      "target_text": "The value of artificial intelligence may depend more on how it is used than on its technical capabilities.",
      "words": [
        "The",
        "value",
        "of",
        "artificial",
        "intelligence",
        "may",
        "depend",
        "more",
        "on",
        "how",
        "it",
        "is",
        "used",
        "than",
        "on",
        "its",
        "technical",
        "capabilities"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Tadqiqot guruhi kutilmagan natijaga duch kelgach, qo'shimcha tajribalar o'tkazishga qaror qildi.",
      "target_text": "After encountering an unexpected result, the research team decided to conduct additional experiments.",
      "words": [
        "After",
        "encountering",
        "an",
        "unexpected",
        "result",
        "the",
        "research",
        "team",
        "decided",
        "to",
        "conduct",
        "additional",
        "experiments"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Yangi biznes strategiyasi mijozlar sodiqligini oshirish bilan birga xarajatlarni nazorat qilishga qaratilgan.",
      "target_text": "The new business strategy aims to increase customer loyalty while keeping costs under control.",
      "words": [
        "The",
        "new",
        "business",
        "strategy",
        "aims",
        "to",
        "increase",
        "customer",
        "loyalty",
        "while",
        "keeping",
        "costs",
        "under",
        "control"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Shaharlar iqlim xavflariga moslashar ekan, infratuzilmani uzoq muddatli rejalashtirish tobora muhimlashadi.",
      "target_text": "As cities adapt to climate risks, long-term infrastructure planning becomes increasingly important.",
      "words": [
        "As",
        "cities",
        "adapt",
        "to",
        "climate",
        "risks",
        "long-term",
        "infrastructure",
        "planning",
        "becomes",
        "increasingly",
        "important"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Kompaniya ma'lumotlarni shifrlash orqali ruxsatsiz kirish ehtimolini sezilarli darajada kamaytirdi.",
      "target_text": "The company significantly reduced the risk of unauthorized access by encrypting its data.",
      "words": [
        "The",
        "company",
        "significantly",
        "reduced",
        "the",
        "risk",
        "of",
        "unauthorized",
        "access",
        "by",
        "encrypting",
        "its",
        "data"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Agar tadqiqot yetarlicha katta namunaga asoslanmasa, uning xulosalari cheklangan bo'lishi mumkin.",
      "target_text": "If research is not based on a sufficiently large sample, its conclusions may be limited.",
      "words": [
        "If",
        "research",
        "is",
        "not",
        "based",
        "on",
        "a",
        "sufficiently",
        "large",
        "sample",
        "its",
        "conclusions",
        "may",
        "be",
        "limited"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Yangi tizimning samaradorligi oshganiga qaramay, uni joriy etish xodimlardan qo'shimcha tayyorgarlikni talab qildi.",
      "target_text": "Although the new system was more efficient, implementing it required additional training for employees.",
      "words": [
        "Although",
        "the",
        "new",
        "system",
        "was",
        "more",
        "efficient",
        "implementing",
        "it",
        "required",
        "additional",
        "training",
        "for",
        "employees"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Men bir nechta modelni sinab ko'rdim, chunki bitta usul barcha vazifalarda bir xil natija bermadi.",
      "target_text": "I tested several models because no single method performed equally well on every task.",
      "words": [
        "I",
        "tested",
        "several",
        "models",
        "because",
        "no",
        "single",
        "method",
        "performed",
        "equally",
        "well",
        "on",
        "every",
        "task"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Kompaniya foydani oshirish bilan birga mijozlar ishonchini saqlab qolishni ham maqsad qilgan.",
      "target_text": "The company aims to increase profits while maintaining customer trust.",
      "words": [
        "The",
        "company",
        "aims",
        "to",
        "increase",
        "profits",
        "while",
        "maintaining",
        "customer",
        "trust"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Tadqiqotchilar yangi materialning xususiyatlari kutilganidan farq qilishini aniqlashdi.",
      "target_text": "The researchers discovered that the properties of the new material differed from what had been expected.",
      "words": [
        "The",
        "researchers",
        "discovered",
        "that",
        "the",
        "properties",
        "of",
        "the",
        "new",
        "material",
        "differed",
        "from",
        "what",
        "had",
        "been",
        "expected"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Texnologik taraqqiyot tezlashgani sari xodimlarning yangi ko'nikmalarni o'rganishi tobora zarur bo'lmoqda.",
      "target_text": "As technological progress accelerates, learning new skills is becoming increasingly necessary for employees.",
      "words": [
        "As",
        "technological",
        "progress",
        "accelerates",
        "learning",
        "new",
        "skills",
        "is",
        "becoming",
        "increasingly",
        "necessary",
        "for",
        "employees"
      ],
      "topic": "Work"
    },
    {
      "source_text": "Agar sun'iy intellekt tizimlari shaffof bo'lmasa, foydalanuvchilar ularning qarorlarini qabul qilishda qiynalishi mumkin.",
      "target_text": "If artificial intelligence systems are not transparent, users may struggle to accept their decisions.",
      "words": [
        "If",
        "artificial",
        "intelligence",
        "systems",
        "are",
        "not",
        "transparent",
        "users",
        "may",
        "struggle",
        "to",
        "accept",
        "their",
        "decisions"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Qishloq xo'jaligida aniq ma'lumotlardan foydalanish resurslarni tejash va hosildorlikni oshirishga yordam beradi.",
      "target_text": "Using accurate data in agriculture can help save resources and increase productivity.",
      "words": [
        "Using",
        "accurate",
        "data",
        "in",
        "agriculture",
        "can",
        "help",
        "save",
        "resources",
        "and",
        "increase",
        "productivity"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Yangi qonun kuchga kirgach, kompaniyalar ma'lumotlarni saqlash siyosatini o'zgartirishga majbur bo'ldi.",
      "target_text": "After the new law came into force, companies had to change their data-storage policies.",
      "words": [
        "After",
        "the",
        "new",
        "law",
        "came",
        "into",
        "force",
        "companies",
        "had",
        "to",
        "change",
        "their",
        "data-storage",
        "policies"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ushbu yondashuv qimmat uskunalarni talab qilmagani uchun kichik tashkilotlar uchun ham mos keladi.",
      "target_text": "This approach is suitable for small organizations because it does not require expensive equipment.",
      "words": [
        "This",
        "approach",
        "is",
        "suitable",
        "for",
        "small",
        "organizations",
        "because",
        "it",
        "does",
        "not",
        "require",
        "expensive",
        "equipment"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Tadqiqot natijalari dastlabki taxminni tasdiqlamagan bo'lsa-da, ular yangi savollarni yuzaga keltirdi.",
      "target_text": "Although the research results did not confirm the initial assumption, they raised new questions.",
      "words": [
        "Although",
        "the",
        "research",
        "results",
        "did",
        "not",
        "confirm",
        "the",
        "initial",
        "assumption",
        "they",
        "raised",
        "new",
        "questions"
      ],
      "topic": "Science"
    },
    {
      "source_text": "O'zbekistonda raqamli xizmatlarning kengayishi aholining kundalik ishlarini ancha soddalashtirmoqda.",
      "target_text": "The expansion of digital services in Uzbekistan is making everyday tasks considerably easier for people.",
      "words": [
        "The",
        "expansion",
        "of",
        "digital",
        "services",
        "in",
        "Uzbekistan",
        "is",
        "making",
        "everyday",
        "tasks",
        "considerably",
        "easier",
        "for",
        "people"
      ],
      "topic": "Uzbekistan"
    }
  ],
  "C1": [
    {
      "source_text": "Sun'iy intellektning jadal rivojlanishi texnologik taraqqiyot bilan bir qatorda uning ijtimoiy oqibatlarini ham chuqurroq muhokama qilishni talab qilmoqda.",
      "target_text": "The rapid advancement of artificial intelligence is prompting deeper discussion of its social consequences alongside technological progress.",
      "words": [
        "The",
        "rapid",
        "advancement",
        "of",
        "artificial",
        "intelligence",
        "is",
        "prompting",
        "deeper",
        "discussion",
        "of",
        "its",
        "social",
        "consequences",
        "alongside",
        "technological",
        "progress"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Kvant hisoblash amaliy jihatdan yetuklashgani sari, hozirgi shifrlash usullarining barqarorligi jiddiy qayta ko'rib chiqilishi mumkin.",
      "target_text": "As quantum computing matures, the resilience of existing encryption methods may need to be seriously reconsidered.",
      "words": [
        "As",
        "quantum",
        "computing",
        "matures",
        "the",
        "resilience",
        "of",
        "existing",
        "encryption",
        "methods",
        "may",
        "need",
        "to",
        "be",
        "seriously",
        "reconsidered"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Tadqiqotchilar model yuqori aniqlikni namoyish etgan bo'lsa-da, uning real sharoitdagi ishonchliligi hali to'liq isbotlanmaganini ta'kidladilar.",
      "target_text": "The researchers emphasized that although the model demonstrated high accuracy, its reliability in real-world conditions had not yet been fully established.",
      "words": [
        "The",
        "researchers",
        "emphasized",
        "that",
        "although",
        "the",
        "model",
        "demonstrated",
        "high",
        "accuracy",
        "its",
        "reliability",
        "in",
        "real-world",
        "conditions",
        "had",
        "not",
        "yet",
        "been",
        "fully",
        "established"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Raqamli platformalar ta'limni demokratlashtirishi mumkin, biroq ulardan foydalanishdagi tengsizlik mavjud farqlarni yanada kuchaytirishi ehtimoldan xoli emas.",
      "target_text": "Digital platforms can democratize education, but unequal access to them may well deepen existing disparities.",
      "words": [
        "Digital",
        "platforms",
        "can",
        "democratize",
        "education",
        "but",
        "unequal",
        "access",
        "to",
        "them",
        "may",
        "well",
        "deepen",
        "existing",
        "disparities"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Iqlim siyosati qisqa muddatli iqtisodiy xarajatlardan ko'ra uzoq muddatli ekologik barqarorlikni ustuvor qo'yishi kerak.",
      "target_text": "Climate policy should prioritize long-term environmental sustainability over short-term economic costs.",
      "words": [
        "Climate",
        "policy",
        "should",
        "prioritize",
        "long-term",
        "environmental",
        "sustainability",
        "over",
        "short-term",
        "economic",
        "costs"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Kompaniya bozor ulushini oshirganiga qaramay, uning strategiyasi mijozlarning o'zgaruvchan ehtiyojlariga yetarlicha moslashmagan edi.",
      "target_text": "Despite increasing its market share, the company's strategy had failed to adapt sufficiently to changing customer needs.",
      "words": [
        "Despite",
        "increasing",
        "its",
        "market",
        "share",
        "the",
        "company's",
        "strategy",
        "had",
        "failed",
        "to",
        "adapt",
        "sufficiently",
        "to",
        "changing",
        "customer",
        "needs"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ma'lumotlar sifati qanchalik yuqori bo'lmasin, noto'g'ri tanlangan ko'rsatkichlar tahlil natijalarini chalg'itishi mumkin.",
      "target_text": "No matter how high the data quality is, poorly selected indicators can distort analytical results.",
      "words": [
        "No",
        "matter",
        "how",
        "high",
        "the",
        "data",
        "quality",
        "is",
        "poorly",
        "selected",
        "indicators",
        "can",
        "distort",
        "analytical",
        "results"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Yangi algoritmni ishlab chiqishda tadqiqotchilar nafaqat aniqlikni, balki hisoblash xarajatlarini ham hisobga olishdi.",
      "target_text": "In developing the new algorithm, the researchers considered not only accuracy but also computational cost.",
      "words": [
        "In",
        "developing",
        "the",
        "new",
        "algorithm",
        "the",
        "researchers",
        "considered",
        "not",
        "only",
        "accuracy",
        "but",
        "also",
        "computational",
        "cost"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Agar tizim foydalanuvchilarning xatti-harakatlari o'zgarganini hisobga olmasa, uning dastlabki samaradorligi vaqt o'tishi bilan pasayib boradi.",
      "target_text": "If a system fails to account for changes in user behavior, its initial effectiveness will gradually decline over time.",
      "words": [
        "If",
        "a",
        "system",
        "fails",
        "to",
        "account",
        "for",
        "changes",
        "in",
        "user",
        "behavior",
        "its",
        "initial",
        "effectiveness",
        "will",
        "gradually",
        "decline",
        "over",
        "time"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Sun'iy intellekt qarorlarini tushuntirish qobiliyati, ayniqsa, natijalar inson hayotiga bevosita ta'sir qiladigan sohalarda muhim ahamiyat kasb etadi.",
      "target_text": "The ability to explain AI decisions is particularly important in fields where outcomes directly affect people's lives.",
      "words": [
        "The",
        "ability",
        "to",
        "explain",
        "AI",
        "decisions",
        "is",
        "particularly",
        "important",
        "in",
        "fields",
        "where",
        "outcomes",
        "directly",
        "affect",
        "people's",
        "lives"
      ],
      "topic": "AI Ethics"
    },
    {
      "source_text": "Tadqiqotning dastlabki bosqichida olingan natijalar istiqbolli ko'rinsa-da, ularni kengroq populyatsiyaga tatbiq etishdan oldin qo'shimcha dalillar talab etiladi.",
      "target_text": "Although the initial findings appear promising, further evidence is required before they can be generalized to a broader population.",
      "words": [
        "Although",
        "the",
        "initial",
        "findings",
        "appear",
        "promising",
        "further",
        "evidence",
        "is",
        "required",
        "before",
        "they",
        "can",
        "be",
        "generalized",
        "to",
        "a",
        "broader",
        "population"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya yangi texnologiyani joriy etishdan oldin uning huquqiy va axloqiy oqibatlarini mustaqil ekspertlar yordamida baholadi.",
      "target_text": "Before adopting the new technology, the company assessed its legal and ethical implications with the help of independent experts.",
      "words": [
        "Before",
        "adopting",
        "the",
        "new",
        "technology",
        "the",
        "company",
        "assessed",
        "its",
        "legal",
        "and",
        "ethical",
        "implications",
        "with",
        "the",
        "help",
        "of",
        "independent",
        "experts"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Raqamli iqtisodiyot kengayib borar ekan, an'anaviy kasblarning ayrimlari yo'qolishi bilan birga ilgari mavjud bo'lmagan yangi mutaxassisliklar paydo bo'lmoqda.",
      "target_text": "As the digital economy expands, some traditional occupations are disappearing while new professions are emerging.",
      "words": [
        "As",
        "the",
        "digital",
        "economy",
        "expands",
        "some",
        "traditional",
        "occupations",
        "are",
        "disappearing",
        "while",
        "new",
        "professions",
        "are",
        "emerging"
      ],
      "topic": "Business"
    },
    {
      "source_text": "O'zbekistonda texnologik infratuzilmaning rivojlanishi mintaqadagi startap ekotizimining raqobatbardoshligini oshirishi mumkin.",
      "target_text": "The development of technological infrastructure in Uzbekistan could strengthen the competitiveness of the region's startup ecosystem.",
      "words": [
        "The",
        "development",
        "of",
        "technological",
        "infrastructure",
        "in",
        "Uzbekistan",
        "could",
        "strengthen",
        "the",
        "competitiveness",
        "of",
        "the",
        "region's",
        "startup",
        "ecosystem"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Sun'iy yo'ldosh tasvirlarini meteorologik ma'lumotlar bilan birlashtirish qishloq xo'jaligi hosildorligini aniqroq prognoz qilish imkonini beradi.",
      "target_text": "Combining satellite imagery with meteorological data makes it possible to forecast agricultural yields more accurately.",
      "words": [
        "Combining",
        "satellite",
        "imagery",
        "with",
        "meteorological",
        "data",
        "makes",
        "it",
        "possible",
        "to",
        "forecast",
        "agricultural",
        "yields",
        "more",
        "accurately"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Tahlilchilar kompaniyaning daromadi oshganini ijobiy belgi sifatida baholashgan bo'lsa-da, xarajatlarning tezroq o'sishi xavotir uyg'otdi.",
      "target_text": "Although analysts viewed the rise in the company's revenue as a positive sign, the faster growth in costs caused concern.",
      "words": [
        "Although",
        "analysts",
        "viewed",
        "the",
        "rise",
        "in",
        "the",
        "company's",
        "revenue",
        "as",
        "a",
        "positive",
        "sign",
        "the",
        "faster",
        "growth",
        "in",
        "costs",
        "caused",
        "concern"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi siyosat amalda qanday ishlashi, uning qog'ozda qanchalik yaxshi ishlab chiqilganidan ko'ra muhimroq bo'lishi mumkin.",
      "target_text": "How the new policy works in practice may matter more than how well it has been designed on paper.",
      "words": [
        "How",
        "the",
        "new",
        "policy",
        "works",
        "in",
        "practice",
        "may",
        "matter",
        "more",
        "than",
        "how",
        "well",
        "it",
        "has",
        "been",
        "designed",
        "on",
        "paper"
      ],
      "topic": "Policy"
    },
    {
      "source_text": "Texnologik kompaniyalar innovatsiyani tezlashtirishga intilar ekan, ma'lumotlar maxfiyligini himoya qilish masalasi tobora murakkablashmoqda.",
      "target_text": "As technology companies seek to accelerate innovation, protecting data privacy is becoming increasingly complex.",
      "words": [
        "As",
        "technology",
        "companies",
        "seek",
        "to",
        "accelerate",
        "innovation",
        "protecting",
        "data",
        "privacy",
        "is",
        "becoming",
        "increasingly",
        "complex"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ushbu tadqiqot avvalgi qarashlarni butunlay rad etmaydi; aksincha, ularni ancha nozik tushuntirishni taklif qiladi.",
      "target_text": "This study does not entirely reject previous views; rather, it offers a more nuanced interpretation of them.",
      "words": [
        "This",
        "study",
        "does",
        "not",
        "entirely",
        "reject",
        "previous",
        "views",
        "rather",
        "it",
        "offers",
        "a",
        "more",
        "nuanced",
        "interpretation",
        "of",
        "them"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Modelning yuqori aniqligi uni avtomatik ravishda foydali vositaga aylantirmaydi, chunki amaliy qo'llashda boshqa omillar ham muhim.",
      "target_text": "High model accuracy does not automatically make it a useful tool, since other factors also matter in practical applications.",
      "words": [
        "High",
        "model",
        "accuracy",
        "does",
        "not",
        "automatically",
        "make",
        "it",
        "a",
        "useful",
        "tool",
        "since",
        "other",
        "factors",
        "also",
        "matter",
        "in",
        "practical",
        "applications"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Kompaniya qisqa muddatli foydani oshirishga muvaffaq bo'lgan bo'lsa-da, bu qaror uzoq muddatda uning obro'siga zarar yetkazishi mumkin.",
      "target_text": "Although the company succeeded in increasing short-term profits, the decision could damage its reputation in the long run.",
      "words": [
        "Although",
        "the",
        "company",
        "succeeded",
        "in",
        "increasing",
        "short-term",
        "profits",
        "the",
        "decision",
        "could",
        "damage",
        "its",
        "reputation",
        "in",
        "the",
        "long",
        "run"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Iqlim o'zgarishining oqibatlari hududlar bo'yicha bir xil namoyon bo'lmagani sababli, yagona siyosat barcha jamoalarga mos kelmasligi mumkin.",
      "target_text": "Because the effects of climate change do not appear equally across regions, a single policy may not suit every community.",
      "words": [
        "Because",
        "the",
        "effects",
        "of",
        "climate",
        "change",
        "do",
        "not",
        "appear",
        "equally",
        "across",
        "regions",
        "a",
        "single",
        "policy",
        "may",
        "not",
        "suit",
        "every",
        "community"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Tadqiqotchilar yangi usulni taklif qilish bilan cheklanmay, uning mavjud yondashuvlardan qaysi sharoitlarda ustun ekanini ham ko'rsatdilar.",
      "target_text": "The researchers not only proposed a new method but also demonstrated the conditions under which it outperforms existing approaches.",
      "words": [
        "The",
        "researchers",
        "not",
        "only",
        "proposed",
        "a",
        "new",
        "method",
        "but",
        "also",
        "demonstrated",
        "the",
        "conditions",
        "under",
        "which",
        "it",
        "outperforms",
        "existing",
        "approaches"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Ta'lim tizimlari sun'iy intellektdan foydalanishni taqiqlash o'rniga, undan mas'uliyatli foydalanish ko'nikmalarini shakllantirishi maqsadga muvofiq.",
      "target_text": "Rather than banning the use of artificial intelligence, education systems should develop skills for using it responsibly.",
      "words": [
        "Rather",
        "than",
        "banning",
        "the",
        "use",
        "of",
        "artificial",
        "intelligence",
        "education",
        "systems",
        "should",
        "develop",
        "skills",
        "for",
        "using",
        "it",
        "responsibly"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Ma'lumotlar yetarli darajada xilma-xil bo'lmasa, modelning ayrim guruhlar uchun yuqori natija ko'rsatishi umumiy adolatni anglatmaydi.",
      "target_text": "If the data is not sufficiently diverse, strong performance for some groups does not necessarily imply overall fairness.",
      "words": [
        "If",
        "the",
        "data",
        "is",
        "not",
        "sufficiently",
        "diverse",
        "strong",
        "performance",
        "for",
        "some",
        "groups",
        "does",
        "not",
        "necessarily",
        "imply",
        "overall",
        "fairness"
      ],
      "topic": "AI Ethics"
    },
    {
      "source_text": "Yangi texnologiya ish unumdorligini oshirishi mumkin, ammo u xodimlarning ish tajribasini avtomatik ravishda yaxshilamaydi.",
      "target_text": "The new technology may increase productivity, but it does not automatically improve employees' work experience.",
      "words": [
        "The",
        "new",
        "technology",
        "may",
        "increase",
        "productivity",
        "but",
        "it",
        "does",
        "not",
        "automatically",
        "improve",
        "employees",
        "work",
        "experience"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Kompaniya xalqaro kengayishni rejalashtirar ekan, mahalliy madaniy me'yorlarni hisobga olmaslik jiddiy strategik xatoga aylanishi mumkin.",
      "target_text": "As the company plans international expansion, failing to consider local cultural norms could become a serious strategic mistake.",
      "words": [
        "As",
        "the",
        "company",
        "plans",
        "international",
        "expansion",
        "failing",
        "to",
        "consider",
        "local",
        "cultural",
        "norms",
        "could",
        "become",
        "a",
        "serious",
        "strategic",
        "mistake"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Qayta tiklanadigan energiyaga o'tish texnik jihatdan mumkin bo'lsa-da, uning iqtisodiy samaradorligi mamlakat sharoitiga bog'liq.",
      "target_text": "Although the transition to renewable energy is technically feasible, its economic viability depends on national circumstances.",
      "words": [
        "Although",
        "the",
        "transition",
        "to",
        "renewable",
        "energy",
        "is",
        "technically",
        "feasible",
        "its",
        "economic",
        "viability",
        "depends",
        "on",
        "national",
        "circumstances"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Tadqiqotda qo'llangan usul cheklangan namunaga asoslanganligi sababli, natijalarni ehtiyotkorlik bilan talqin qilish lozim.",
      "target_text": "Since the method used in the study was based on a limited sample, the results should be interpreted cautiously.",
      "words": [
        "Since",
        "the",
        "method",
        "used",
        "in",
        "the",
        "study",
        "was",
        "based",
        "on",
        "a",
        "limited",
        "sample",
        "the",
        "results",
        "should",
        "be",
        "interpreted",
        "cautiously"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Sun'iy intellekt tizimlarining murakkabligi oshgani sari, ularning qarorlarini insonlarga tushunarli tarzda izohlash qiyinlashmoqda.",
      "target_text": "As AI systems become more complex, explaining their decisions in a way that humans can understand is becoming more difficult.",
      "words": [
        "As",
        "AI",
        "systems",
        "become",
        "more",
        "complex",
        "explaining",
        "their",
        "decisions",
        "in",
        "a",
        "way",
        "that",
        "humans",
        "can",
        "understand",
        "is",
        "becoming",
        "more",
        "difficult"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Bozor sharoitlari keskin o'zgargan taqdirda ham, kompaniyaning asosiy qadriyatlari qisqa muddatli foyda uchun qurbon qilinmasligi kerak.",
      "target_text": "Even if market conditions change dramatically, a company's core values should not be sacrificed for short-term profit.",
      "words": [
        "Even",
        "if",
        "market",
        "conditions",
        "change",
        "dramatically",
        "a",
        "company's",
        "core",
        "values",
        "should",
        "not",
        "be",
        "sacrificed",
        "for",
        "short-term",
        "profit"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Men natijalarni talqin qilishda statistik ahamiyat bilan amaliy ahamiyat o'rtasidagi farqni hisobga olishni muhim deb bilaman.",
      "target_text": "I consider it important to distinguish between statistical significance and practical significance when interpreting results.",
      "words": [
        "I",
        "consider",
        "it",
        "important",
        "to",
        "distinguish",
        "between",
        "statistical",
        "significance",
        "and",
        "practical",
        "significance",
        "when",
        "interpreting",
        "results"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Yangi avlod modellarining imkoniyatlari kengayib borayotgan bo'lsa-da, ularning xatolarini to'liq bartaraf etish hali imkonsiz.",
      "target_text": "Although the capabilities of next-generation models are expanding, eliminating their errors entirely remains impossible.",
      "words": [
        "Although",
        "the",
        "capabilities",
        "of",
        "next-generation",
        "models",
        "are",
        "expanding",
        "eliminating",
        "their",
        "errors",
        "entirely",
        "remains",
        "impossible"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Agar qarorlar faqat tarixiy ma'lumotlarga asoslangan bo'lsa, tez o'zgarayotgan muhitda ular kutilganidek samarali bo'lmasligi mumkin.",
      "target_text": "If decisions are based solely on historical data, they may not remain effective in rapidly changing environments.",
      "words": [
        "If",
        "decisions",
        "are",
        "based",
        "solely",
        "on",
        "historical",
        "data",
        "they",
        "may",
        "not",
        "remain",
        "effective",
        "in",
        "rapidly",
        "changing",
        "environments"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "O'zbekistonda raqamli xizmatlarning kengayishi iqtisodiy faollikni rag'batlantirishi bilan birga, kiberxavfsizlik talablarini ham oshirmoqda.",
      "target_text": "The expansion of digital services in Uzbekistan is stimulating economic activity while also increasing cybersecurity requirements.",
      "words": [
        "The",
        "expansion",
        "of",
        "digital",
        "services",
        "in",
        "Uzbekistan",
        "is",
        "stimulating",
        "economic",
        "activity",
        "while",
        "also",
        "increasing",
        "cybersecurity",
        "requirements"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Sun'iy yo'ldosh ma'lumotlaridan foydalanish fermerlarga dalalarni masofadan kuzatish imkonini beradi, bu esa resurslarni aniqroq taqsimlashga yordam beradi.",
      "target_text": "Using satellite data enables farmers to monitor fields remotely, helping them allocate resources more precisely.",
      "words": [
        "Using",
        "satellite",
        "data",
        "enables",
        "farmers",
        "to",
        "monitor",
        "fields",
        "remotely",
        "helping",
        "them",
        "allocate",
        "resources",
        "more",
        "precisely"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Tizim muntazam yangilanib turmasa, foydalanuvchilarning xatti-harakatlaridagi yangi tendensiyalar model tomonidan e'tibordan chetda qolishi mumkin.",
      "target_text": "Unless the system is updated regularly, emerging patterns in user behavior may be overlooked by the model.",
      "words": [
        "Unless",
        "the",
        "system",
        "is",
        "updated",
        "regularly",
        "emerging",
        "patterns",
        "in",
        "user",
        "behavior",
        "may",
        "be",
        "overlooked",
        "by",
        "the",
        "model"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Tadqiqotchilar nazariy jihatdan jozibador bo'lgan yechim amaliy sharoitlarda juda katta hisoblash resurslarini talab qilishini aniqlashdi.",
      "target_text": "The researchers found that a theoretically attractive solution required excessive computational resources in practice.",
      "words": [
        "The",
        "researchers",
        "found",
        "that",
        "a",
        "theoretically",
        "attractive",
        "solution",
        "required",
        "excessive",
        "computational",
        "resources",
        "in",
        "practice"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Kompaniyaning muvaffaqiyati faqat moliyaviy ko'rsatkichlar bilan o'lchanmasligi, balki uning jamiyatga ta'siri ham hisobga olinishi kerak.",
      "target_text": "A company's success should not be measured solely by financial indicators; its impact on society should also be considered.",
      "words": [
        "A",
        "company's",
        "success",
        "should",
        "not",
        "be",
        "measured",
        "solely",
        "by",
        "financial",
        "indicators",
        "its",
        "impact",
        "on",
        "society",
        "should",
        "also",
        "be",
        "considered"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi tadqiqot avvalgi natijalarni takrorlagani bilan qimmatli, chunki ilmiy ishonchlilik mustaqil tasdiqlashga tayanadi.",
      "target_text": "The new study is valuable because it replicates earlier findings, as scientific reliability depends on independent confirmation.",
      "words": [
        "The",
        "new",
        "study",
        "is",
        "valuable",
        "because",
        "it",
        "replicates",
        "earlier",
        "findings",
        "as",
        "scientific",
        "reliability",
        "depends",
        "on",
        "independent",
        "confirmation"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Texnologik yechim muammoning o'zini hal qilishdan ko'ra uning alomatlarini yashirsa, uzoq muddatli foydasi shubhali bo'lib qoladi.",
      "target_text": "If a technological solution merely conceals the symptoms rather than addressing the problem itself, its long-term value remains questionable.",
      "words": [
        "If",
        "a",
        "technological",
        "solution",
        "merely",
        "conceals",
        "the",
        "symptoms",
        "rather",
        "than",
        "addressing",
        "the",
        "problem",
        "itself",
        "its",
        "long-term",
        "value",
        "remains",
        "questionable"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ta'limdagi sun'iy intellekt vositalari o'qituvchini almashtirishdan ko'ra uning individual o'quvchilarga ko'proq vaqt ajratishiga yordam berishi mumkin.",
      "target_text": "Rather than replacing teachers, AI tools in education may enable them to devote more time to individual students.",
      "words": [
        "Rather",
        "than",
        "replacing",
        "teachers",
        "AI",
        "tools",
        "in",
        "education",
        "may",
        "enable",
        "them",
        "to",
        "devote",
        "more",
        "time",
        "to",
        "individual",
        "students"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Kutilmagan natijalar tadqiqotni muvaffaqiyatsiz qilmaydi; aksincha, ular dastlabki farazlarni qayta ko'rib chiqishga sabab bo'lishi mumkin.",
      "target_text": "Unexpected results do not make a study unsuccessful; on the contrary, they may prompt researchers to reconsider their initial assumptions.",
      "words": [
        "Unexpected",
        "results",
        "do",
        "not",
        "make",
        "a",
        "study",
        "unsuccessful",
        "on",
        "the",
        "contrary",
        "they",
        "may",
        "prompt",
        "researchers",
        "to",
        "reconsider",
        "their",
        "initial",
        "assumptions"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya yangi bozorga kirishdan oldin raqobatchilarni tahlil qilmaganida, uning strategiyasi ancha katta xavf ostida qolgan bo'lardi.",
      "target_text": "Had the company failed to analyze its competitors before entering the new market, its strategy would have been far more vulnerable.",
      "words": [
        "Had",
        "the",
        "company",
        "failed",
        "to",
        "analyze",
        "its",
        "competitors",
        "before",
        "entering",
        "the",
        "new",
        "market",
        "its",
        "strategy",
        "would",
        "have",
        "been",
        "far",
        "more",
        "vulnerable"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Raqamli maxfiylikka oid qoidalar texnologik innovatsiyalarni to'xtatib qo'ymasdan, foydalanuvchilar huquqlarini samarali himoya qilishi kerak.",
      "target_text": "Regulations on digital privacy should protect users' rights effectively without unnecessarily restricting technological innovation.",
      "words": [
        "Regulations",
        "on",
        "digital",
        "privacy",
        "should",
        "protect",
        "users",
        "rights",
        "effectively",
        "without",
        "unnecessarily",
        "restricting",
        "technological",
        "innovation"
      ],
      "topic": "Policy"
    },
    {
      "source_text": "Iqlimga moslashish choralarini kechiktirish qisqa muddatda xarajatlarni kamaytirgandek ko'rinishi mumkin, ammo kelajakdagi zararlarni oshiradi.",
      "target_text": "Delaying climate adaptation measures may appear to reduce costs in the short term, but it increases future damage.",
      "words": [
        "Delaying",
        "climate",
        "adaptation",
        "measures",
        "may",
        "appear",
        "to",
        "reduce",
        "costs",
        "in",
        "the",
        "short",
        "term",
        "but",
        "it",
        "increases",
        "future",
        "damage"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Ma'lumotlar to'plamida yashirin tarafkashlik mavjud bo'lsa, modelning ob'ektiv ko'rinishi uning natijalari adolatli ekanini kafolatlamaydi.",
      "target_text": "If a dataset contains hidden bias, the model's appearance of objectivity does not guarantee that its outcomes are fair.",
      "words": [
        "If",
        "a",
        "dataset",
        "contains",
        "hidden",
        "bias",
        "the",
        "model's",
        "appearance",
        "of",
        "objectivity",
        "does",
        "not",
        "guarantee",
        "that",
        "its",
        "outcomes",
        "are",
        "fair"
      ],
      "topic": "AI Ethics"
    },
    {
      "source_text": "Tadqiqotchilar yangi texnologiyani keng joriy etishdan oldin uning turli ijtimoiy guruhlarga ta'sirini baholashlari zarur.",
      "target_text": "Researchers need to assess the technology's impact on different social groups before it is widely deployed.",
      "words": [
        "Researchers",
        "need",
        "to",
        "assess",
        "the",
        "technology's",
        "impact",
        "on",
        "different",
        "social",
        "groups",
        "before",
        "it",
        "is",
        "widely",
        "deployed"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya xarajatlarni kamaytirish maqsadida avtomatlashtirishni joriy qilgan bo'lsa-da, xodimlarni qayta tayyorlashga yetarli mablag' ajratmadi.",
      "target_text": "Although the company introduced automation to reduce costs, it failed to allocate enough funding for employee retraining.",
      "words": [
        "Although",
        "the",
        "company",
        "introduced",
        "automation",
        "to",
        "reduce",
        "costs",
        "it",
        "failed",
        "to",
        "allocate",
        "enough",
        "funding",
        "for",
        "employee",
        "retraining"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Sun'iy intellektning kelajakdagi roli uning texnik taraqqiyotidan tashqari, jamiyatning ishonch va tartibga solish masalalariga qanday javob berishiga ham bog'liq.",
      "target_text": "The future role of artificial intelligence will depend not only on technical progress but also on how society responds to questions of trust and regulation.",
      "words": [
        "The",
        "future",
        "role",
        "of",
        "artificial",
        "intelligence",
        "will",
        "depend",
        "not",
        "only",
        "on",
        "technical",
        "progress",
        "but",
        "also",
        "on",
        "how",
        "society",
        "responds",
        "to",
        "questions",
        "of",
        "trust",
        "and",
        "regulation"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Ushbu model real vaqt rejimida ishlashi uchun optimallashtirilgan bo'lsa-da, cheklangan qurilmalarda uning ishlash tezligi pasayishi mumkin.",
      "target_text": "Although the model has been optimized for real-time operation, its speed may decline on resource-constrained devices.",
      "words": [
        "Although",
        "the",
        "model",
        "has",
        "been",
        "optimized",
        "for",
        "real-time",
        "operation",
        "its",
        "speed",
        "may",
        "decline",
        "on",
        "resource-constrained",
        "devices"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Tadqiqot natijalarini ommaga taqdim etishda noaniqliklarni yashirish ilmiy muloqotga bo'lgan ishonchni susaytirishi mumkin.",
      "target_text": "Hiding uncertainties when presenting research findings to the public can undermine trust in scientific communication.",
      "words": [
        "Hiding",
        "uncertainties",
        "when",
        "presenting",
        "research",
        "findings",
        "to",
        "the",
        "public",
        "can",
        "undermine",
        "trust",
        "in",
        "scientific",
        "communication"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Bozorning tez o'zgarishi kompaniyalarni strategik rejalarni uzoq muddatga qat'iy belgilashdan ko'ra moslashuvchan yondashuvni tanlashga undamoqda.",
      "target_text": "Rapid market change is encouraging companies to adopt flexible approaches rather than rigid long-term strategic plans.",
      "words": [
        "Rapid",
        "market",
        "change",
        "is",
        "encouraging",
        "companies",
        "to",
        "adopt",
        "flexible",
        "approaches",
        "rather",
        "than",
        "rigid",
        "long-term",
        "strategic",
        "plans"
      ],
      "topic": "Business"
    },
    {
      "source_text": "O'zbekistonning yosh texnologik kompaniyalari xalqaro bozorga chiqishi uchun nafaqat innovatsion mahsulot, balki barqaror biznes modeli ham zarur.",
      "target_text": "For Uzbekistan's young technology companies to enter international markets, they need not only innovative products but also sustainable business models.",
      "words": [
        "For",
        "Uzbekistan's",
        "young",
        "technology",
        "companies",
        "to",
        "enter",
        "international",
        "markets",
        "they",
        "need",
        "not",
        "only",
        "innovative",
        "products",
        "but",
        "also",
        "sustainable",
        "business",
        "models"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Aniq qishloq xo'jaligi texnologiyalari rivojlangan sari fermerlar resurslardan foydalanishni dala sharoitiga qarab moslashtira oladi.",
      "target_text": "As precision agriculture technologies advance, farmers can adapt resource use to specific field conditions.",
      "words": [
        "As",
        "precision",
        "agriculture",
        "technologies",
        "advance",
        "farmers",
        "can",
        "adapt",
        "resource",
        "use",
        "to",
        "specific",
        "field",
        "conditions"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Agar sun'iy intellekt tomonidan berilgan tavsiyalar inson tomonidan tekshirilmasa, kichik xatolar ham keng ko'lamli qarorlarga ta'sir qilishi mumkin.",
      "target_text": "If AI-generated recommendations are not reviewed by humans, even minor errors can influence large-scale decisions.",
      "words": [
        "If",
        "AI-generated",
        "recommendations",
        "are",
        "not",
        "reviewed",
        "by",
        "humans",
        "even",
        "minor",
        "errors",
        "can",
        "influence",
        "large-scale",
        "decisions"
      ],
      "topic": "AI Ethics"
    },
    {
      "source_text": "Yangi materialning sanoatda qo'llanishi uning laboratoriyadagi natijalaridan ko'ra, uzoq muddatli barqarorligi va narxiga ko'proq bog'liq bo'lishi mumkin.",
      "target_text": "The industrial adoption of the new material may depend more on its long-term durability and cost than on its laboratory performance.",
      "words": [
        "The",
        "industrial",
        "adoption",
        "of",
        "the",
        "new",
        "material",
        "may",
        "depend",
        "more",
        "on",
        "its",
        "long-term",
        "durability",
        "and",
        "cost",
        "than",
        "on",
        "its",
        "laboratory",
        "performance"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Texnologiya odamlarning imkoniyatlarini kengaytirishi mumkin, biroq undan foydalanishdagi mas'uliyat ham shunga yarasha ortadi.",
      "target_text": "Technology can expand human capabilities, but the responsibility associated with its use increases accordingly.",
      "words": [
        "Technology",
        "can",
        "expand",
        "human",
        "capabilities",
        "but",
        "the",
        "responsibility",
        "associated",
        "with",
        "its",
        "use",
        "increases",
        "accordingly"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Kompaniya foydalanuvchi ma'lumotlarini yig'ishni ko'paytirar ekan, bu amaliyotning qonuniyligi bilan bir qatorda axloqiy chegaralari ham muhokama qilinishi kerak.",
      "target_text": "As the company collects more user data, the ethical boundaries of this practice should be discussed alongside its legality.",
      "words": [
        "As",
        "the",
        "company",
        "collects",
        "more",
        "user",
        "data",
        "the",
        "ethical",
        "boundaries",
        "of",
        "this",
        "practice",
        "should",
        "be",
        "discussed",
        "alongside",
        "its",
        "legality"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Ilmiy da'voning ishonchliligi u qanchalik jozibali ko'rinishiga emas, balki mustaqil dalillar bilan qay darajada qo'llab-quvvatlanishiga bog'liq.",
      "target_text": "The credibility of a scientific claim depends not on how appealing it appears but on how strongly it is supported by independent evidence.",
      "words": [
        "The",
        "credibility",
        "of",
        "a",
        "scientific",
        "claim",
        "depends",
        "not",
        "on",
        "how",
        "appealing",
        "it",
        "appears",
        "but",
        "on",
        "how",
        "strongly",
        "it",
        "is",
        "supported",
        "by",
        "independent",
        "evidence"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Tizimning ishlashini yaxshilash uchun faqat modelni murakkablashtirish emas, balki ma'lumotlar yig'ish jarayonini takomillashtirish ham muhim.",
      "target_text": "Improving a system's performance requires not only a more sophisticated model but also better data-collection processes.",
      "words": [
        "Improving",
        "a",
        "system's",
        "performance",
        "requires",
        "not",
        "only",
        "a",
        "more",
        "sophisticated",
        "model",
        "but",
        "also",
        "better",
        "data-collection",
        "processes"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Qaror qabul qiluvchilar qisqa muddatli ko'rsatkichlarga haddan tashqari e'tibor bersa, uzoq muddatli xavflarni ko'zdan qochirishlari mumkin.",
      "target_text": "If decision-makers focus excessively on short-term indicators, they may overlook long-term risks.",
      "words": [
        "If",
        "decision-makers",
        "focus",
        "excessively",
        "on",
        "short-term",
        "indicators",
        "they",
        "may",
        "overlook",
        "long-term",
        "risks"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Yangi texnologiya keng tarqalishidan oldin uning foydasi, xavfi va kutilmagan oqibatlari o'rtasida muvozanat topilishi kerak.",
      "target_text": "Before a new technology becomes widespread, a balance must be found between its benefits, risks, and unintended consequences.",
      "words": [
        "Before",
        "a",
        "new",
        "technology",
        "becomes",
        "widespread",
        "a",
        "balance",
        "must",
        "be",
        "found",
        "between",
        "its",
        "benefits",
        "risks",
        "and",
        "unintended",
        "consequences"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Ta'limda sun'iy intellektdan oqilona foydalanish o'quvchilarning mustaqil fikrlashini susaytirish o'rniga uni rivojlantirishi mumkin.",
      "target_text": "Used wisely, artificial intelligence in education can strengthen rather than weaken students' independent thinking.",
      "words": [
        "Used",
        "wisely",
        "artificial",
        "intelligence",
        "in",
        "education",
        "can",
        "strengthen",
        "rather",
        "than",
        "weaken",
        "students",
        "independent",
        "thinking"
      ],
      "topic": "Education"
    },
    {
      "source_text": "Tadqiqotchilar xulosalarini haddan tashqari umumlashtirmaslikka harakat qilishdi, chunki ularning ma'lumotlari faqat ma'lum bir hududni qamrab olgan edi.",
      "target_text": "The researchers avoided overgeneralizing their conclusions because their data covered only a specific region.",
      "words": [
        "The",
        "researchers",
        "avoided",
        "overgeneralizing",
        "their",
        "conclusions",
        "because",
        "their",
        "data",
        "covered",
        "only",
        "a",
        "specific",
        "region"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Iqtisodiy o'sish ekologik zarar hisobiga qo'lga kiritilsa, uning uzoq muddatli foydasi jiddiy savol ostida qoladi.",
      "target_text": "If economic growth is achieved at the expense of environmental damage, its long-term benefits become highly questionable.",
      "words": [
        "If",
        "economic",
        "growth",
        "is",
        "achieved",
        "at",
        "the",
        "expense",
        "of",
        "environmental",
        "damage",
        "its",
        "long-term",
        "benefits",
        "become",
        "highly",
        "questionable"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Kompaniya yangi mahsulotni ishlab chiqishda foydalanuvchilar bilan hamkorlik qilgani sababli, yakuniy yechim ularning ehtiyojlariga ancha mos tushdi.",
      "target_text": "Because the company collaborated with users during development, the final solution matched their needs much more closely.",
      "words": [
        "Because",
        "the",
        "company",
        "collaborated",
        "with",
        "users",
        "during",
        "development",
        "the",
        "final",
        "solution",
        "matched",
        "their",
        "needs",
        "much",
        "more",
        "closely"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Modelning bashoratlari qanchalik aniq ko'rinmasin, ularning ortidagi noaniqlikni tushunmasdan turib mas'uliyatli qaror qabul qilib bo'lmaydi.",
      "target_text": "No matter how accurate the model's predictions appear, responsible decisions cannot be made without understanding the uncertainty behind them.",
      "words": [
        "No",
        "matter",
        "how",
        "accurate",
        "the",
        "model's",
        "predictions",
        "appear",
        "responsible",
        "decisions",
        "cannot",
        "be",
        "made",
        "without",
        "understanding",
        "the",
        "uncertainty",
        "behind",
        "them"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Sun'iy intellekt tizimlari mustaqil ravishda qaror qabul qilishga qodir bo'lib borgani sari, inson nazoratining chegaralari yanada muhim masalaga aylanadi.",
      "target_text": "As AI systems become increasingly capable of making decisions autonomously, the limits of human oversight become an even more important issue.",
      "words": [
        "As",
        "AI",
        "systems",
        "become",
        "increasingly",
        "capable",
        "of",
        "making",
        "decisions",
        "autonomously",
        "the",
        "limits",
        "of",
        "human",
        "oversight",
        "become",
        "an",
        "even",
        "more",
        "important",
        "issue"
      ],
      "topic": "AI Ethics"
    },
    {
      "source_text": "Yangi energiya siyosati muvaffaqiyatli bo'lishi uchun texnik yechimlar bilan bir qatorda jamoatchilikning ishonchi ham zarur.",
      "target_text": "For the new energy policy to succeed, public trust is required alongside technical solutions.",
      "words": [
        "For",
        "the",
        "new",
        "energy",
        "policy",
        "to",
        "succeed",
        "public",
        "trust",
        "is",
        "required",
        "alongside",
        "technical",
        "solutions"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Tadqiqotda qo'llanilgan usul murakkab bo'lsa-da, uning asosiy tamoyillari boshqa sohalarga ham moslashtirilishi mumkin.",
      "target_text": "Although the method used in the study is complex, its underlying principles can be adapted to other fields.",
      "words": [
        "Although",
        "the",
        "method",
        "used",
        "in",
        "the",
        "study",
        "is",
        "complex",
        "its",
        "underlying",
        "principles",
        "can",
        "be",
        "adapted",
        "to",
        "other",
        "fields"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya inqiroz davrida xarajatlarni qisqartirishga majbur bo'ldi, biroq tadqiqot va rivojlantirish uchun ajratilgan mablag'ni saqlab qoldi.",
      "target_text": "The company was forced to cut costs during the crisis, but it preserved its investment in research and development.",
      "words": [
        "The",
        "company",
        "was",
        "forced",
        "to",
        "cut",
        "costs",
        "during",
        "the",
        "crisis",
        "but",
        "it",
        "preserved",
        "its",
        "investment",
        "in",
        "research",
        "and",
        "development"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Raqamli xizmatlar qanchalik qulay bo'lmasin, internetga kirish imkoniyati cheklangan odamlar uchun muqobil yo'llar ham mavjud bo'lishi kerak.",
      "target_text": "No matter how convenient digital services are, alternatives should remain available to people with limited internet access.",
      "words": [
        "No",
        "matter",
        "how",
        "convenient",
        "digital",
        "services",
        "are",
        "alternatives",
        "should",
        "remain",
        "available",
        "to",
        "people",
        "with",
        "limited",
        "internet",
        "access"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Iqlim prognozlaridagi noaniqlik harakat qilmaslik uchun sabab emas; aksincha, u moslashuvchan siyosat yuritish zarurligini ko'rsatadi.",
      "target_text": "Uncertainty in climate projections is not a reason for inaction; rather, it demonstrates the need for flexible policies.",
      "words": [
        "Uncertainty",
        "in",
        "climate",
        "projections",
        "is",
        "not",
        "a",
        "reason",
        "for",
        "inaction",
        "rather",
        "it",
        "demonstrates",
        "the",
        "need",
        "for",
        "flexible",
        "policies"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Yangi biznes modelining muvaffaqiyati mahsulotning o'zidan ko'ra, kompaniyaning mijozlar bilan uzoq muddatli munosabatlarni qanday qurishiga bog'liq bo'lishi mumkin.",
      "target_text": "The success of the new business model may depend less on the product itself than on how the company builds long-term relationships with customers.",
      "words": [
        "The",
        "success",
        "of",
        "the",
        "new",
        "business",
        "model",
        "may",
        "depend",
        "less",
        "on",
        "the",
        "product",
        "itself",
        "than",
        "on",
        "how",
        "the",
        "company",
        "builds",
        "long-term",
        "relationships",
        "with",
        "customers"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Sun'iy intellekt yordamida avtomatlashtirish inson mehnatini kamaytirishi mumkin, ammo uning o'rnini bosadigan yangi ko'nikmalarga bo'lgan ehtiyojni ham yuzaga keltiradi.",
      "target_text": "AI-driven automation can reduce human labor while also creating a need for new skills to replace those that become obsolete.",
      "words": [
        "AI-driven",
        "automation",
        "can",
        "reduce",
        "human",
        "labor",
        "while",
        "also",
        "creating",
        "a",
        "need",
        "for",
        "new",
        "skills",
        "to",
        "replace",
        "those",
        "that",
        "become",
        "obsolete"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Ilmiy tadqiqotlar bir martalik kashfiyotlardan ko'ra, natijalarni qayta-qayta tekshirish va takomillashtirish jarayoni sifatida qaralishi kerak.",
      "target_text": "Scientific research should be viewed as a process of repeatedly testing and refining results rather than as a series of isolated discoveries.",
      "words": [
        "Scientific",
        "research",
        "should",
        "be",
        "viewed",
        "as",
        "a",
        "process",
        "of",
        "repeatedly",
        "testing",
        "and",
        "refining",
        "results",
        "rather",
        "than",
        "as",
        "a",
        "series",
        "of",
        "isolated",
        "discoveries"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Agar texnologik innovatsiyalar teng taqsimlanmasa, raqamli taraqqiyot jamiyatdagi mavjud iqtisodiy tafovutlarni kamaytirish o'rniga kuchaytirishi mumkin.",
      "target_text": "If technological innovations are not distributed equitably, digital progress may deepen existing economic inequalities rather than reduce them.",
      "words": [
        "If",
        "technological",
        "innovations",
        "are",
        "not",
        "distributed",
        "equitably",
        "digital",
        "progress",
        "may",
        "deepen",
        "existing",
        "economic",
        "inequalities",
        "rather",
        "than",
        "reduce",
        "them"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Qishloq xo'jaligida real vaqt ma'lumotlaridan foydalanish qarorlarni tezlashtirishi mumkin, biroq noto'g'ri ma'lumot tezkor xatolarga ham olib keladi.",
      "target_text": "Using real-time data in agriculture can accelerate decisions, but inaccurate data can also lead to rapid mistakes.",
      "words": [
        "Using",
        "real-time",
        "data",
        "in",
        "agriculture",
        "can",
        "accelerate",
        "decisions",
        "but",
        "inaccurate",
        "data",
        "can",
        "also",
        "lead",
        "to",
        "rapid",
        "mistakes"
      ],
      "topic": "Agriculture"
    },
    {
      "source_text": "Tadqiqotchilar natijalarning boshqa hududlarda takrorlanishi ularning umumiy qo'llanilishini aniqlash uchun hal qiluvchi ahamiyatga ega ekanini qayd etdilar.",
      "target_text": "The researchers noted that reproducing the findings in other regions would be crucial for determining their broader applicability.",
      "words": [
        "The",
        "researchers",
        "noted",
        "that",
        "reproducing",
        "the",
        "findings",
        "in",
        "other",
        "regions",
        "would",
        "be",
        "crucial",
        "for",
        "determining",
        "their",
        "broader",
        "applicability"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya axloqiy xavflarni oldindan baholaganida, keyinchalik yuzaga kelgan ishonch inqirozining oldini olish mumkin bo'lardi.",
      "target_text": "Had the company assessed the ethical risks in advance, it might have prevented the trust crisis that emerged later.",
      "words": [
        "Had",
        "the",
        "company",
        "assessed",
        "the",
        "ethical",
        "risks",
        "in",
        "advance",
        "it",
        "might",
        "have",
        "prevented",
        "the",
        "trust",
        "crisis",
        "that",
        "emerged",
        "later"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Texnologik qarorlar qabul qilinayotganda samaradorlik bilan bir qatorda shaffoflik, xavfsizlik va adolat ham asosiy mezon bo'lishi kerak.",
      "target_text": "When technological decisions are made, transparency, security, and fairness should be core criteria alongside efficiency.",
      "words": [
        "When",
        "technological",
        "decisions",
        "are",
        "made",
        "transparency",
        "security",
        "and",
        "fairness",
        "should",
        "be",
        "core",
        "criteria",
        "alongside",
        "efficiency"
      ],
      "topic": "AI Ethics"
    },
    {
      "source_text": "Yangi tadqiqot muammoni hal qilishdan tashqari, kelajakdagi tadqiqotlar uchun bir qator muhim savollarni ham ochib berdi.",
      "target_text": "Beyond addressing the problem, the new study also raised several important questions for future research.",
      "words": [
        "Beyond",
        "addressing",
        "the",
        "problem",
        "the",
        "new",
        "study",
        "also",
        "raised",
        "several",
        "important",
        "questions",
        "for",
        "future",
        "research"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Ushbu yondashuvning afzalligi shundaki, u murakkab jarayonni soddalashtiradi, lekin muhim tafsilotlarni yo'qotib qo'ymaslikni talab qiladi.",
      "target_text": "The advantage of this approach is that it simplifies a complex process while requiring care not to lose important details.",
      "words": [
        "The",
        "advantage",
        "of",
        "this",
        "approach",
        "is",
        "that",
        "it",
        "simplifies",
        "a",
        "complex",
        "process",
        "while",
        "requiring",
        "care",
        "not",
        "to",
        "lose",
        "important",
        "details"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Kompaniyalar sun'iy intellektni joriy etishda texnik tayyorgarlikdan tashqari, xodimlarning o'zgarishga tayyorligini ham hisobga olishlari lozim.",
      "target_text": "When adopting AI, companies should consider not only technical readiness but also employees' readiness for change.",
      "words": [
        "When",
        "adopting",
        "AI",
        "companies",
        "should",
        "consider",
        "not",
        "only",
        "technical",
        "readiness",
        "but",
        "also",
        "employees",
        "readiness",
        "for",
        "change"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Raqamli texnologiyalar orqali xizmat ko'rsatish tezlashgan bo'lsa-da, insoniy muloqotning ayrim jihatlarini avtomatlashtirish qiyinligicha qolmoqda.",
      "target_text": "Although digital technologies have accelerated service delivery, some aspects of human interaction remain difficult to automate.",
      "words": [
        "Although",
        "digital",
        "technologies",
        "have",
        "accelerated",
        "service",
        "delivery",
        "some",
        "aspects",
        "of",
        "human",
        "interaction",
        "remain",
        "difficult",
        "to",
        "automate"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "O'zbekistonda sun'iy intellekt ekotizimi rivojlanishi uchun ta'lim, infratuzilma va biznes o'rtasidagi hamkorlik izchil kuchaytirilishi kerak.",
      "target_text": "For Uzbekistan's AI ecosystem to develop, cooperation among education, infrastructure, and business needs to be strengthened consistently.",
      "words": [
        "For",
        "Uzbekistan's",
        "AI",
        "ecosystem",
        "to",
        "develop",
        "cooperation",
        "among",
        "education",
        "infrastructure",
        "and",
        "business",
        "needs",
        "to",
        "be",
        "strengthened",
        "consistently"
      ],
      "topic": "Uzbekistan"
    },
    {
      "source_text": "Qaysi model eng yaxshi ekanini faqat bitta ko'rsatkich asosida aniqlash noto'g'ri, chunki turli mezonlar bir-biriga zid natijalar berishi mumkin.",
      "target_text": "It is misleading to determine which model is best using a single metric, since different criteria can produce conflicting results.",
      "words": [
        "It",
        "is",
        "misleading",
        "to",
        "determine",
        "which",
        "model",
        "is",
        "best",
        "using",
        "a",
        "single",
        "metric",
        "since",
        "different",
        "criteria",
        "can",
        "produce",
        "conflicting",
        "results"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Tadqiqotchilar yangi nazariya ilgari tushuntirib bo'lmaydigan kuzatuvlarni izohlashga imkon berishini ko'rsatdilar.",
      "target_text": "The researchers showed that the new theory could account for observations that had previously been difficult to explain.",
      "words": [
        "The",
        "researchers",
        "showed",
        "that",
        "the",
        "new",
        "theory",
        "could",
        "account",
        "for",
        "observations",
        "that",
        "had",
        "previously",
        "been",
        "difficult",
        "to",
        "explain"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Iqtisodiy barqarorlikni ta'minlash uchun hukumatlar innovatsiyani rag'batlantirish bilan birga moliyaviy xavflarni ham nazorat qilishi kerak.",
      "target_text": "To ensure economic stability, governments must encourage innovation while also controlling financial risks.",
      "words": [
        "To",
        "ensure",
        "economic",
        "stability",
        "governments",
        "must",
        "encourage",
        "innovation",
        "while",
        "also",
        "controlling",
        "financial",
        "risks"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Sun'iy intellektdan foydalanish kengaygani sari, odamlar tomonidan berilgan topshiriqlarning sifati ham tizim natijalarining muhim omiliga aylanadi.",
      "target_text": "As the use of AI expands, the quality of human instructions will also become an important factor in system outcomes.",
      "words": [
        "As",
        "the",
        "use",
        "of",
        "AI",
        "expands",
        "the",
        "quality",
        "of",
        "human",
        "instructions",
        "will",
        "also",
        "become",
        "an",
        "important",
        "factor",
        "in",
        "system",
        "outcomes"
      ],
      "topic": "AI News"
    },
    {
      "source_text": "Ekologik siyosatning samaradorligi faqat yangi qonunlarning mavjudligiga emas, balki ularning amalda qanday bajarilishiga bog'liq.",
      "target_text": "The effectiveness of environmental policy depends not merely on the existence of new laws but on how they are implemented in practice.",
      "words": [
        "The",
        "effectiveness",
        "of",
        "environmental",
        "policy",
        "depends",
        "not",
        "merely",
        "on",
        "the",
        "existence",
        "of",
        "new",
        "laws",
        "but",
        "on",
        "how",
        "they",
        "are",
        "implemented",
        "in",
        "practice"
      ],
      "topic": "Environment"
    },
    {
      "source_text": "Tadqiqot guruhining xulosalari dastlabki gipotezaga zid bo'lgan bo'lsa-da, ular keyingi izlanishlar uchun yanada qiziqarli yo'nalish yaratdi.",
      "target_text": "Although the research group's conclusions contradicted the initial hypothesis, they opened up a more interesting direction for further investigation.",
      "words": [
        "Although",
        "the",
        "research",
        "group's",
        "conclusions",
        "contradicted",
        "the",
        "initial",
        "hypothesis",
        "they",
        "opened",
        "up",
        "a",
        "more",
        "interesting",
        "direction",
        "for",
        "further",
        "investigation"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya innovatsion mahsulot yaratgan bo'lsa ham, uni bozorga to'g'ri joylashtira olmagani sababli kutilgan natijaga erisha olmadi.",
      "target_text": "Despite creating an innovative product, the company failed to achieve the expected result because it could not position it effectively in the market.",
      "words": [
        "Despite",
        "creating",
        "an",
        "innovative",
        "product",
        "the",
        "company",
        "failed",
        "to",
        "achieve",
        "the",
        "expected",
        "result",
        "because",
        "it",
        "could",
        "not",
        "position",
        "it",
        "effectively",
        "in",
        "the",
        "market"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Texnologiya rivojlanishini to'xtatib bo'lmaydi, ammo uning qaysi yo'nalishda rivojlanishini jamiyatning tanlovlari ma'lum darajada belgilashi mumkin.",
      "target_text": "Technological development cannot be stopped, but society's choices can influence the direction in which it evolves.",
      "words": [
        "Technological",
        "development",
        "cannot",
        "be",
        "stopped",
        "but",
        "society's",
        "choices",
        "can",
        "influence",
        "the",
        "direction",
        "in",
        "which",
        "it",
        "evolves"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Agar ma'lumotlar yig'ilish jarayonida xatolar e'tibordan chetda qolsa, keyingi tahlil qanchalik murakkab bo'lmasin, ishonchli xulosa chiqarish qiyin.",
      "target_text": "If errors are overlooked during data collection, no matter how sophisticated the subsequent analysis is, reliable conclusions will be difficult to draw.",
      "words": [
        "If",
        "errors",
        "are",
        "overlooked",
        "during",
        "data",
        "collection",
        "no",
        "matter",
        "how",
        "sophisticated",
        "the",
        "subsequent",
        "analysis",
        "is",
        "reliable",
        "conclusions",
        "will",
        "be",
        "difficult",
        "to",
        "draw"
      ],
      "topic": "Data Science"
    },
    {
      "source_text": "Yangi texnologiyaning afzalliklari aniq ko'rinsa-da, uning kutilmagan oqibatlarini oldindan to'liq baholash deyarli imkonsiz.",
      "target_text": "Although the benefits of the new technology are apparent, it is almost impossible to anticipate all of its unintended consequences.",
      "words": [
        "Although",
        "the",
        "benefits",
        "of",
        "the",
        "new",
        "technology",
        "are",
        "apparent",
        "it",
        "is",
        "almost",
        "impossible",
        "to",
        "anticipate",
        "all",
        "of",
        "its",
        "unintended",
        "consequences"
      ],
      "topic": "Technology"
    },
    {
      "source_text": "Tadqiqotchilar o'z xulosalarini ehtiyotkorlik bilan ifodalashdi, chunki mavjud dalillar qat'iy sababiy bog'liqlikni isbotlash uchun yetarli emas edi.",
      "target_text": "The researchers expressed their conclusions cautiously because the available evidence was insufficient to establish a definitive causal relationship.",
      "words": [
        "The",
        "researchers",
        "expressed",
        "their",
        "conclusions",
        "cautiously",
        "because",
        "the",
        "available",
        "evidence",
        "was",
        "insufficient",
        "to",
        "establish",
        "a",
        "definitive",
        "causal",
        "relationship"
      ],
      "topic": "Science"
    },
    {
      "source_text": "Kompaniya barqaror o'sishni ta'minlamoqchi bo'lsa, qisqa muddatli daromadni oshirishdan ko'ra innovatsiya va mijozlar ishonchiga sarmoya kiritishi kerak.",
      "target_text": "If the company wants to ensure sustainable growth, it should invest in innovation and customer trust rather than simply maximizing short-term revenue.",
      "words": [
        "If",
        "the",
        "company",
        "wants",
        "to",
        "ensure",
        "sustainable",
        "growth",
        "it",
        "should",
        "invest",
        "in",
        "innovation",
        "and",
        "customer",
        "trust",
        "rather",
        "than",
        "simply",
        "maximizing",
        "short-term",
        "revenue"
      ],
      "topic": "Business"
    },
    {
      "source_text": "Sun'iy intellekt tizimlari qanchalik rivojlangan bo'lmasin, yakuniy qarorning insoniy va ijtimoiy oqibatlari uchun javobgarlik masalasi ochiq qoladi.",
      "target_text": "However advanced AI systems become, the question of responsibility for the human and social consequences of final decisions remains open.",
      "words": [
        "However",
        "advanced",
        "AI",
        "systems",
        "become",
        "the",
        "question",
        "of",
        "responsibility",
        "for",
        "the",
        "human",
        "and",
        "social",
        "consequences",
        "of",
        "final",
        "decisions",
        "remains",
        "open"
      ],
      "topic": "AI Ethics"
    }
  ]
}
