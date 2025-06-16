# 🔹 1.
# Fetch your GitHub profile data using:
# https://api.github.com/users/anshuman-sparsh
# Print your name, public repos, and followers.


import requests

url = "https://api.github.com/users/anshuman-sparsh"

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Name:", data.get("name"))
        print("Public Repositories:", data.get("public_repos"))
        print("Followers:", data.get("followers"))
    else:
        print("Failed to fetch data! Status Code:", response.status_code)

except Exception as e:
    print("Error fetching data:", e)