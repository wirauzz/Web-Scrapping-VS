import json
from bs4 import BeautifulSoup
import utilities
from selenium import webdriver

def scrape_el_dia(url, soup):
    print('Scrapping in web {}'.format(url))
    try:
        driver = webdriver.Chrome('C:/Users/fabri/Downloads/chromedriver.exe')
        driver.get(url)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        content = driver.page_source
    except:
        content = ''
        print('webdriver timeout')
    driver.close()

    for c in BeautifulSoup(content, "html.parser").find_all('div', class_='container'):
        data = {}
        data['type'] = 'article'
        data['source'] = url
        for title in c.find_all('h1'):
            data['title'] = utilities.clean_soup(title)
        for text in c.find_all('span', style='color:#000000;'):
            data['text'] = data['text'] + utilities.clean_soup(text) + ' '

    return json.dumps(data, ensure_ascii=False)