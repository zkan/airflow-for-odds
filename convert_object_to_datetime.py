import pandas as pd


df = pd.read_csv('dataset/transaction-data-table.csv', header=1)
print(df.head())

df['new_week_end_date'] = pd.to_datetime(df['WEEK_END_DATE'], format='%d-%b-%y')

print(df.head())
print(df.info())
