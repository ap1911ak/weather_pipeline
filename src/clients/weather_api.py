import requests
from src.config.settings import settings

class WeatherClient:
    def fetch_raw_weather(self):
        params = {
            "latitude": settings.LATITUDE,
            "longitude": settings.LONGITUDE,
            "hourly": "temperature_2m"
        }
        response = requests.get(settings.API_URL, params=params)
        response.raise_for_status()
        return response.json()