from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils import timezone


default_args = {
  'owner': 'ODDS',
}
dag = DAG('hello_pipeline',
          default_args=default_args,
          start_date=timezone.datetime(2020, 8, 1),
          catchup=False)


def say_hello():
    return 'Hello, Python'


say_hello = PythonOperator(task_id='say_hello',
                           python_callable=say_hello,
                           dag=dag)

say_hello
