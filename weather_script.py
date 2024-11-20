import requests

API_KEY = 'd1ad1ee81341f423ba3fd13c48d9d12b'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    else:
        return None

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found or API request failed.")

if __name__ == "__main__":
    main()