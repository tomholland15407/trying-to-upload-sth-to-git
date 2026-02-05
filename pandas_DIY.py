import pandas as pd
class DataPreprocessing:
    def __init__(self):
        self.dataframe = None
        self.X = None
        self.Y = None
    def read(self):
        df = pd.read_csv('real_estate.csv', index_col = 'No')
        self.dataframe = df
    def set_figures(self):
        self.X = self.dataframe.iloc[:, :-1].values
        self.Y = self.dataframe.iloc[:, -1]. values

dp = DataPreprocessing()
dp.read()
dp.set_figures()
dp.dataframe.info()
print('the distance of house 3 to the nearest mrt station is :', dp.X[2][2])
print('the price of that house is: ', dp.Y[2])
print(dp.dataframe.loc[3])
print(dp.dataframe.iloc[2])