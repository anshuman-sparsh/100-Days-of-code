input = input("Enter the sentence:- ")

words = input.lower().split()

word_count = {word: words.count(word) for word in set(words)}

print("Word frequency:", word_count)
