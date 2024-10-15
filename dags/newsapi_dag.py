from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import s3fs
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET, NEWSAPI_KEY

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": NEWSAPI_KEY
    }
    response = requests.get(url, params=params)
    news = response.json()
    df = pd.DataFrame(news['articles'])
    return df.to_json(orient='records')

def save_to_s3(**kwargs):
    ti = kwargs['ti']
    news_json = ti.xcom_pull(task_ids='fetch_news_task')
    df = pd.read_json(news_json)
    
    s3 = s3fs.S3FileSystem(anon=False,key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_ACCESS_KEY)
    with s3.open('newsapi-airflow-project20241001/noticias_{}.csv'.format(datetime.now().strftime('%Y%m%d')), 'w') as f:
        df.to_csv(f, index=False)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 14),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'newsapi_dag',
    default_args=default_args,
    description='A DAG to fetch news from NewsAPI and store in S3',
    schedule_interval=timedelta(days=1),
)

fetch_news_task = PythonOperator(
    task_id='fetch_news_task',
    python_callable=fetch_news,
    dag=dag,
)

save_to_s3_task = PythonOperator(
    task_id='save_to_s3_task',
    python_callable=save_to_s3,
    provide_context=True,
    dag=dag,
)

fetch_news_task >> save_to_s3_task