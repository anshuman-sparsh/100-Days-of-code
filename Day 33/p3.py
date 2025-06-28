# 🔹 3. Word Cleaner & Counter (Keep this one as it is)
# 📌 Ask for a sentence, clean special characters (@$#), count words.
# ✅ Use clean_sentence(text) and count_words(text)



def clean_sentence(sentence):
    special_chars = "@#$%^&*()[]{};:,./<>?|`~=_+"
    cleaned = ""
    for char in sentence:
        if char not in special_chars:
            cleaned += char
    return cleaned

def count_words(cleaned):
    words = cleaned.split()
    return len(words)

sentence = input("Enter a sentence: ")
cleaned = clean_sentence(sentence)
word_count = count_words(cleaned)

print(f"\nCleaned Sentence: {cleaned}")
print(f"Word Count: {word_count}")
