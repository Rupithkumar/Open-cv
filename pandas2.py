import pandas as pd
a={
    'clories':[420,340,335,385,478],
    'duration':[40,10,34,67,28]
}
b=pd.DataFrame(a,index=['a','b','c','d','e'])
print(b)