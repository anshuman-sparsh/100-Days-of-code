import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not API_KEY:
        print("API Key not found!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unable to fetch weather.')}")
            return

        
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        city_name = data["name"]

        
        print(f"\n Weather in {city_name}:")
        print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network Error: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_weather(city)
