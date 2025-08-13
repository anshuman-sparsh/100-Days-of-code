import random

def get_mock_weather(city_name):
    possible_conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Partly Cloudy", "Stormy", "Clear"]
    
    temperature = random.randint(-5, 40)
    condition = random.choice(possible_conditions)
    
    return temperature, condition

def main():
    print("--- Mock Weather Report ---")
    city = input("Enter a city name: ")
    
    if city:
        temp, cond = get_mock_weather(city)
        print(f"Current weather in {city.title()}: {temp}°C, {cond}")
    else:
        print("City name cannot be empty.")

if __name__ == "__main__":
    main()