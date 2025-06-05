# 🔹 3. Custom Joiner
# Ask user to input 3–5 words
# Join them with - in between (like: word1-word2-word3)
# Use .join()
# Bonus: Let user choose the joining symbol too!



separator = input("Enter joining symbol (e.g., -, *, #): ")
if separator == "":
    separator = "-"


words = []
num_words = int(input("How many words (3-5)? "))
if num_words < 3 or num_words > 5:
      print(f"Please enter between 3 and 5 words. Default is 3: ")
      num_words=3



for i in range(num_words):
     word = input(f"Enter word {i+1}: ")
     if word != "":
        words.append(word)


result = separator.join(words)
print("Result:", result)