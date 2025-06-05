# 🔹 1. Sentence Word Reverser
# Take a sentence as input
# Reverse each word in place (not the order of words)
# "hello world" → "olleh dlrow"
# Use .split(), slicing, .join()




sentence = input("Enter a sentence: ").strip()
words = sentence.split()

reversed_words = []
for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

result = " ".join(reversed_words)
print("Result: ", result)