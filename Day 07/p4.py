# 🔹 4. Email Cleaner
# Write a function clean_email(email) that:
# Strips leading/trailing spaces
# Converts to lowercase
# Removes spaces inside the string
# Return the cleaned email. Then print it.





email = input("Enter your email to get cleaned version of it: ")

def  clean_email(email):
    cleaned_email = email.strip().lower().replace(" ", "")
    return cleaned_email


print(clean_email(email))