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

current_url = 'https://twitter.com/evoespueblo'
driver.maximize_window()
driver.implicitly_wait(5)

# load the website
try:
    driver.get(current_url)
    #os.system("pause")
    time.sleep(2)
    for item in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
    content = driver.page_source
except:
    print('webdriver timeout... ')
    content = ''

# close the driver

result = [] 
for t in BeautifulSoup(content, "html.parser").find_all('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'):

    dm = {}
    dm["type"] = 'tw_post'
    dm["source"] = current_url
    dm["text"] = utils.clean_soup(t)

    result.append(dm)




print("Data scrapped")
for r in result:
    print(r)
    print()