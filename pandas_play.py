import pandas as pd

data = {'name' : ['tom', 'mary', 'jane'], 'age' : [20, 20, 30]}
df = pd.DataFrame(data)
print(df)
lst = pd.Series([2,3,4], index=['a', 'b', 'c'])
print(lst)
dc = pd.read_csv('real_estate.csv', index_col='No')
print(dc.head(4), dc.tail(4))
dc.info()
print(dc.loc[3])
print(dc.iloc[3])
print(dc.iloc[:, -1].values)
print(dc[dc['Y house price of unit area'] > 70])
df['school'] = ['mid', 'low', 'high']
print(df)