# merge csv
import pandas as pd
import os

# merge csv in data directory

csv_files = [f for f in os.listdir('data') if f.endswith('.csv')]

df = pd.DataFrame()

for file in csv_files:
    df = df.append(pd.read_csv('data/' + file))

df.to_csv('merged.csv', index=False)
