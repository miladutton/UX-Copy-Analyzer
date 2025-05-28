
from textblob import TextBlob
import textstat

def get_sentiment(text):
    blob = TextBlob(text)
    return {
        "char_count": len(text),
        "word_count": len(blob.words),
        "polarity": round(blob.sentiment.polarity, 2),
        "subjectivity": round(blob.sentiment.subjectivity, 2),
    }

def get_readability(text):
    return {
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
        "flesch_reading_ease": textstat.flesch_reading_ease(text)
    }
