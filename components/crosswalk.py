import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from folium.plugins import MarkerCluster, HeatMap

from streamlit_folium import folium_static

@st.cache_data
def get_data():
    data = pd.read_csv("data/횡단보도.csv")
    return data

def main(m):
    st.subheader('대전 내의 횡단보도와 사고다발지의 연관성 분석')

    data = get_data()
    crosswalk_with_signal = data[data['보행자신호등유무'] == 'Y']
    crosswalk_without_signal = data[data['보행자신호등유무'] == 'N']
    crosswalk = data

    # use radio button to select the type of crosswalk
    crosswalk_type = st.radio("신호등 유무", ("전체", "신호등 있는 횡단보도", "신호등 없는 횡단보도"))
    if crosswalk_type == "신호등 있는 횡단보도":
        crosswalk = crosswalk_with_signal
    elif crosswalk_type == "신호등 없는 횡단보도":
        crosswalk = crosswalk_without_signal

    map_center = [data['위도'].mean(), data['경도'].mean()]

    # heap map
    heat_data = [[row['위도'], row['경도']] for index, row in crosswalk.iterrows()]
    HeatMap(heat_data, radius=10).add_to(m)

    folium_static(m)


