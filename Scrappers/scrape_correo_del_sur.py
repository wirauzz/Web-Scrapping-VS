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
    for content in soup.find_all('div', class_='cntContent'):
        data = {}
        data['source'] = url
        data['type'] = 'article'
        for title in content.find('h1'):
            data['title'] = title
            
        for text in content.find_all('div', style='text-align: justify;'):
            data['text'] = data['text'] + utilities.clean_soup(text) + ' '      
    return json.dumps(data, ensure_ascii=False)