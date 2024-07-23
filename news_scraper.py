import requests
from bs4 import BeautifulSoup


def request_news():
    # URL of the website you want to scrape
    url = 'https://rega.gov.sa/'

    # Send a GET request to the website
    response = requests.get(url)

    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main div with the specified classes
    main_div = soup.find('div', class_='news-section')


    news_headlines = {}
    news_content = {}
    news_links = {}
    if main_div:
        # Extract all the text from its children
        c = 1
        for child in main_div.find_all(class_ ="news-title font-bold"):
            news_headlines[c] = child.get_text(strip=True)
            c += 1
            if c > 3:
                break
        c = 1
        for child in main_div.find_all(class_ ="news-brief"):
            news_content[c] = child.get_text(strip=True)
            c += 1
            if c > 3:
                break
        c = 1
        for cild in main_div.find_all(class_ ="site-btn"):
            news_links[c] = cild.get('href')
            c += 1
            if c > 3:
                break

            
    else:
        print("No div found with the specified classes.")


    
    return news_headlines, news_content, news_links

