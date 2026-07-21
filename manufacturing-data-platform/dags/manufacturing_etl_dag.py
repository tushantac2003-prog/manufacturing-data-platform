from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="manufacturing_etl_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["manufacturing", "etl"],
) as dag:

    extract = BashOperator(
        task_id="extract_data",
        bash_command="""
        set -e
        cd /opt/airflow
        python3 /opt/airflow/scripts/extract.py
        """
    )

    validate = BashOperator(
        task_id="validate_data",
        bash_command="""
        set -e
        cd /opt/airflow
        python3 /opt/airflow/scripts/validate.py
        """
    )

    transform = BashOperator(
        task_id="transform_data",
        bash_command="""
        set -e
        cd /opt/airflow
        python3 /opt/airflow/scripts/transform.py
        """
    )

    load = BashOperator(
        task_id="load_data",
        bash_command="""
        set -e
        cd /opt/airflow
        python3 /opt/airflow/scripts/load.py
        """
    )

    extract >> validate >> transform >> load