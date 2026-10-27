import requests
import os
from dotenv import load_dotenv
from cache import get_cached_weather, set_cached_weather

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def fetch_weather_from_api(city: str):
    """Fetch weather data from Visual Crossing API."""
    if not API_KEY:
        raise ValueError("API_KEY not configured in .env file")

    url = f"{BASE_URL}/{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")

def get_weather_data(city: str):
    """
    Get weather data for a city, using cache if available.
    Returns dict with weather data or raises exception.
    """
    city_normalized = city.strip()

    # Try cache first
    cached = get_cached_weather(city_normalized)
    if cached:
        print(f"Cache HIT for {city_normalized}")
        return cached

    # Cache miss - fetch from API
    print(f"Cache MISS for {city_normalized}, fetching from API...")
    data = fetch_weather_from_api(city_normalized)

    # Store in cache
    set_cached_weather(city_normalized, data)
    return data

if __name__ == "__main__":
    # Test the function
    city = "Sibiu, Romania"
    try:
        weather = get_weather_data(city)
        print(f"Weather data for {city}:")
        print(f"  Temperature: {weather.get('currentConditions', {}).get('temp')}°C")
        print(f"  Conditions: {weather.get('currentConditions', {}).get('conditions')}")
    except Exception as e:
        print(f"Error: {e}")