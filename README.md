# 🌦️ Weather App - Beginner Python Project

This is a **beginner-friendly Python Weather App** that fetches live weather data using the [OpenWeatherMap API](https://openweathermap.org/api).

Simply enter a **city and country code** (e.g., `London,UK`), and the app displays:
- Current weather conditions
- Temperature (in °C and °F)
- Humidity
- Wind speed  
It also logs each search to a file (`weather_history.txt`) for future reference.

---

## 🚀 Features

✅ Input city & country (e.g., `Mumbai,IN`)  
✅ Live weather data from OpenWeatherMap  
✅ Temperature in **Celsius & Fahrenheit**  
✅ Humidity and wind speed  
✅ Search history saved to file  
✅ Graceful error handling (invalid city, API errors)  
✅ Loop runs until user exits  
✅ Unit-tested temperature conversion function  
✅ `.exe` file built using PyInstaller

---

## 🧠 Skills Used

- Working with APIs using `requests`
- Parsing JSON data
- File handling in Python
- Functions and reusability
- Loops and user interaction
- Unit testing
- Basic packaging using `pyinstaller`

---

## 🛠️ Code Structure

1. Import required modules (`requests`, `time`)
2. Define constants: API key, base URL
3. Temperature conversion function
4. `get_weather()` for fetching + formatting data
5. Log search results to `weather_history.txt`
6. Main loop for continuous user input
7. Exit mechanism using `'exit'`

---

## 📋 How It Works

1. User types a location like `Delhi,IN`
2. App sends request to OpenWeatherMap API
3. API returns weather data in JSON format
4. App extracts and displays:
   - Description
   - Temp in °C / °F
   - Humidity
   - Wind speed
5. Results logged to file with timestamp
6. Runs again until user enters `'exit'`

---

## 📦 Sample Output

Location: Mumbai,IN  
Weather: haze  
Temperature: 32°C / 89.6°F  
Humidity: 70%  
Wind Speed: 4.63 m/s

---

## 📁 File Structure

Weather_App/
│
├── weather_app.py              # Main script  
├── test_weather.py             # Unit test  
├── weather_history.txt         # Search log  
├── weather_app.spec            # PyInstaller config  
├── dist/  
│   └── weather_app.exe         # Executable (optional)  
├── README.md                   # Project overview   

---

## 🧪 How to Run

```bash
python weather_app.py

## To build executable (Windows):

pyinstaller --onefile weather_app.py

## 🙌 Author
Rameez Jamadar
This project was built as a beginner-friendly CLI Python project for learning API usage and file handling.