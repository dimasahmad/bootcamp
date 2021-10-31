import requests


def get_forecast(api_key: str, city: str, dt_txt: str) -> dict:
    """Get weather forecast from [OpenWeather](https://openweathermap.org) for a specific datetime

    Args:
        api_key (str): API key
        city (str): City name
        dt_txt (str): date and time in UTC, yyyy-mm-dd hh:mm:ss

    Returns:
        dict: City information and weather forecast result

    Raises:
        Exception: No forecast data found
    """

    # API base URL and endpoint
    base_url: str = "https://api.openweathermap.org/data/2.5"
    endpoint: str = "/forecast"

    # Parameters
    params: dict[str, str] = {'q': city, 'appid': api_key}

    # Send GET request, then convert it's response to json
    response: dict | list = requests.get(
        url=base_url + endpoint, params=params).json()

    # Iterate results to get the specified datetime
    for forecast in response['list']:
        if forecast['dt_txt'] == dt_txt:
            return {"city": response["city"], "forecast": forecast}

    # Raise Exception if no data found
    raise Exception("No forecast data found")


# Get weather forecast
forecast: dict = get_forecast(api_key="6a41a7abc293e0e942c7bfbb43e6b220",
                              city="Bandung", dt_txt="2021-10-30 15:00:00")

# Print result
print("WEATHER FORECAST")
print(f"City: {forecast['city']['name']}")
print(f"Population: {forecast['city']['population']}")
print(f"DateTime: {forecast['forecast']['dt_txt']} UTC")
print(f"Weather: {forecast['forecast']['weather'][0]['description']}")
