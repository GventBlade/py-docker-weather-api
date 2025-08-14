import os
import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather(api_key: str) -> None:
    """
    Gets current weather for a specific city.
    """
    params = {"key": api_key, "q": CITY}
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        if "current" in data and "temp_c" in data["current"]:
            temperature = data["current"]["temp_c"]
            print(f"Current temperature in {CITY}: {temperature}°C")
        else:
            print(f"Could not get weather data for {CITY}. Response: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")


if __name__ == "__main__":
    # Read API key from environment variable
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
    else:
        get_weather("Paris", api_key)
