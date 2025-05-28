
from .metrics import get_sentiment, get_readability
from .flags import find_vague_words, count_passive_phrases

def analyze(text: str) -> dict:
    sentiment = get_sentiment(text)
    readability = get_readability(text)
    vague_words = find_vague_words(text)
    passive_count = count_passive_phrases(text)

    return {
        "text": text.strip(),
        **sentiment,
        **readability,
        "vague_words": vague_words,
        "passive_phrases": passive_count,
    }
