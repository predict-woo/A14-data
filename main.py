import streamlit as st
import pandas as pd
from components.reason_year_accident import main as reason_year_accident
from components.traffic_score import main as traffic_score
from components.reason_death_hurt import main as reason_death_hurt
from components.many_accidents import main as many_accidents
from components.crosswalk import main as crosswalk
def main():
    st.title("데이터 시각화 미션")
    st.write("\n\n")
    traffic_score()
    st.write("\n\n")
    reason_year_accident()
    st.write("\n\n")
    reason_death_hurt()
    st.write("\n\n")
    m = many_accidents()
    st.write("\n\n")
    crosswalk(m)

if __name__ == '__main__':
    main()