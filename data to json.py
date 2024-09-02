import pandas as pd
data={
    "Name":["John","Anna","Peter","Linda"],
    "Age":[28,24,5,32],
    "City":["New York","Paris","London","Tokyo"]
}
df=pd.DataFrame(data)
print(df)
json_data=df.to_json(orient='records')
print(json_data)