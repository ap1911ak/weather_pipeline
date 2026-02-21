import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    
    API_URL = os.getenv("WEATHER_API_URL")
    LATITUDE = os.getenv("LATITUDE")
    LONGITUDE = os.getenv("LONGITUDE")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH", "data/weather_report.csv")

settings = Settings()