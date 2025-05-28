
def print_report(result):
    print("\n🧠 UX COPY ANALYSIS")
    print("-" * 40)
    print(f"📝 Text: {result['text']}")
    print(f"🔤 Characters: {result['char_count']} | 🧾 Words: {result['word_count']}")
    print(f"📈 Tone: Polarity = {result['polarity']} | Subjectivity = {result['subjectivity']}")
    print(f"📚 Flesch-Kincaid Grade: {result['flesch_kincaid_grade']:.1f}")
    print(f"✅ Readability Score: {result['flesch_reading_ease']:.1f}")
    print(f"🚫 Passive Phrases: {result['passive_phrases']}")
    print(f"⚠️ Vague Words: {', '.join(result['vague_words']) if result['vague_words'] else 'None'}")
    print("-" * 40)
