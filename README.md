# NewsAPI-AWS-Airflow-ETL

## Description
This project implements an ETL (Extract, Transform, Load) pipeline that extracts news data from NewsAPI, processes it, and stores it in AWS S3 using Apache Airflow for task orchestration.

## Features
- News data extraction from NewsAPI
- Data storage in AWS S3
- Task orchestration with Apache Airflow
- Secure credential management

## Requirements
- Python 3.7+
- Apache Airflow
- AWS account with S3 access
- NewsAPI API key

## Installation
1. Clone this repository: git clone https://github.com/your-username/NewsAPI-AWS-Airflow-ETL.git
2. Install dependencies:
3. Set up environment variables in a `config.py` file: ```python
    AWS_ACCESS_KEY_ID = 'your_access_key_id'
    AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
    AWS_REGION = 'your_region'
    S3_BUCKET = 'your_s3_bucket'
    NEWSAPI_KEY = 'your_newsapi_key'

## Usage
Start the Airflow webserver: airflow webserver -p 8080
In another terminal, start the Airflow scheduler: airflow scheduler
Access the Airflow web interface at http://localhost:8080
Activate the 'newsapi_dag' in the Airflow interface

## Project Structure
'dags/': Contains Airflow DAG files
'scripts/': Auxiliary scripts for data processing
'logs'/: Airflow logs
'config.py': Configuration file (not included in the repository for security reasons)

## Contributing
Contributions are welcome. Please open an issue first to discuss what you would like to change.