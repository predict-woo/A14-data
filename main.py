import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from folium.plugins import MarkerCluster, HeatMap

# Function to convert polygon data from string to folium compatible format
def parse_polygon_data(polygon_str):
    polygon_json = json.loads(polygon_str)
    coordinates = polygon_json["coordinates"][0]
    return [(lat, lon) for lon, lat in coordinates]

# Streamlit app title
st.title("사고 통계 시각화")

# Specify the path to your CSV file here
csv_file_path = 'pedstrians_utf8.csv'

# Load CSV data
data = pd.read_csv(csv_file_path)

if st.checkbox("데이터 보기", False):
    st.write(data)

st.subheader("Polygon 지도위에 표시하기")
st.markdown("다발지역폴리곤을 지도위에 표시합니다. 보시는 바와 같이, 지도상에 일정한 원형으로 표시됩니다. 따라서, 그냥 위도 경도만 표시하는 것과 다를 점이 없습니다.")

# Initialize a map
map_center = [data['위도'].mean(), data['경도'].mean()]  # Center the map based on the mean latitude and longitude
m = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB positron')

# Add polygons to the map
for index, row in data.iterrows():
    polygon_data = parse_polygon_data(row['다발지역폴리곤'])
    folium.Polygon(locations=polygon_data, color="red", weight=2.5, fill=True, fill_color="red", fill_opacity=0.5).add_to(m)

# Display the map in the Streamlit app
folium_static(m)

st.subheader("경도위도 지도위에 표시하기")
st.markdown("경도위도를 지도위에 표시합니다.")


# Initialize a second map for displaying locations as dots
m_dots = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB positron')  # Using the same center and tiles for consistency

# Add markers to the map
for index, row in data.iterrows():
    folium.CircleMarker(
        location=(row['위도'], row['경도']),
        radius=5,  # You can adjust the size of the dot here
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.7
    ).add_to(m_dots)

# Display the second map in the Streamlit app
folium_static(m_dots)

m_dynamic = folium.Map(location=map_center, zoom_start=12, tiles='CartoDB positron')

# title
st.subheader("데이터 타입에 따른 시각화")
# markdown
st.markdown("사고 통계를 데이터 타입에 따라 볼 수 있습니다")
# Column selection
column = st.selectbox(
    "데이터 선택",
    ("사고건수", "사상자수", "사망자수", "중상자수", "경상자수", "부상신고자수")
)

# Normalize the selected column values for radius visualization
# This ensures the circle sizes are reasonable and visually differentiated
max_value = data[column].max()
min_radius = 3  # Minimum circle radius
max_radius = 50  # Maximum circle radius

def get_color(value, max_value):
    # Normalize the value to a range between 0 and 1
    normalized_value = value / max_value
    # Use matplotlib's colormap to generate a color
    # This example uses the 'RdYlGn' colormap which goes from Red (high) to Yellow (medium) to Green (low)
    # You can choose other colormaps as per your preference
    color = plt.get_cmap('RdYlGn')(1 - normalized_value)  # Subtracting from 1 to invert the scale
    # Convert RGB to hex color using matplotlib.colors
    return mcolors.rgb2hex(color[:3])

# Add dynamic radius markers to the map
for index, row in data.iterrows():
    radius = (row[column] / max_value) * (max_radius - min_radius) + min_radius
    color = get_color(row[column], max_value)  # Get color based on the column value
    popup_text = f"<h4>시도시군구명: {row['시도시군구명']}</h3><br>지점명: {row['지점명']} <br>{column}: {row[column]}"
    folium.CircleMarker(
        location=(row['위도'], row['경도']),
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.5,
        popup=folium.Popup(popup_text, max_width=300)  # Adding a popup here
    ).add_to(m_dynamic)

# Display the map
folium_static(m_dynamic)

# Load the crosswalk data from a CSV file
crosswalks_file_path = 'crosswalk_utf8.csv'
crosswalk_data = pd.read_csv(crosswalks_file_path)

if st.checkbox("데이터 보기", False):
    st.write(crosswalk_data)

# Initialize a map for the crosswalks (or use an existing map object)
map_center_crosswalk = [crosswalk_data['위도'].mean(), crosswalk_data['경도'].mean()]
m_crosswalks = folium.Map(location=map_center_crosswalk, zoom_start=13, tiles='CartoDB positron')

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(m_crosswalks)

# Add markers for crosswalks to the MarkerCluster with popups
for index, row in crosswalk_data.iterrows():
    popup_text = f"도로명: {row['도로명']}<br>횡단보도종류: {row['횡단보도종류']} <br>녹색신호시간: {row['녹색신호시간']}초 <br>적색신호시간: {row['적색신호시간']}초"
    folium.Marker(
        location=(row['위도'], row['경도']),
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(marker_cluster)

st.title("신호등 시각화")

# Display the crosswalk map in the Streamlit app
folium_static(m_crosswalks)

locations = crosswalk_data[['위도', '경도']].values.tolist()

# Create and add a HeatMap layer to the map
heatmap = HeatMap(locations, radius=10)  # You can adjust the radius as needed
m_crosswalks.add_child(heatmap)

# Display the map with the heatmap in the Streamlit app
folium_static(m_crosswalks)