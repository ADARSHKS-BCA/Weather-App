from django.shortcuts import render
import requests
import datetime 

def get_weather_data(city):
    """Helper function to fetch weather data for a given city"""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api-key}'
    PARAMS = {'units': 'metric'}
    
    try:
        response = requests.get(url, params=PARAMS)
        data = response.json()
        
        # Check if API returned an error
        if response.status_code != 200 or 'cod' in data and data['cod'] != 200:
            return {'error': data.get('message', 'City not found. Please try again.')}
        
        # Check if required keys exist in the response
        if 'weather' not in data or 'main' not in data:
            return {'error': 'Invalid response from weather API. Please try again.'}
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        day = datetime.date.today()
        
        return {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    
    except KeyError as e:
        return {'error': f'Error accessing weather data: {str(e)}. Please try again.'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}. Please try again.'}

def home(request):
    # Default city to show on initial page load
    default_city = "bangalore"
    
    # If it's a GET request (initial page load), show default city weather
    if request.method == 'GET':
        weather_data = get_weather_data(default_city)
        return render(request, 'index.html', weather_data)
    
    # If POST request, get city from form
    if 'city' in request.POST:
        city = request.POST['city'].strip()  # Remove extra spaces
        
        # Check if city name is not empty
        if not city:
            # If empty, show default city
            weather_data = get_weather_data(default_city)
            return render(request, 'index.html', weather_data)
        
        # Fetch weather for the searched city
        weather_data = get_weather_data(city)
        return render(request, 'index.html', weather_data)
    
    # Fallback: show default city
    weather_data = get_weather_data(default_city)
    return render(request, 'index.html', weather_data)

