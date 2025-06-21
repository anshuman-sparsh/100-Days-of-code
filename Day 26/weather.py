# 🔹 5. Weather Tool (Mock)
# Take a --city argument and pretend to fetch weather (just print a random weather status like "Sunny in Delhi").





import argparse
import random

parser = argparse.ArgumentParser(description="Mock Weather Reporter")
parser.add_argument("--city", required=True, help="City to get weather for")

args = parser.parse_args()
city = args.city

weather_options = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy", "Foggy", "Snowy"]
current_weather = random.choice(weather_options)

print(f"Weather in {city}: {current_weather}")

# python "Day 26/weather.py" --city Patna