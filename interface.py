import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Power Metrics Dashboard")

data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40],
    'Other Values': [15, 25, 35, 45]
}
df = pd.DataFrame(data)

fig_bar = px.bar(df, x='Category', y='Values', title="Category vs Values")
fig_line = px.line(df, x='Category', y='Values', title="Category vs Values")
fig_area = px.area(df, x='Category', y='Values', title="Category vs Values")
fig_pie = px.pie(df, names='Category', values='Values', title="Category Distribution")
fig_scatter = px.scatter(df, x='Category', y='Values', size='Other Values', title="Category vs Values with Size")
fig_box = px.box(df, x='Category', y='Values', title="Category vs Values")

col1, col2, col3= st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.plotly_chart(fig_bar, use_container_width=True)
with col2:
    st.plotly_chart(fig_line, use_container_width=True)
with col3:
    st.plotly_chart(fig_area, use_container_width=True)
with col4:
    st.plotly_chart(fig_pie, use_container_width=True)
with col5:
    st.plotly_chart(fig_scatter, use_container_width=True)
with col6:
    st.plotly_chart(fig_box, use_container_width=True)

