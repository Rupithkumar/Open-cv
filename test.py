import pandas as pd
#Define a dictionary with nested data
data ={
    "Name":["John","Anna","Peter","Linda"],
    "Age":[28,24,35,32],
    "Address":[
        {"City":"New York","Street":"123 Main St","Zip":"10001"},
        {"City":"Paris","Street":"456 Rue de Rivoli","Zip":"75001"},
        {"City":"London","Street":"789 Oxford St","Zip":"WID ILL"},
        {"City":"Tokyo","Street":"012 Shinjuku Ave","Zip":"160-0022"}
    ]
}

#Convert dictionary to DataFrame
df=pd.DataFrame(data)
#Convert DataFrame to JSON format
json_data=df.to_json(orient='records')
#Display the JSON data
print(json_data)