import requests

def get_weather_data(city_name, api_key):
    """Fetch weather data from OpenWeatherMap API."""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
    return None

def display_weather_info(data):
    """Extract and display weather details."""
    if data and data.get('cod') == 200:
        try:
            city = data['name']
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']

            print(f"\nWeather Report for {city}:")
            print(f"  Description       : {description}")
            print(f"  Temperature       : {temp}°C")
            print(f"  Feels Like        : {feels_like}°C")
            print(f"  Humidity          : {humidity}%")
        except KeyError as e:
            print(f"Missing expected data in API response: {e}")
    else:
        print("City not found or no data available.")

def main():
    api_key = 'a4c90e2f5c8b4a49c4ef8e2a017c17e2'  # Your OpenWeatherMap API key
    city_name = input("Enter the city name: ").strip()
    if city_name:
        data = get_weather_data(city_name, api_key)
        display_weather_info(data)
    else:
        print("City name cannot be empty.")

if __name__ == "__main__":
    main()
