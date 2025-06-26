# 🔹 1. Random Joke Generator
# 📌 Use the Official Joke API
# 🧾 Fetch a random joke and print:
# "Why don't scientists trust atoms? — Because they make up everything!"



import requests

API = "https://official-joke-api.appspot.com/random_joke"

try: 
    response = requests.get(API)
    if response.status_code == 200:
        data = response.json()
        setup = data.get("setup")
        punchline = data.get("punchline")
        print(f"Joke: {setup}\n{punchline}")

    else:
        print("Failed to fetch data! Status Code:", response.status_code)

except Exception as e:
    print(f"Error fetching data:{e}")