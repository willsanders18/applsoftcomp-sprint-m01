import pandas as pd

# Load and tidy
data_table = pd.read_csv('./data/raw/gdp-data.csv')
# Use pd.melt(), pd.pivot_table(), or custom code
df = pd.DataFrame(data_table)
tidy_CM_data_table = df.melt(
    id_vars = ['geo', 'name'],
    var_name='year',
    value_name= 'GDP per capita'
)
tidy_CM_data_table.to_csv('./data/preprocessed/tidy_GDP_data.csv', index=False)