# 🔹 5. Weather Bot 
# Create weather_bot.py:
# WeatherBot class with city as attribute
# Use CLI input --city
# Print mock weather based on city:
# Use dictionary inside the class for random mappings:
# Delhi → “Hot”
# Shimla → “Cold”
# Mumbai → “Humid”


import argparse

class WeatherBot:
    def __init__(self, city):
        self.city = city
        self.weather_data = {
            "Delhi": "Hot",
            "Shimla": "Cold",
            "Mumbai": "Humid",
            "Bangalore": "Pleasant",
            "Kolkata": "Rainy"
        }

    def get_weather(self):
        weather = self.weather_data.get(self.city, "Weather data not available")
        print(f"Weather in {self.city}: {weather}")

parser = argparse.ArgumentParser(description="Simple Weather Bot")
parser.add_argument("--city", type=str, required=True, help="Enter city name")
args = parser.parse_args()

bot = WeatherBot(args.city)
bot.get_weather()
# python "Day 27/weather_bot.py" --city Delhi
