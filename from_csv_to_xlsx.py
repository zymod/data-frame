import pandas as pd


df = pd.read_csv('ids.csv')
df.to_excel('ids.xlsx', index=True)
