# 🔹 1. Vowel Counter
# Write a program that:
# Takes a string as input
# Counts and prints the number of vowels (a, e, i, o, u) in it
# Ignores case




word = input("Enter a Word: ")
vowels = "aeiouAEIOU"
vowels_count = 0

for char in word:
    if char in vowels:
        vowels_count += 1


print("No of vowels found:", vowels_count)
