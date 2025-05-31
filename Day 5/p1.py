# 1. Word Frequency Counter
# Ask the user for a sentence
# Split it into words
# Count how many times each word appears
# Print result like:
# the → 2 times  
# dog → 1 time  
# runs → 1 time





sentence = input("Enter a sentence: ")
words = sentence.split()

word_counts = {}
# Loop through each word and count its frequency
for word in words:
    # Update count: get current count (default 0) and add 1
    word_counts[word] = word_counts.get(word, 0) + 1

# Print each word and its count in the format "word → count times"
for word in word_counts:
    print(f"{word} → {word_counts[word]} times")