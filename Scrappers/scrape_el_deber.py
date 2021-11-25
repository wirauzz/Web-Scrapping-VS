import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_el_deber(url, soup):
    print('Scrapping in web {}'.format(url))
    for content in soup.find_all('div', class_='scroller-holder'):
        data = {}
        data['type'] = 'article'
        data['source'] = url
        for title in content.find('h1'):
            data['title'] = utilities.clean_soup(title)
            
        for text in content.find_all('p'):
            data['text'] = data['text'] + utilities.clean_soup(text) + ' '        
    

    return json.dumps(data, ensure_ascii=False)