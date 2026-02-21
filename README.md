# 🌦️ Weather Data Pipeline
Production-ready lightweight Weather ETL Pipeline
ออกแบบด้วยแนวคิด Layered Architecture + Separation of Concerns
รองรับการต่อยอดไปสู่ Data Platform ขนาดใหญ่ได้

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
                   clients.weather_api
                          │
                ┌─────────▼───────────┐
                │  services layer     │
                │  weather_service    │
                └─────────┬───────────┘
                          │
                  transform.py (pure)
                          │
                ┌─────────▼───────────┐
                │ repositories layer  │
                │ weather_storage     │
                └─────────────────────┘



# 🧱 3. Project Structure

     weather_pipeline/
    │
    ├── src/
    │   ├── main.py
    │   ├── transform.py
    │   │
    │   ├── clients/
    │   │   └── weather_api.py
    │   │
    │   ├── services/
    │   │   └── weather_service.py
    │   │
    │   ├── repositories/
    │   │   └── weather_storage.py
    │   │
    │   └── config/
    │       └── settings.py
    │
    ├── tests/
    │   └── test_transform.py
    │
    ├── Dockerfile
    ├── requirements.txt
    ├── pytest.ini
    └── .github/workflows/ci.yml

# ⚙️ 4. Design Principles
## Separation of Concerns

    | Layer        | Responsibility                      |
    | ------------ | ----------------------------------- |
    | clients      | External API communication          |
    | services     | Business logic orchestration        |
    | transform    | Pure deterministic transformation   |
    | repositories | Persistence logic                   |
    | config       | Environment & runtime configuration |
    | main         | Entry point                         |

#🚀 5. Execution
##▶️ Run Locally

    pip install -r requirements.txt
    python -m src.main
  
##🐳 Docker Execution

    docker build -t weather-pipeline .
    docker run --rm weather-pipeline
    
#📊 6. Data Model

    | Column         | Type     | Description           |
    | -------------- | -------- | --------------------- |
    | time           | datetime | Observation timestamp |
    | temperature_2m | float    | Air temperature (°C)  |
    | is_hot         | boolean  | temperature > 30      |

#🔍 7. Engineering Trade-offs

    | Decision              | Rationale                    |
    | --------------------- | ---------------------------- |
    | CSV storage           | Lightweight demo persistence |
    | Pandas                | Dataset ขนาดเล็ก              |
    | Batch Mode            | Operational simplicity       |
    | No orchestration tool | Keep system minimal          |

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

##🔐 Reliability Improvements
  - Retry with exponential backoff
  - Timeout control
  - Schema validation (Pandera / Pydantic)
  - Dead-letter storage
  - Alerting integration

#🛡️ 9. Production Hardening Checklist
 - Structured logging
 - Centralized config management
 - Environment-based config (.env supported)
 - Observability metrics
 - Container security scan
 - CI/CD enforcement
