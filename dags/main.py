from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scrape.scraping_script import scrape_and_save

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

with DAG("crawl_dag", schedule_interval="0 0 * * *", default_args=default_args, max_active_runs=1) as dag:
    crawl_data = PythonOperator(
        task_id="scrape_and_save",
        python_callable=scrape_and_save
    )

    crawl_data
