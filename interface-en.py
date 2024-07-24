import streamlit as st
import pandas as pd
import plotly.express as px
import news_scraper

st.set_page_config(layout="wide")
logo_url = "https://wetaan.com/assets/img/logo.png"
st.markdown(
    f"""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1 style="margin: 0;">لوحة العقار السعودي</h1>
        <img src="{logo_url}" alt="Logo" style="width: 150px; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
 "<br><br>",unsafe_allow_html=True
)

df = pd.read_excel("datafile.xlsx")
df_prop_by_price = pd.read_csv("Sum of Total Property Value by Property Type.csv")
df_deals_by_city = pd.read_csv("Sum of Number of Deals by City.csv")
df_price_by_city = pd.read_csv("Sum of Highest Avg Price by City.csv")
df_deals_by_property = pd.read_csv("Sum of Number of Deals by Property Type.csv")
df_propery_value = pd.read_csv("Sum of Total Property Value by City.csv") 

fig_prop_price = px.bar(df_prop_by_price, x='Property Type', y='Sum of Total Property Value', title="Property Type vs Sum of Total Property Value")
fig_pie = px.pie(df_deals_by_property, names='Property Type', values='Sum of Number of Deals', title="Property Types by Number of Deals")
fig_bar_city = px.bar(df_deals_by_city, x='City', y='Sum of Number of Deals', title="City vs Sum of Number of Deals")
fig_treemap = px.treemap(df_propery_value, path=['City'], values='Sum of Total Property Value', title='Sum of Total Property Value by City')
fig_pie_price = px.pie(df_price_by_city, names='City', values='Sum of Highest Avg Price', title="City vs Sum of Highest Avg Price")
fig_box = px.box(df, x='Property Type', y='Average Rental Contract Price (Thousand SAR/Unit)', title="Property Type vs Average Rental Contract Price")


col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.plotly_chart(fig_prop_price, use_container_width=True)
with col2:
    st.plotly_chart(fig_bar_city, use_container_width=True)
with col3:
    st.plotly_chart(fig_treemap, use_container_width=True)
with col4:
    st.plotly_chart(fig_pie, use_container_width=True)
with col5:
    st.plotly_chart(fig_pie_price, use_container_width=True)
with col6:
    st.plotly_chart(fig_box, use_container_width=True)


st.markdown("<br><br>", unsafe_allow_html=True)
st.title("News")

# Request news headlines and content
news_headlines, news_content, news_links = news_scraper.request_news()
base_url = 'https://rega.gov.sa'


st.markdown("""
    <link href="//db.onlinewebfonts.com/c/6b75b24d502dab23003320c2e1b2fc68?family=Adobe+Arabic" rel="stylesheet" type="text/css"/>
    <style>
        .card {
            border: 1px solid #686D76;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 400px; /* Fixed height for all cards */
            overflow: hidden; /* Ensure content fits within the card */
            font-family: 'Adobe Arabic', sans-serif;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
        }
        .card-header {
            text-align: center;
            color: #F5F7F8;
            padding: 10px;
            border-radius: 5px 5px 0 0;
            font-family: 'Adobe Arabic', sans-serif;
            font-weight: bold;
            font-size: 1.6em;
        }
        .card-content {
            padding: 10px;
            flex-grow: 1;
            font-family: 'Adobe Arabic', sans-serif;
            overflow: auto; /* Enable scrolling if content overflows */
            font-size: 1.4em;
            color: #F5F7F8;
        }
        .card hr {
            border: 1px solid #686D76;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    news_col1, news_col2, news_col3 = st.columns(3)

    with news_col1:
        st.markdown(f"""
        <a href="{base_url}{news_links[1]}" target="_blank" class="card">
            <div class="card-header">{news_headlines[1]}</div>
            <hr>
            <div class="card-content">{news_content[1]}</div>
        </a>
        """, unsafe_allow_html=True)

    with news_col2:
        st.markdown(f"""
        <a href="{base_url}{news_links[2]}" target="_blank" class="card">
            <div class="card-header">{news_headlines[2]}</div>
            <hr>
            <div class="card-content">{news_content[2]}</div>
        </a>
        """, unsafe_allow_html=True)

    with news_col3:
        st.markdown(f"""
        <a href="{base_url}{news_links[3]}" target="_blank" class="card">
            <div class="card-header">{news_headlines[3]}</div>
            <hr>
            <div class="card-content">{news_content[3]}</div>
        </a>
        """, unsafe_allow_html=True)
