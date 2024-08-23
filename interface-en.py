import streamlit as st
import pandas as pd
import plotly.express as px
import news_scraper
def home_en():
    logo_url = "https://wetaan.com/assets/img/logo.png"
    st.markdown(
        f"""
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1 style="margin: 0;">Saudi Real Estate Dashboard</h1>
            <img src="{logo_url}" alt="Logo" style="width: 150px; height: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    "<br><br>",unsafe_allow_html=True
    )

# OLD
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






# NEW
    pie = pd.read_excel("Data\\Pie.xlsx")
    bar = pd.read_excel("Data\\bar.xlsx")
    heatmap = pd.read_excel("Data\\heatmap.xlsx")
    scatter = pd.read_excel("Data\\scatter.xlsx")





    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)





# Dummy Data
    # scatter = pd.DataFrame({"X": [1, 2, 3, 4, 5], "Y": [10, 25, 25, 30, 45]})
    line = pd.DataFrame({"X": [1, 2, 3, 4, 5], "Y": [50, 25, 30, 35, 45]})
    area = pd.DataFrame({"X": [1, 2, 3, 4, 5], "Y": [10, 25, 30, 35, 75]})
    # bar = pd.DataFrame({"X": [1,2,3] , "Y": [10, 30, 20]})
    # pie = pd.DataFrame({"X": [1, 2, 3], "Y": [10, 35, 50]})
    box = pd.DataFrame({"X": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], "Y": [10, 90, 30, 40, 50, 160, 200, 220, 250, 300]})
    radar = pd.DataFrame({"X": [1, 2, 3, 4, 5], "Y": [10, 25, 30, 35, 75]})
    # heatmap = pd.DataFrame({"X": [1, 2, 3, 4, 5], "Y": [10, 25, 30, 35, 75]})



    fig_scatter = px.scatter(scatter, x="Num of Rooms", y="Price (SAR)", title="Number of Rooms vs Price")
    fig_area = px.area(area, x="X", y="Y", title="Area Plot")
    fig_line = px.line(line, x="X", y="Y", title="Line Plot")
    fig_bar = px.bar(bar, x=bar.columns[1], y=bar.columns[0], title="Sum of price by City")
    fig_pie = px.pie(pie, names=pie.columns[1], values=pie.columns[0], title="Sum of Area by City")
    fig_box = px.box(box, x="X", y="Y", title="Box Plot")
    fig_radar = px.line_polar(radar, r="Y", theta="X", title="Radar Plot")
    fig_heatmap = px.density_heatmap(heatmap, x="City", y="City", z="Sum of Area", title="Sum of Area by City", )








    with col1:
        st.plotly_chart(fig_scatter, use_container_width=True)
    with col2:
        st.plotly_chart(fig_line, use_container_width=True)
    with col3:
        st.plotly_chart(fig_area, use_container_width=True)
    with col4:
        st.plotly_chart(fig_bar, use_container_width=True)
    with col5:
        st.plotly_chart(fig_pie, use_container_width=True)
    with col6:
        st.plotly_chart(fig_treemap, use_container_width=True)
    with col7:
        st.markdown(
            """
    <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
        <div style="text-align: center; display: flex; flex-direction: column; align-items: center;">
            <p style="font-size: 24px;">Total Property Value</p>
            <h2 style="font-size: 64px; margin: 0;">308M SAR</h2>
        </div>
    </div>

            """
, unsafe_allow_html=True)


    with col8:
        st.plotly_chart(fig_box, use_container_width=True)
    with col9:
        st.plotly_chart(fig_heatmap, use_container_width=True)





    # st.markdown("<br><br>", unsafe_allow_html=True)
    # st.title("News")

    # # Request news headlines and content
    # news_headlines, news_content, news_links = news_scraper.request_news()
    # base_url = 'https://rega.gov.sa'


    # st.markdown("""
    #     <link href="//db.onlinewebfonts.com/c/6b75b24d502dab23003320c2e1b2fc68?family=Adobe+Arabic" rel="stylesheet" type="text/css"/>
    #     <style>
    #         .card {
    #             border: 1px solid #686D76;
    #             padding: 10px;
    #             margin: 10px 0;
    #             border-radius: 5px;
    #             display: flex;
    #             flex-direction: column;
    #             justify-content: space-between;
    #             height: 400px; /* Fixed height for all cards */
    #             overflow: hidden; /* Ensure content fits within the card */
    #             font-family: 'Adobe Arabic', sans-serif;
    #             cursor: pointer;
    #             text-decoration: none;
    #             color: inherit;
    #         }
    #         .card-header {
    #             text-align: center;
    #             color: #F5F7F8;
    #             padding: 10px;
    #             border-radius: 5px 5px 0 0;
    #             font-family: 'Adobe Arabic', sans-serif;
    #             font-weight: bold;
    #             font-size: 1.6em;
    #         }
    #         .card-content {
    #             padding: 10px;
    #             flex-grow: 1;
    #             font-family: 'Adobe Arabic', sans-serif;
    #             overflow: auto; /* Enable scrolling if content overflows */
    #             font-size: 1.4em;
    #             color: #F5F7F8;
    #         }
    #         .card hr {
    #             border: 1px solid #686D76;
    #             margin: 10px 0;
    #         }
    #     </style>
    # """, unsafe_allow_html=True)

    # with st.container():
    #     news_col1, news_col2, news_col3 = st.columns(3)

    #     with news_col1:
    #         st.markdown(f"""
    #         <a href="{base_url}{news_links[1]}" target="_blank" class="card">
    #             <div class="card-header">{news_headlines[1]}</div>
    #             <hr>
    #             <div class="card-content">{news_content[1]}</div>
    #         </a>
    #         """, unsafe_allow_html=True)

    #     with news_col2:
    #         st.markdown(f"""
    #         <a href="{base_url}{news_links[2]}" target="_blank" class="card">
    #             <div class="card-header">{news_headlines[2]}</div>
    #             <hr>
    #             <div class="card-content">{news_content[2]}</div>
    #         </a>
    #         """, unsafe_allow_html=True)

    #     with news_col3:
    #         st.markdown(f"""
    #         <a href="{base_url}{news_links[3]}" target="_blank" class="card">
    #             <div class="card-header">{news_headlines[3]}</div>
    #             <hr>
    #             <div class="card-content">{news_content[3]}</div>
    #         </a>
    #         """, unsafe_allow_html=True)
