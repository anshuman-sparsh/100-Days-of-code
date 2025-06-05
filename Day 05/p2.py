# 🔹 2. Remove Vowels from Sentence
# Take a sentence input
# Remove all vowels (a, e, i, o, u) from it
# Print the new sentence
# Use .replace() inside a loop




sentence = input("Enter a sentence: ")
vowels = "a", "e", "i", "o", "u"
for vowel in vowels:
    sentence = sentence.replace(vowel, "")
print(sentence)