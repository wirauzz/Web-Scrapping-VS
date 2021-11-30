import requests
import json
from bs4 import BeautifulSoup
import utilities

def scrape_los_tiempos(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    for c in BeautifulSoup(soup, "html.parser").find_all('article'):
        data['type'] = 'article'
        data['source'] = url
        data['text'] = ''
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
            print(title)
        for text_content in c.find_all('p', class_= "rtejustify"):
            data['text'] = data['text'] + utilities.clean_soup(text_content) + ' ' 
    return json.dumps(data, ensure_ascii=False)
