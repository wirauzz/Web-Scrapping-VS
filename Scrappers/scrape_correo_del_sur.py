import json
from bs4 import BeautifulSoup
import utilities

def scrape_correo_del_sur(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    for c in soup.find_all('div', class_='row nota'):
        data['source'] = url
        data['type'] = 'article'
        data['text'] = ''
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        for text_content in c.find_all('p', attrs={'class': None}):
            data['text'] = data['text'] + utilities.clean_soup(text_content) + ' '   
    return json.dumps(data, ensure_ascii=False)