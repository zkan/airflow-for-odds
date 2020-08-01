import requests

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils import timezone


default_args = {
  'owner': 'ODDS',
}
dag = DAG('python_pipeline',
          default_args=default_args,
          start_date=timezone.datetime(2020, 8, 1),
          catchup=False)

t1 = DummyOperator(task_id='start',dag=dag)


def get_covid_data_today():
    response = requests.get('https://covid19.th-stat.com/api/open/today')
    return response.json()


# https://covid19.th-stat.com/api/open/today
t2 = PythonOperator(task_id='get_covid_data_today',
                    python_callable=get_covid_data_today,
                    dag=dag)

t3 = DummyOperator(task_id='end', dag=dag)

t1 >> t2 >> t3
