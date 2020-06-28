"""
Information gathering with apache airflow
"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models import Variable


default_args = {
    'owner': 'Vlad',
    'depends_on_past': False,
    'start_date': datetime(2020, 2, 3),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


# port_scaning_params = Variable.get("port-scaning", deserialize_json=True)
# application_scaning_params = Variable.get("application-scaning", deserialize_json=True)
ports = [80, 443, 22, 21, 8080, 9090]

with DAG('port-scaning', default_args=default_args, catchup=False,
            schedule_interval=None) as dag:

    start = DummyOperator(task_id='start', dag=dag)
    nmap = DummyOperator(task_id='nmap', dag=dag)
    for port in ports:
        netcat = DummyOperator(task_id='nc-%s' % str(port), dag=dag)
    end = DummyOperator(task_id='end', dag=dag)
