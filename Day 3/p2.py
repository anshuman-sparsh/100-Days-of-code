# 🔹 2. Reverse Words
# Ask the user to enter a sentence.
# Print the sentence with words in reverse order.
# Example: "I love coding" → "coding love I"





sentence = input("Enter your sentence: ")
words = sentence.split()
reversed_sentence = ' '.join(words[::-1])
print(reversed_sentence)