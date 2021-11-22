import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_la_patria(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    data['type'] = 'article'
    data['source'] = url
    data['title'] = clean_soup(soup.find('h1', class_='text-200'))
    data['text'] = ''
    for t in soup.find_all('p', style="margin: 0 auto; padding: 0px 5px 15px 0px;"):
        data['text'] = data['text'] + utilities.clean_soup(t) + ' '
    return json.dumps(data, ensure_ascii=False)