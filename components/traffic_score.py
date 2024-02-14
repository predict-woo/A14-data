import streamlit as st
import pandas as pd
import altair as alt


@st.cache_data
def get_data():
    df_traffic = pd.read_csv("data/교통지수.csv")
    return df_traffic


def main():
    data = get_data()

    color_scale = alt.Scale(domain=[min(data['교통 안전 지수']), max(data['교통 안전 지수'])],
                            range=['#4A74B4', 'white', '#D4322C'])

    # Create an Altair chart
    chart = alt.Chart(data).mark_bar().encode(
        x='지역:N',
        y='교통 안전 지수:Q',
        color=alt.Color('교통 안전 지수:Q', scale=color_scale, legend=alt.Legend(title="교통 안전 지수")),
        tooltip=['지역:N', '교통 안전 지수:Q']
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)


if __name__ == '__main__':
    main()
