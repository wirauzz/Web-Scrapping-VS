import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_el_dia(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    data['type'] = 'article'
    data['source'] = url
    data['title'] = soup.find('h1', class_='')
    data['text'] = ''
    for t in soup.find_all('span', style="color:#000000;"):
        data['text'] = data['text'] + utilities.clean_soup(t) + ' '

    return json.dumps(data, ensure_ascii=False)