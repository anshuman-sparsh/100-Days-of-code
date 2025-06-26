# 🔹 5. IP Address Lookup
# 📌 Use IP API → http://ip-api.com/json/
# 🧾 Show your city, country, and ISP using your own IP.



import requests

def get_ip_info():
    api = "http://ip-api.com/json/"

    try:
        response = requests.get(api)
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'success':
            print("\nIP Address Lookup:\n")
            print(f"IP Address: {data.get('query', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"Region: {data.get('regionName', 'N/A')}")
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
        else:
            print("Failed to retrieve IP information.")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


get_ip_info()
