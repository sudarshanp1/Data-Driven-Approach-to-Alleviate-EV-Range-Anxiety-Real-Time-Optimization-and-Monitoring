
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_data(**kwargs):
    # Placeholder for extraction logic
    print("Extracting data...")

def transform_data(**kwargs):
    # Placeholder for transformation logic
    print("Transforming data...")

def load_data(**kwargs):
    # Placeholder for loading logic
    print("Loading data...")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
}

dag = DAG('driver_data_etl', default_args=default_args, schedule_interval='@daily')

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag
)

extract_task >> transform_task >> load_task
            
