# Practice_3 : String Tools

# Input a string

# Print: reversed string, number of vowels, and capitalized version



Input = input("Enter a Word: ")

reversed_text = Input[::-1]
print(f"Reversed String: {reversed_text}")



vowel_count = sum(char in "aeiouAEIOU" for char in Input )
print(f"No of vowels: {vowel_count}")


upper_case = Input.upper()
print("Title Case(each word): ", upper_case)



title_case = Input.title()
print("Title Case(each word): ", title_case)

