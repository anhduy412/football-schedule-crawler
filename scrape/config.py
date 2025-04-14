import os

# Folder in MinIO
BRONZE_LAYER_PATH = 'data/football_schedule'

# Info to log in to MinIO
MINIO_ACCESS_KEY = os.getenv('MINIO_ROOT_USER', 'default-access-key')
MINIO_SECRET_KEY = os.getenv('MINIO_ROOT_PASSWORD', 'default-secret-key')
ENDPOINT = 'http://minio1:9000'

# Bucket name of MinIO
BUCKET_NAME = 'football_schedule'

# Folder on the local system
RAW_PATH = './data/raw_data/'
CLEAN_PATH = './data/clean_data/'
STAGE_PATH = './data/stage_layer/'

# File on the local system
temporary_file = 'temp_file.csv'
temporary_file_parquet = 'temp_file.parquet'

# Postgres for data warehouse
POSTGRES_HOST = '172.28.0.6'
POSTGRES_PORT = '5432'
POSTGRES_DB_NAME = 'postgres'
POSTGRES_URL = f'jdbc:postgresql://{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}'

# Postgres metadata
POSTGRES_USER = 'airflow'
POSTGRES_PASSWORD = 'airflow'
POSTGRES_DRIVER = 'org.postgresql.Driver'