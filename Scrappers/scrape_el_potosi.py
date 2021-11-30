import requests
import json
from bs4 import BeautifulSoup
import utilities

def scrape_el_potosi(url, soup):
    print('Scrapping in web {}'.format(url))
    for c in BeautifulSoup(soup, "html.parser").find_all('div', class_='row nota'):
        data = {}
        data['type'] = 'article'
        data['source'] = url
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        for text_content in c.find('div', class_='content'):
            if(str(text_content) == '<p class="text-center">..........</p>'):
                break
            data['text'] = data['text'] + utilities.clean_soup(text_content) + ' '
    return json.dumps(data, ensure_ascii=False)


