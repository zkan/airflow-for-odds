# Airflow for ODDS

## Dataset

[Breakfast at the Frat](https://www.dunnhumby.com/careers/engineering/sourcefiles)

## Setting the Airflow home

```sh
export AIRFLOW_HOME=/Users/zkan/Projects/zkan/airflow-for-odds/airflow
```

PS. The path above may vary when using a different machine.

## Fixng an issue when using `requests` on Mac OS

```sh
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```
