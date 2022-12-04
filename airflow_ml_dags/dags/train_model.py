import os
from datetime import timedelta

from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from airflow.utils.dates import days_ago
from docker.types import Mount

from airflow import DAG

default_args = {
    "owner": "airflow",
    "email": ["eglaforsteam@gmail.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

RAW_DATA_PATH = "/data/raw/{{ ds }}"

with DAG(
    "train_model",
    default_args=default_args,
    schedule_interval="@weekly",
    start_date=days_ago(1),
) as dag:
    data_ready_sensor = PythonSensor(
        task_id="data_ready_sensor",
        python_callable=os.path.exists,
        op_args=[f"/opt/airflow{RAW_DATA_PATH}/data.csv"],
        timeout=1000,
        poke_interval=6,
        retries=2,
        mode="poke",
    )

    preprocess = DockerOperator(
        image="preprocessing",
        command="/data/raw/{{ ds }} /data/interim/{{ ds }}",
        network_mode="bridge",
        task_id="preprocessing",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

    split = DockerOperator(
        image="train-val-split",
        command="/data/interim/{{ ds }} /data/processed/{{ ds }}",
        network_mode="bridge",
        task_id="train-val-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

    train_model = DockerOperator(
        image="train-model",
        command="/data/processed/{{ ds }} /data/models/{{ ds }}",
        network_mode="bridge",
        task_id="train-model",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

    evaluate_model = DockerOperator(
        image="evaluate-model",
        command="/data/processed/{{ ds }} /data/models/{{ ds }} /data/metrics/{{ ds }}",
        network_mode="bridge",
        task_id="evaluate-model",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

    data_ready_sensor >> preprocess >> split >> train_model >> evaluate_model
