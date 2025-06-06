# 🔹 4.
# Create a function that finds and returns all duplicate elements in a list.



input_lists = input("Enter all elements to filter all duplicate ones: ")
input_list = input_lists.split()

def find_duplicates(input_list):
    duplicates = []
    seen = []
    
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    
    return duplicates


print("Duplicate elements:", find_duplicates(input_list))