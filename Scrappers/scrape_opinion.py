import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_opinion(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    data['type'] = 'article'
    data['source'] = url
    data['title'] = utilities.clean_soup(soup.find('h2', class_='title'))
    data['text'] = ''
    print(data)
    for d in soup.find_all('div', class_='body pais'):
        for t in d.find_all('p'):
            data['text'] = data['text'] + utilities.clean_soup(d) + ' '
    return json.dumps(data, ensure_ascii=False)