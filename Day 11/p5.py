# 🔹 5.
# Write a function that takes a list of names and returns the ones that start with a vowel.



names = input("Enter names here: ")
names_list = names.split()


def starts_with_vowel(names):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for name in names:
        if len(name) > 0:
            first_letter = name[0].lower()
            for vowel in vowels:
                if first_letter == vowel:
                    result.append(name)
                    break
    return result

print(starts_with_vowel(names_list))