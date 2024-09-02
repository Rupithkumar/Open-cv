import pandas as pd
json_string = '''
{
    "Name":["Rahul","Vinod","Prakash"],
    "Age":[28,34,27],
    "Salary":[45000,40000,50000]
}
'''
df = pd.read_json(json_string)
print(df)