import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    "generate_dataset",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(5),
) as dag:
    generate = DockerOperator(
        image="generate-dataset",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="generate_dataset",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

generate
