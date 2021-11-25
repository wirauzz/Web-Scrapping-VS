import requests
import json
from bs4 import BeautifulSoup
import utilities
from selenium import webdriver

def scrape_el_diario(url, soup):
    print('Scrapping in web {}'.format(url))
    for c in BeautifulSoup(soup, "html.parser").find_all('div', class_='jeg_main_content col-md-8'):
        data = {}
        data['type'] = 'article'
        data['source'] = url
        for title in c.find_all('h1', class_='jeg_post_title'):
            data['title'] = utilities.clean_soup(title)
        if(c.find('div', class_='content-inner')):
            for text in c.find_all('p'):
                data['text'] = data['text'] + utilities.clean_soup(text) + ' '

    return json.dumps(data, ensure_ascii=False)