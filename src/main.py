import requests
import os
from transform import clean_weather_data

def fetch_weather():
    # API ของ Open-Meteo ดึงพยากรณ์อากาศของกรุงเทพฯ
    url = "https://api.open-meteo.com/v1/forecast?latitude=13.75&longitude=100.50&hourly=temperature_2m"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("Fetching data...")
    data = fetch_weather()
    
    print("Transforming data...")
    df = clean_weather_data(data)
    
    # บันทึกลงโฟลเดอร์ data/
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/weather_report.csv', index=False)
    print("Pipeline finished! Saved to data/weather_report.csv")