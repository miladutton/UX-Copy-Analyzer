
import re
from textblob import TextBlob

VAGUE_WORDS = {"thing", "stuff", "nice", "some", "good", "bad", "maybe", "possibly", "very"}

def find_vague_words(text):
    blob = TextBlob(text)
    return [w for w in blob.words if w.lower() in VAGUE_WORDS]

def count_passive_phrases(text):
    return len(re.findall(r"\b(is|was|were|be|been|being)\b\s+\w+ed", text.lower()))
