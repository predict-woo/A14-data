import pandas as pd

# read accidentInfoList.csv
data = pd.read_csv('accidentInfoList.csv')

# print the first 5 rows of the dataframe
print(data.head())

# filter 사고일시 if it contains 2019, 2020, 2021, 2022 and get data length for each year
print(data[data['사고일시'].str.contains('2019')].shape[0])
print(data[data['사고일시'].str.contains('2020')].shape[0])
print(data[data['사고일시'].str.contains('2021')].shape[0])


