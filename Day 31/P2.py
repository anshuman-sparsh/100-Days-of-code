# 🔹 2. Bitcoin Price Checker
# 📌 Use CoinDesk API
# 🧾 Fetch current BTC price in INR and display:
# Current Bitcoin Price in INR: ₹XXXXXX


import requests

API = "https://api.coinbase.com/v2/prices/BTC-INR/spot"


try:  
    response = requests.get(API)
    if response.status_code == 200:
        data = response.json()
        price = float(data["data"]["amount"])
        print(f"Current Bitcoin Price in INR: ₹{price:.4f}")

    else:  
        print("Couldn't fetch data!")

except Exception as e:
    print(f"Error: {e}")