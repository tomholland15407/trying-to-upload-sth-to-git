import pandas as pd

class DataPreprocessing():
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None

    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('real_estate.csv', index_col='No')
        self.dataframe = df

    def set_attributes_and_output(self):
        self.X = self.dataframe.iloc[:, :-1].values
        self.y = self.dataframe.iloc[:, -1].values

dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()
print(dp.dataframe.info())
print(dp.dataframe['X2 house age'])
print('First house\'s age:', dp.X[0][1])
print('House price/unit are:', dp.y[0])