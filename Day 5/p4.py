# 🔹 4. Common Words Checker
# Take 2 sentences as input
# Find and print the words that are common in both
# Use .split() and loop with conditionals





sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

words1 = sentence1.split()
words2 = sentence2.split()

common_words = []

for word in words2:
    if word in words1 and word not in common_words:
        common_words.append(word)


if len(common_words) > 0:
    print(f"Common words: {common_words}")

else:
    print("No common words.")