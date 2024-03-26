from airflow import models
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.operators.gcs import GCSCreateBucketOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import (
              BigQueryCreateEmptyDatasetOperator,
              BigQueryCreateEmptyTableOperator,
              BigQueryCreateExternalTableOperator
              )
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStorageObjectSensor
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago 

project_id = "numeric-guide-417915"
#region = Variable.get("region")
#bucket_name = Variable.get("bucket_name")

with models.DAG(
    "test9",
    default_args={
        "project_id": project_id,
        "start_date":days_ago(1)
    },
    description="This task is belong to BI team",
    schedule_interval=timedelta(days=1),
    tags=["BITeam"]
) as dag:
    start_task = DummyOperator(
        task_id="starttttting",
        dag=dag
    )

    create_bucket = GCSCreateBucketOperator(
        task_id="creating_bucket",
        bucket_name="simanjree",
        dag=dag
    )

    end_task = DummyOperator(
        task_id="endiiing",
        dag=dag
    )

start_task >> create_bucket >> end_task