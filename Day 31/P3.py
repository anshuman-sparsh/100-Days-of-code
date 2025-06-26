# 🔹 3. NASA Astronomy Picture of the Day (APOD)
# 📌 Use https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
# 🧾 Print the title, date, and explanation.
# Use NASA's demo key for free requests.




import requests

API = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

try: 
    response = requests.get(API)
    if response.status_code == 200:
        data = response.json()
        date = data.get("date")
        explanation = data.get("explanation")
        url = data.get("hdurl")
        title = data.get("title")
        print(f"Image Details:\n\nTitle: {title}\n\nDate: {date}\n\nExplanation: {explanation}\n\nHD url: {url}\n")

    else:
        print("Failed to fetch data! Status Code:", response.status_code)

except Exception as e:
    print(f"Error fetching data:{e}")