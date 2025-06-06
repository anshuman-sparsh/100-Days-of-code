# 🔹 2.
# Create a function that returns only the words longer than 5 characters from a list of strings.




list_of_strings = input("Enter a sentence: ")



def word_filter(list_of_strings):
    result_list =[]
    words = list_of_strings.split()
    for word in words:
        if len(word) > 5:
            result_list.append(word)
    return result_list
print(word_filter(list_of_strings))