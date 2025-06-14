from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str.strip(), "%Y-%m-%d")
    today = datetime.now()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
