import airflow
from airflow.models import DAG, Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator


default_args = {
    'start_date': airflow.utils.dates.days_ago(2),
    'owner': 'zkan'
}
dag = DAG(
    dag_id='trigger_dag_target',
    default_args=default_args,
    schedule_interval=None,
)


def branch_func(**kwargs):
    print(f'Remotely received a message: {kwargs["dag_run"].conf["message"]}')

    count = Variable.get('count', default_var=0)
    print(f'count: {count}')

    count = int(count) + 1
    Variable.set('count', count)

    if count == 1:
        return 'run_this'
    if count == 3:
        Variable.set('count', 0)

    return 'skip'


branch_op = BranchPythonOperator(
    task_id='branching',
    python_callable=branch_func,
    provide_context=True,
    dag=dag,
)


def run_this_func(*args, **kwargs):
    return 'Hello!'


run_this = PythonOperator(
    task_id='run_this',
    python_callable=run_this_func,
    dag=dag,
)

skip = DummyOperator(
    task_id='skip',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    trigger_rule='none_failed_or_skipped',
    dag=dag,
)

branch_op >> [run_this, skip] >> end
