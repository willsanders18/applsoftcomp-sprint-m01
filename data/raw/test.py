import pandas as pd

data_table = pd.read_csv('gdp-data.csv')
data_table_child = pd.read_csv('child-motality.csv')
count = 0



for i in data_table['name']:
    count += 1
    if count > 10:
        break
    else:
        print(i)
