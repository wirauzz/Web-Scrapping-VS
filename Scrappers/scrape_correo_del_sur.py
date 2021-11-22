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
    driver = webdriver.Chrome('C:/Users/fabri/Downloads/chromedriver.exe')
    driver.implicitly_wait(5)
    try:
        driver.get(url)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        content = driver.page_source()
    except:
        print('webdriver timeout... ')
        content = ''
    data = {}
    data['type'] = 'article'
    data['source'] = url
    data['title'] = utilities.clean_soup(soup.find('h1'))
    data['text'] = ''
    for d in soup.find_all('div', class_='content'):
        for t in d.find_all('p'):
            data['text'] = data['text'] + utilities.clean_soup(t) + ' '
            
    print(data)
    return json.dumps(data, ensure_ascii=False)