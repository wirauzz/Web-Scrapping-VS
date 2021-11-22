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

current_url = 'https://www.facebook.com/GrupoELDEBER/'
driver.maximize_window()
driver.implicitly_wait(5)

# load the website
try:
    driver.get(current_url)
    #os.system("pause")
    #time.sleep(1)
    for item in range(1):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #time.sleep()
    content = driver.page_source
except:
    print('webdriver timeout... ')
    content = ''

# close the driver
driver.close()

result = [] 
for t in BeautifulSoup(content, "html.parser").find_all('div', class_='_5pbx userContent _3576'):

    dm = {}
    dm["type"] = 'fb_post'
    dm["source"] = current_url
    dm["text"] = utils.clean_soup(t)

    result.append(dm)


for t in BeautifulSoup(content, "html.parser").find_all('div', class_='ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a'):
    dm = {}
    dm["type"] = 'fb_post'
    dm["source"] = current_url
    dm["text"] = utils.clean_soup(t)
    result.append(dm)


print("Data scrapped")
print(result)