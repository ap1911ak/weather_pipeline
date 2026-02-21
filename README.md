# 🌦️ Weather Data Pipeline
Lightweight ETL pipeline สำหรับดึงข้อมูลพยากรณ์อากาศจาก **Open-Meteo API** → Transform → Persist เป็น CSV  
ออกแบบในเชิง Data Engineering Best Practice เพื่อใช้เป็น template สำหรับ production-grade pipeline ขนาดเล็ก

---

# 📌 1. Problem Statement
องค์กรต้องการ ingest weather data รายชั่วโมง เพื่อใช้ใน:
  - Demand forecasting
  - Energy optimization
  - Environmental analytics
  - Feature store enrichment

Pipeline นี้ทำหน้าที่:
  > Extract → Validate → Transform → Persist (Batch Mode)

# 🏗️ 2. High-Level Architecture
            ┌─────────────────────┐
            │   Open-Meteo API    │
            └─────────┬───────────┘
                      │
                (HTTP Request)
                      │
            ┌─────────▼───────────┐
            │   Extract Layer     │
            │  fetch_weather()    │
            └─────────┬───────────┘
                      │
            ┌─────────▼───────────┐
            │  Transform Layer    │
            │ clean_weather_data()│
            └─────────┬───────────┘
                      │
            ┌─────────▼───────────┐
            │     Load Layer      │
            │  CSV Persistence    │
            └─────────────────────┘


# 🧱 3. Project Structure
    weather_pipeline-dev/
    │
    ├── src/
    │ ├── main.py # Orchestration entry point
    │ └── transform.py # Pure transformation logic
    │
    ├── tests/
    │ └── test_transform.py
    │
    ├── Dockerfile
    ├── requirements.txt
    └── pytest.ini

# ⚙️ 4. Design Principles
## 4.1 Separation of Concerns
    | Layer     | Responsibility                  |
    |------------|--------------------------------|
    | Extract    | External API communication     |
    | Transform  | Pure data logic                |
    | Load       | Persistence                    |
    | Test       | Deterministic validation       |

`transform.py` ไม่มี side-effect → ทำให้ test ได้ง่าย

---

## 4.2 Deterministic Transformation

```python
df['is_hot'] = df['temperature_2m'] > 30
```
## 4.3 Idempotency
Pipeline สามารถ rerun ได้โดย:
  - Overwrite file output
  - ไม่มี hidden state
  - ไม่มี dependency ภายนอกนอกจาก API

#🚀 5. Executio
## Dockerized Execution

    docker build -t weather-pipeline .
    docker run --rm weather-pipeline
    
#📊 6. Data Model

    | Column         | Type     | Description          |
    | -------------- | -------- | -------------------- |
    | time           | datetime | Observation time     |
    | temperature_2m | float    | Air temperature (°C) |
    | is_hot         | boolean  | temperature > 30     |


#🔍 7. Engineering Trade-offs

    | Decision         | Rationale                 |
    | ---------------- | ------------------------- |
    | CSV storage      | Simplicity for demo       |
    | Pandas           | Small dataset             |
    | Batch mode       | Simpler operational model |
    | No orchestration | Keep lightweight          |

#📈 8. Scalability Path

  หากต้อง scale:
##🔁 Replace Pandas → PySpark
  เมื่อ dataset โตระดับ GB+

##🗄 Replace CSV → Object Storage
  - S3
  - GCS
  - Data Lake (Parquet format)

##⏱ Add Orchestration
  - Apache Airflow

##📊 Add Monitoring
  - Prometheus
  - Grafana

🔐 Add Retry & Circuit Breaker

#🛡️ 9. Reliability Considerations 

  Production-ready version ควรเพิ่ม:
  Structured logging
  Retry with exponential backoff
  Timeout handling
  Schema validation (Pandera)  
  Dead-letter storage
  Alerting mechanism
