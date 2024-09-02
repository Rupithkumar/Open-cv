import pandas as pd
df=pd.read_csv("data.csv")
df_string=df.to_string()
print(df_string)