import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_opinion(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    for c in soup.find_all('div', class_='inner-content col-md-8 col-sm-7 col-ms-12 col-xs-12'):
        data['type'] = 'article'
        data['source'] = url
        for title in c.find_all('h2'):
            data['title'] = utilities.clean_soup(title)
        text_content = c.find('div', class_="body")
        if(text_content):
            for text in text_content.find_all('p'):
                data['text'] = data['text'] + utilities.clean_soup(text) + ' '
            
    return json.dumps(data, ensure_ascii=False)