from src.clients.weather_api import WeatherClient
from src.services.weather_service import WeatherService
from src.repositories.weather_storage import WeatherRepository

def run_pipeline():
    print("Pipeline started!")
    raw_data = extract()
    transformed_df = transform(raw_data)
    load(transformed_df)
    print("Pipeline finished!")

def extract():
    client = WeatherClient()
    raw_data = client.fetch_raw_weather()
    return raw_data

def transform(raw_data):
    service = WeatherService()
    transformed_df = service.transform_data(raw_data)
    return transformed_df

def load(transformed_df):
    repository = WeatherRepository()
    repository.save_to_csv(transformed_df)
