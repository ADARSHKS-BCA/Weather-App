# Weather App

A simple weather app built with Django that shows weather information for any city. It has a nice day/night theme toggle and displays temperature, humidity, wind speed, and weather conditions.

## Features

- Search weather for any city
- Shows temperature, humidity, wind speed
- Day/night mode toggle (saves your preference)
- Responsive design
- Clean and simple UI

## Requirements

- Python 3.7+
- Django
- requests library
- OpenWeatherMap API key (free)

## Setup

1. Clone or download this project

2. Install the dependencies:
```bash
pip install django requests
```

3. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api). Sign up, go to API Keys, and copy your key.

4. Open `weatherapp/views.py` and replace the API key on line 7:
```python
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY_HERE'
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the server:
```bash
python manage.py runserver
```

7. Open http://127.0.0.1:8000/ in your browser

That's it! The app will show Bangalore weather by default. You can search for any city and toggle between day/night mode using the button in the top right.

## Project Structure

- `Weatherproject/` - Main Django project settings
- `weatherapp/` - The weather app
  - `views.py` - Main logic for fetching weather
  - `templates/index.html` - Frontend template
  - `static/style.css` - Styling

## Notes

- The default city is set to "bangalore" in `views.py`. You can change it if you want.
- Make sure to keep your API key secure. Don't commit it to public repos.
- The app uses OpenWeatherMap's free tier which has rate limits, but it's enough for personal use.

## License

Free to use and modify.
