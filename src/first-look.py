import pandas as pd

"""
Returns the number of NaN values for each column
    - df: DataFrame, dataset where to look for NaNs
    - Returns: Dictionary with the columns and their number of NaN
"""
def findNans(df):
    columns = df.columns
    dict_nan = {}
    i = 0
    for column in columns:
        dict_nan[column] = df.loc[:,column].isnull().sum()
        i+=1

    return dict_nan


"""
Returns the number of NaN values for each column
    - df: DataFrame, dataset where to look for NaNs
    - chunkSize: int, size of chunk of data
    - Returns: Dictionary with the columns and their number of NaN
"""
def findNansInChunks(filePath, chunkSize=3000):
    chunk = pd.read_csv(filePath, chunksize=5)
    columns = chunk.columns
    dict_nan = {}
    for chunk in pd.read_csv(filePath, chunksize=chunkSize):
        i=0
        for column in columns:
          dict_nan[column] += chunk.loc[:,column].isnull().sum()
          i+=1

    return dict_nan
