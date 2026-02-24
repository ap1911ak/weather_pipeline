from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.pipeline import extract, transform, load
import logging


with DAG(
    dag_id="weather_pipeline",
    schedule_interval="@daily",
    start_date=datetime(2024,1,1),
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load
    )

    t1 >> t2 >> t3
    
logger = logging.getLogger(__name__)