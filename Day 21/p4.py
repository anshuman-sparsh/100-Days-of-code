# 🔹 4.
# Use https://dog.ceo/api/breeds/image/random
# Print a random dog image URL (or open it with webbrowser).



import requests
import webbrowser

url = "https://dog.ceo/api/breeds/image/random"

try:
    response = requests.get(url, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]  # Image URL Terminal me hai.
        print("Random Dog Image:", image_url)
        webbrowser.open(image_url) # Image will open in browser.
    else:
        print("Failed to fetch dog image. Status:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)
