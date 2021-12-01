from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json, time
from bs4 import BeautifulSoup
import utilities

def scrape_correo_del_sur(url, soup):
    print('Scrapping in web {}'.format(url))
    data = {}

    for c in soup.find_all('div', class_='row nota'):
        data_content = {}
        data['source'] = url
        data['type'] = 'article'
        data['text'] = ''
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        for text_content in c.find_all('p', attrs={'class': None}):
            data['text'] = data['text'] + utilities.clean_soup(text_content) + ' '   

    print(data)
    return json.dumps(data, ensure_ascii=False)