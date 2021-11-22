import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_el_deber(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    data['type'] = 'article'
    data['source'] = url
    data['title'] = utilities.clean_soup(soup.find('h1'))
    data['text'] = ''
    for t in soup.find_all('span', style="mso-ansi-language:ES-MX"):
        data['text'] = data['text'] + clean_soup(t) + ' '
    return json.dumps(data, ensure_ascii=False)