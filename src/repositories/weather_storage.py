import os
import pandas as pd
from src.config.settings import settings

class WeatherRepository:
    def save_to_csv(self, df: pd.DataFrame):
        os.makedirs(os.path.dirname(settings.OUTPUT_PATH), exist_ok=True)
        df.to_csv(settings.OUTPUT_PATH, index=False)
        print(f"Data saved successfully to {settings.OUTPUT_PATH}")