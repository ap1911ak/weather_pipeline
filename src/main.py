from src.clients.weather_api import WeatherClient
from src.services.weather_service import WeatherService
from src.repositories.weather_storage import WeatherRepository

def run_pipeline():
    # Initialize components
    client = WeatherClient()
    service = WeatherService()
    repo = WeatherRepository()

    print("Step 1: Fetching data from API...")
    raw_data = client.fetch_raw_weather()

    print("Step 2: Transforming data...")
    transformed_df = service.transform_data(raw_data)

    print("Step 3: Saving data...")
    repo.save_to_csv(transformed_df)

    print("Pipeline finished!")

if __name__ == "__main__":
    run_pipeline()