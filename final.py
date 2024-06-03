import requests

def get_current_weather(api_key, city):
    url = "https://api.weatherbit.io/v2.0/current"
    params = {
        'key': api_key,
        'city': city
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        return {"error": 403, "message": "Forbidden - check your API key and permissions."}
    else:
        return {"error": response.status_code, "message": response.reason}

# Replace 'your_api_key' with your actual Weatherbit API key
api_key = '4d35846726f442febc5b5b4ae41ec7bd'
city = 'New York'

weather_data = get_current_weather(api_key, city)
print(weather_data)
