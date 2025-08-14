import os
import requests
# The 'typing' import is only needed for type hints that are not built-in,
# so we can remove the unused imports like 'Dict' and 'Any'.
# 'None' is a built-in type and should not be imported from 'typing'.
# Also, corrected the URL to use HTTPS for a secure connection.


def get_weather(city: str, api_key: str) -> None:
    """
    Gets current weather for a specific city.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # For Celsius
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        if "main" in data and "temp" in data["main"]:
            temperature = data["main"]["temp"]
            print(f"Current temperature in {city}: {temperature}°C")
        else:
            print(f"Could not get weather data for {city}. Response: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")


if __name__ == "__main__":
    # Read API key from environment variable
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
    else:
        get_weather("Paris", api_key)
