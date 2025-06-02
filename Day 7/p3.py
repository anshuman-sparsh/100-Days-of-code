# 🔹 3. Word Length Filter
# Write a function filter_words(sentence) that:
# Takes a sentence
# Prints only the words longer than 4 characters
# Use .split() and a loop



sentence = input("Enter a sentence to filter out: ")

def filter_words(sentence):
    
    filter_sentence = sentence.split()
    for word in filter_sentence:
        if len(word)>4 :
            print(word)
        
filter_words(sentence)