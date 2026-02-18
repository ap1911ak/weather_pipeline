import pandas as pd

def clean_weather_data(raw_json):
    """แปลง JSON จาก API ให้เป็น DataFrame และทำความสะอาดข้อมูล"""
    if "hourly" not in raw_json:
        raise ValueError("Invalid data format from API")
    
    df = pd.DataFrame(raw_json["hourly"])
    # สมมติเราต้องการแค่เวลาและอุณหภูมิ
    df = df[['time', 'temperature_2m']]
    # กรองข้อมูลที่อุณหภูมิสูงกว่า 30 องศา (ตัวอย่าง Logic การ Transform)
    df['is_hot'] = df['temperature_2m'] > 30
    return df