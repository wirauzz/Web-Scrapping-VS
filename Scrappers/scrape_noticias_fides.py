import requests
import json
from bs4 import BeautifulSoup
import utilities


def scrape_noticias_fides(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    for c in BeautifulSoup(soup, "html.parser").find_all('section', attrs={'class': None}):
        data['type'] = 'article'
        data['source'] = url
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        
        text_content = c.find('span', {"id": "contentN"})
        for text in text_content.find_all('p'):
            data['text'] = data['text'] + utilities.clean_soup(text) + ' '
    return json.dumps(data, ensure_ascii=False)
