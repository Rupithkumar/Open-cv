import pandas as pd
df=pd.read_json('data.json')
df_string=df.to_string()
print(df_string)