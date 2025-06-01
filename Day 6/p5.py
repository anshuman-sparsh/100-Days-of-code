# 🔹 5. Word Counter (Basic Version)
# Ask for a sentence
# Count how many words are in it
# Print total words and total characters (excluding spaces)





sentence = input("Enter a sentence: ")
words = sentence.split()
count_words = len(words)

chars = sentence.replace(" ", "")
char_count = len(chars)

print(f"Total Words: {count_words}, Total Characters: {char_count}")