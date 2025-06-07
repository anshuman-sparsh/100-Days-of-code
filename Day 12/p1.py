# 🔹 1.
# Create a function that returns a dictionary mapping each word in a sentence to its length.



sentence_input = input("Enter a sentence: ").strip()


def word_length(sentence_input):
    sentence = sentence_input.split()
    word_dict = {}
    for word in sentence:
        word_dict[word] = len(word)
    return word_dict

print(word_length(sentence_input))