import streamlit as st
import plotly.express as px
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/clustergram_brain_cancer.csv')

clust = dash_bio.Clustergram(
    data=df,
    column_labels=list(df.columns.values),
    row_labels=list(df.index),
    height=800,
    width=700
)


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


st.header("Scatter Plot")
st.plotly_chart(scatter_fig)

st.header("Bar Plot")
st.plotly_chart(bar_fig)