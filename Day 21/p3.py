# 🔹 3.
# Use https://api.coindesk.com/v1/bpi/currentprice.json
# Print current Bitcoin price in USD.


import requests

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        amount = data["data"]["amount"]        
        currency = data["data"]["currency"] 
        print(f"BTC Price: {amount} {currency}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Network error occurred:", e)