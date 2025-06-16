# 🔹 5.
# Call a fake API (https://invalid.api) and handle the error gracefully using try/except.




import requests

url = "https://invalid.api"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("API call succeeded!")
        print(response.json())
    else:
        print(f"Failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("An error occurred while calling the API.")
    print("Error details:", e)
