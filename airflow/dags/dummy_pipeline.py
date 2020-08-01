from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils import timezone


default_args = {
  'owner': 'ODDS',
}
dag = DAG('dummy_pipeline',
          schedule_interval='*/5 * * * *',
          default_args=default_args,
          start_date=timezone.datetime(2020, 8, 1),
          catchup=False)

t1 = DummyOperator(task_id='my_1st_dummy_task',dag=dag)
t2 = DummyOperator(task_id='my_2nd_dummy_task', dag=dag)
t3 = DummyOperator(task_id='my_3rd_dummy_task', dag=dag)
t4 = DummyOperator(task_id='my_4th_dummy_task', dag=dag)
t5 = DummyOperator(task_id='my_5th_dummy_task', dag=dag)
t6 = DummyOperator(task_id='my_6th_dummy_task', dag=dag)
t7 = DummyOperator(task_id='my_7th_dummy_task', dag=dag)
t8 = DummyOperator(task_id='my_8th_dummy_task', dag=dag)

t1 >> t2 >> t3 >> t8
t1 >> t4 >> [t5, t6] >> t7 >> t8
