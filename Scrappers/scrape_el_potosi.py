import requests
import json
from bs4 import BeautifulSoup
import utilities

def scrape_el_potosi(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    data['type'] = 'article'
    data['source'] = url
    data['title'] = clean_soup(soup.find('h1'))
    data['text'] = ''
    for d in soup.find_all('div', class_='content'):
        for t in d.find_all('p'):
            data['text'] = data['text'] + utilities.clean_soup(t) + ' '
    print(data)
    return json.dumps(data, ensure_ascii=False)


