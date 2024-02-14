import streamlit as st
import pandas as pd
import altair as alt

# load ../data/교통사고-년도-사유.xlsx
@st.cache_data
def get_data():
    data = pd.read_excel('data/교통사고-년도-사유.xlsx', index_col=0)
    return data

def main():
    st.subheader('사고유형별 사망자수 비교')
    data = get_data()
    # add a column next to the index column that is all True
    data['show'] = True
    data = data[['show'] + [col for col in data.columns if col != 'show']]

    edit_data = st.data_editor(data)

    filtered_data = edit_data[edit_data['show'] == True].drop(columns='show')

    long_data = filtered_data.reset_index().melt(id_vars='구분', var_name='Year', value_name='Accidents')

    # Create an Altair chart
    chart = alt.Chart(long_data).mark_line(point=True).encode(
        x=alt.X('Year:N', axis=alt.Axis(title='Year')),
        y=alt.Y('Accidents:Q', axis=alt.Axis(title='Number of Accidents')),
        color='구분:N',
        tooltip=['구분:N', 'Year:N', 'Deaths:Q']
    ).interactive().properties(
        width=600,
        height=300
    )

    st.altair_chart(chart, use_container_width=True)


if __name__ == '__main__':
    main()


# get column and row names
