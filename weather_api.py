"""
Weather API interaction module.
Uses a mock implementation since we can't access external APIs in this environment.
"""

import json
import random
from datetime import datetime

def fetch_weather(location):
    """
    Fetch weather data for the given location.
    
    In a real application, this would make an HTTP request to a weather API.
    Since we're in a constrained environment, we'll generate mock data.
    
    Args:
        location: Location string (city name)
        
    Returns:
        dict: Weather data for the location
    """
    # In a real app, we would use:
    # import urllib.request
    # import urllib.parse
    # url = f"https://api.example.com/weather?q={urllib.parse.quote(location)}&appid=YOUR_API_KEY"
    # with urllib.request.urlopen(url) as response:
    #     return json.loads(response.read().decode())
    
    # For this demo, we'll create mock data
    return generate_mock_weather_data(location)

def generate_mock_weather_data(location):
    """Generate mock weather data for demo purposes."""
    weather_conditions = [
        "Clear", "Sunny", "Partly Cloudy", "Cloudy", 
        "Overcast", "Rain", "Light Rain", "Showers",
        "Thunderstorm", "Snow", "Light Snow", "Fog"
    ]
    
    temp_celsius = random.randint(-10, 35)
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    
    return {
        "location": {
            "name": location,
            "country": "Demo Country",
            "localtime": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        "current": {
            "temp_c": temp_celsius,
            "temp_f": temp_fahrenheit,
            "condition": {
                "text": random.choice(weather_conditions)
            },
            "wind_kph": random.uniform(0, 30),
            "wind_dir": random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"]),
            "humidity": random.randint(30, 95),
            "feelslike_c": temp_celsius + random.uniform(-3, 3),
            "feelslike_f": temp_fahrenheit + random.uniform(-5, 5),
            "uv": random.uniform(0, 10)
        }
    }