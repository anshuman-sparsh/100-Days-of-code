# 🔹 5.
# Create a new module string_utils.py with a function to:
# Count vowels in a word
# Return word length
# Use it in main_vowel.py as well.



with open("Day 19/string_utils.py", "w") as f:
    f.write('''def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def word_length(word):
    return len(word)
''')

with open("Day 19/main_vowel.py", "w") as f:
    f.write('''from string_utils import count_vowels, word_length

word = input("Enter a word: ").strip()

print(f"Vowel count: {count_vowels(word)}")
print(f"Word length: {word_length(word)}")
''')
