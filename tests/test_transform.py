import pytest
from src.transform import clean_weather_data

def test_clean_weather_data_logic():
    # สร้างข้อมูลจำลอง (Mock Data)
    mock_input = {
        "hourly": {
            "time": ["2023-10-01T00:00", "2023-10-01T01:00"],
            "temperature_2m": [25.5, 40.0]
        }
    }
    df = clean_weather_data(mock_input)
    
    assert len(df) == 2
    assert df.loc[1, 'is_hot'] == True  # 32.0 > 30 ต้องเป็น True