import requests

def get_current_weather(api_key, lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        return {"error": 401, "message": "Unauthorized - check your API key."}
    elif response.status_code == 403:
        return {"error": 403, "message": "Forbidden - check your permissions."}
    else:
        return {"error": response.status_code, "message": response.reason}

# Replace with your actual API key
api_key = '041c36486fc0b2772fd95e1912d43ef3'
lat = 40.7128  # Example latitude for New York City
lon = -74.0060  # Example longitude for New York City

weather_data = get_current_weather(api_key, lat, lon)
print(weather_data)
