import requests
import time

API_KEY = "b952f050310233022ef7549355812583"  # ← Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def convert_c_to_f(temp_c):
    """Convert Celsius to Fahrenheit"""
    return round((temp_c * 9/5) + 32, 2)

def get_weather(city_country):
    """Fetch and format weather data"""
    params = {"q": city_country, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("cod") == 200:
        weather = data["weather"][0]["description"]
        temp_c = data["main"]["temp"]
        temp_f = convert_c_to_f(temp_c)
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"\n📍 Location: {city_country.title()}"
            f"\n🌤️ Weather: {weather}"
            f"\n🌡️ Temperature: {temp_c}°C / {temp_f}°F"
            f"\n💧 Humidity: {humidity}%"
            f"\n💨 Wind Speed: {wind} m/s\n"
        )

        # Log to file
        with open("weather_history.txt", "a") as file:
            file.write(f"{time.ctime()} - {city_country.title()}: {weather}, {temp_c}°C\n")

        return result
    else:
        return f"❌ Error: {data.get('message', 'Unknown error')}"

# Interactive loop
if __name__ == "__main__":
    print("🌦️ Welcome to the Weather App with Country Code + Fahrenheit!")
    print("Use format: City,Country_Code (e.g., Mumbai,IN or New York,US)")
    print("Type 'exit' to quit.\n")

    while True:
        city = input("Enter city and country code: ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye! Your weather searches were saved in 'weather_history.txt'.")
            break

        result = get_weather(city)
        print(result)
