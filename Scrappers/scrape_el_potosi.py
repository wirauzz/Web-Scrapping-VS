import json
from bs4 import BeautifulSoup
import utilities

def scrape_el_potosi(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}
    for c in soup.find_all('div', class_='row nota'):

        data['type'] = 'article'
        data['source'] = url
        data['text'] = ' '
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        article = c.find('div', class_='content')
        if(article):
            for text_content in article.find_all('p'):
                if(str(text_content).find('..........') > 0):
                    return json.dumps(data, ensure_ascii=False)
                data['text'] = data['text'] + utilities.clean_soup(text_content) + ' '
    return json.dumps(data, ensure_ascii=False)


