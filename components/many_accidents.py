import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def parse_polygon_data(polygon_str):
    polygon_json = json.loads(polygon_str)
    coordinates = polygon_json["coordinates"][0]
    return [(lat, lon) for lon, lat in coordinates]

@st.cache_data
def get_data():
    data = pd.read_csv("data/사고다발지.csv")
    return data

def get_color(value, max_value):
    normalized_value = value / max_value
    color = plt.get_cmap('RdYlGn')(1 - normalized_value)
    return mcolors.rgb2hex(color[:3])


def main():
    data = get_data()
    # add 위험도 지수 column
    data['위험도 지수'] = data['사망자수'] * 5 + data['중상자수'] * 2 + data['경상자수'] * 1
    map_center = [data['위도'].mean(), data['경도'].mean()]
    m = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB positron')

    column = st.selectbox(
        "데이터 선택",
        ("위험도 지수", "사고건수", "사상자수", "사망자수", "중상자수", "경상자수", "부상신고자수")
    )
    max_value = data[column].max()

    for index,row in data.iterrows():
        popup_text = f"<h5>{row['시도시군구명']}</h5><br>지점명: {row['지점명']}<br>{column}: {row[column]}"
        radius = (row[column] / max_value) * (20 - 3) + 3
        color = get_color(row[column], max_value)
        folium.CircleMarker(
            location=(row['위도'], row['경도']),
            radius=radius,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.5,
            popup=folium.Popup(popup_text, max_width=500)
        ).add_to(m)

    folium_static(m)

    return m

if __name__ == "__main__":
    main()




