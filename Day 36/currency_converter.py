import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")

def convert_currency(amount, from_curr, to_curr):
    url = "https://api.exchangerate.host/live"
    params = {
        "access_key": API_KEY,
        "source": from_curr.upper(),
        "currencies": to_curr.upper(),
        "format": 1
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("success"):
            rate_key = from_curr.upper() + to_curr.upper()
            rate = data["quotes"].get(rate_key)
            if rate:
                converted = amount * rate
                print(f"\n{amount} {from_curr.upper()} = {converted:.2f} {to_curr.upper()}")
            else:
                print("❌ Rate not found.")
        else:
            print("❌ API error:", data.get("error", {}).get("info", "Unknown error."))

    except Exception as e:
        print("❌ Error occurred:", e)

if __name__ == "__main__":
    print("🌍 Currency Converter CLI")

    try:
        amt = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ")
        to_currency = input("To currency (e.g., INR): ")

        convert_currency(amt, from_currency, to_currency)

    except ValueError:
        print("❌ Please enter a valid number for amount.")
