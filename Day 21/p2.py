# 🔹 2.
# Use https://api.agify.io/?name=YOURNAME
# Print the predicted age for a given name.



import requests

url = f"https://api.agify.io/?name=anshuman"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Predicted Age for {data['name'].capitalize()}: {data['age']} years")
        print(data)
    else:
        print("Failed to fetch data.")
except Exception as e:
    print("Error:", e)
