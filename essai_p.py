import streamlit as st
import plotly.express as px
import pandas as pd
import dash_bio


df_clust = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/clustergram_brain_cancer.csv')



data_sun = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])




df_bar = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Amount': [10, 15, 7, 20]
})


df_scatter = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14],
    'category': ['A', 'B', 'A', 'B', 'A']
})


scatter_fig = px.scatter(df_scatter, x='x', y='y', color='category', title='Sample Scatter Plot')

bar_fig = px.bar(df_bar, x='Fruit', y='Amount', title='Fruit Sales')

sun_fig = px.sunburst(data_sun,names='character',parents='parent',values='value',)

clust = dash_bio.Clustergram(
    data=df_clust,
    column_labels=list(df_clust.columns.values),
    row_labels=list(df_clust.index),
    height=800,
    width=700
)


st.header("Scatter Plot")
st.plotly_chart(scatter_fig)

st.header("Bar Plot")
st.plotly_chart(bar_fig)

st.header("Clustergram")
st.plotly_chart(clust)

st.header("Sunburst Plot")
st.plotly_chart(sun_fig)