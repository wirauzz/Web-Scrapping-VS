import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_la_palabra_del_beni(url, soup):
    print('Scrapping in web {}'.format(url))
    for c in BeautifulSoup(soup, "html.parser").find_all('div', class_='elementor-widget-wrap'):
        data = {}
        data['type'] = 'article'
        data['source'] = url
        data['text'] = ''
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        for text_content in c.find_all('p', attrs={'class': None}):
            data['text'] = data['text'] + utilities.clean_soup(text_content) + ' '        
    print(data)
    return json.dumps(data, ensure_ascii=False)