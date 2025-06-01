# 🔹 2. Notes Cleaner
# Ask user to enter a sentence that might contain extra spaces and special characters
# Remove leading/trailing spaces, and replace @, $, # with empty space
# Use .strip() and .replace() multiple times






sentence = input("Enter a sentence: ").strip()

clean_sentence = sentence.strip()
clean_sentence = clean_sentence.replace("@", " ")
clean_sentence = clean_sentence.replace("#", " ")
clean_sentence = clean_sentence.replace("$", " ")
print(clean_sentence)