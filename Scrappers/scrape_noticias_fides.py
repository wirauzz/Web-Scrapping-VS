import json
from bs4 import BeautifulSoup
import utilities


def scrape_noticias_fides(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    for c in soup.find_all('div', class_='cntContent'):
        data['type'] = 'article'
        data['source'] = url
        data['text'] = ' '
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        
        for text in c.find_all('div', style="text-align: justify;"):
            data['text'] = data['text'] + utilities.clean_soup(text) + ' '
    return json.dumps(data, ensure_ascii=False)
