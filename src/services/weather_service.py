import pandas as pd

class WeatherService:
    def transform_data(self, raw_json):
        """Logic สำหรับการจัดการและทำความสะอาดข้อมูล"""
        if "hourly" not in raw_json:
            raise ValueError("Invalid data format from API")
        
        df = pd.DataFrame(raw_json["hourly"])
        df = df[['time', 'temperature_2m']]
        
        # Business Logic: กรองอุณหภูมิที่สูงกว่า 30 องศา
        df['is_hot'] = df['temperature_2m'] > 30
        return df