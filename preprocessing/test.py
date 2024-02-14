import json

import pandas as pd

# preparing the data
data = pd.read_csv('accident_utf8.csv')

print(data.head())

# filter with 사고다발지역시도시군구 contains 대전광역시

data = data[data['사고다발지역시도시군구'].str.contains('대전광역시')]

# print 사고다발지역폴리곤정보 column
print(data['사고다발지역폴리곤정보'])

# get first row of the column
polygon_str = data['사고다발지역폴리곤정보'].iloc[0]

print(polygon_str)


def fix_json(data_str):
    data_str_valid_json = data_str.replace("type", "\"type\"").replace("coordinates", "\"coordinates\"").replace("Polygon", "\"Polygon\"")

    # Then, replace single quotes with double quotes
    data_str_valid_json = data_str_valid_json.replace("'", "\"")
    return data_str_valid_json

# fix column 사고다발지역폴리곤정보
data['사고다발지역폴리곤정보'] = data['사고다발지역폴리곤정보'].apply(fix_json)

polygon_str = data['사고다발지역폴리곤정보'].iloc[0]
json.loads(polygon_str)

# save the data to a new csv file
data.to_csv('accident_daejeon.csv', index=False)