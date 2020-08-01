from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils import timezone


default_args = {
  'owner': 'ODDS',
}
dag = DAG('bash_pipeline',
          default_args=default_args,
          start_date=timezone.datetime(2020, 8, 1),
          catchup=False)

t1 = DummyOperator(task_id='start',dag=dag)

t2 = BashOperator(task_id='hello',
                  bash_command='echo hello',
                  dag=dag)

t3 = DummyOperator(task_id='end', dag=dag)

t1 >> t2 >> t3
