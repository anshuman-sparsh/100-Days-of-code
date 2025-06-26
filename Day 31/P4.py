# 🔹 4. Country Info Finder
# 📌 Use REST Countries API → https://restcountries.com/v3.1/name/india
# 🧾 Input a country name, print capital, region, population, and currency.



import requests

def get_country_info(country_name):
    API = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(API)
        data = response.json()
        country = data[0]

        name = country.get("name", {}).get("common", "N/A")
        capital = country.get("capital", ["N/A"])[0]
        region = country.get("region", "N/A")
        population = country.get("population", "N/A")

        currencies = country.get("currencies", {})
        currency_info = list(currencies.values())[0]
        currency_name = currency_info.get("name", "N/A")
        currency_symbol = currency_info.get("symbol", "N/A")

        print("\nCountry Info:")
        print(f"Country: {name}")
        print(f"Capital: {capital}")
        print(f"Region: {region}")
        print(f"Population: {population}")
        print(f"Currency: {currency_name} ({currency_symbol})")

    except requests.exceptions.HTTPError:
        print("Invalid country name or API error.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


country_name = input("Enter a country name: ")
get_country_info(country_name.strip())