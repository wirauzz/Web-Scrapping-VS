from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import utilities as utils
import time, json, os
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/fabri/Downloads/chromedriver.exe')


##current_url = 'https://www.facebook.com/groups/8080169598'

current_url = 'https://twitter.com/LosTiemposBol'
driver.maximize_window()
driver.implicitly_wait(5)

# load the website
try:
    driver.get(current_url)
    #os.system("pause")
    time.sleep(2)
    result = [] 
    for item in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
        content = driver.page_source

        for tweets in BeautifulSoup(content, 'html.parser').find_all('article'):
            dm = {}
            dm["type"] = 'tw_post'
            dm["source"] = current_url
            for author in tweets.find('div', class_='css-901oao r-1awozwy r-1fmj7o5 r-6koalj r-37j5jr r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-1udh08x r-3s2u2q r-qvutc0'):
                dm["author"] = utils.clean_soup(author)
            for date in tweets.find_all('time'):
                if date.has_attr('datetime'):
                    dm["date"] = date['datetime']
            for text in tweets.find_all('div', class_='css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'):
                dm['text'] = utils.clean_soup(text)
            result.append(dm)
except:
    print('webdriver timeout... ')
    content = ''

# close the driver



print("Data scrapped")
for r in result:
    print(r)
    print()