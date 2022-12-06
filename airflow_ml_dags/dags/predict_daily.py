import os

from datetime import timedelta

from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from airflow.utils.dates import days_ago
from docker.types import Mount

from airflow import DAG

default_args = {
    "owner": "airflowow",
    "email": ["eglaforsteam@gmail.com"],
    "retries": 0,
    "retry_delay": timedelta(minutes=1),
}

MODEL_PATH = Variable.get("model_path")
RAW_DATA_PATH = "/data/raw/{{ ds }}"
INTERIM_DATA_PATH = "/data/interim/{{ ds }}"
PREDICTIONS_PATH = "/data/predictions/{{ ds }}"

with DAG(
    "predict",
    default_args=default_args,
    schedule_interval="@daily",
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
        command=f"{RAW_DATA_PATH} {INTERIM_DATA_PATH}",
        network_mode="bridge",
        task_id="preprocessing",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

    predict = DockerOperator(
        image="predict-model",
        command=f"{INTERIM_DATA_PATH} {MODEL_PATH} {PREDICTIONS_PATH}",
        network_mode="bridge",
        task_id="predict-model",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/alex/airflow/data/", target="/data", type="bind")],
    )

    data_ready_sensor >> preprocess >> predict
