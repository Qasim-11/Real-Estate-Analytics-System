import streamlit as st
import pandas as pd
import plotly.express as px
import news_scraper

def news():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("الأخبار")

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
