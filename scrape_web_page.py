
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
from Scrappers.scrape_correo_del_sur import scrape_correo_del_sur
from Scrappers.scrape_el_deber import scrape_el_deber
from Scrappers.scrape_el_dia import scrape_el_dia
from Scrappers.scrape_el_diario import scrape_el_diario
from Scrappers.scrape_el_potosi import scrape_el_potosi
from Scrappers.scrape_la_palabra_del_beni import scrape_la_palabra_del_beni
from Scrappers.scrape_la_patria import scrape_la_patria
from Scrappers.scrape_los_tiempos import scrape_los_tiempos
from Scrappers.scrape_noticias_fides import scrape_noticias_fides
from Scrappers.scrape_opinion import scrape_opinion
import utilities
import random
import time
import sys


def get_links():
    links = []
    file = open('Data\\web-urls.text', 'r', encoding='utf-8-sig')
    for link in file:
        links.append(link.strip())
    file.close()
    return links

def scrape_links(base_url, current_url, soup):
    print(base_url)
    print(current_url)
    links = []
    for a in soup.find_all('a'):
        link = ''
        if a.has_attr('href'):
            a['href'] = a['href'].replace('https', 'http')
            if a['href'].startswith(base_url) > 0:
                print("asdasd")
                link = a['href'].replace('\n', '').replace('\r', '').replace('\t', '').strip()
                print("asdasd")
                print(link)
            elif a['href'].find('http') < 0:
                link = current_url + '/' + a['href'].lstrip('/').replace('\n', '').replace('\r', '').replace('\t', '').strip()
                #print(link)
        if (link not in links) and ('!'+link not in links) and (len(link) > 0) and (link.find('reply') < 0) and (link.find('png') < 0) and (link.find('jpg') < 0) and (link.find('pdf') < 0) and (link.find('zip') < 0) and (link.find('oh') < 0) and (link.find('necrologicos') < 0):
            links.append(link)
    print("links obtained from {:}".format(current_url))
    print(links)
    return links

# getlinks -> busco nuevos links -> 
def download(base_url, current_url, cycles):

    #OBTIENE LA PAGINA#
    res = []
    resp = requests.get(current_url)
    content = resp.text
    soup = BeautifulSoup(content, "html.parser")
    print('Fetched page {} with status {}'.format(current_url, resp.status_code))

    if current_url.find('noticiasfides.com') > 0: res.append(scrape_noticias_fides(current_url, soup))

    if current_url.find('correodelsur.com') > 0: res.append(scrape_correo_del_sur(current_url, soup))

    if current_url.find('eldeber.com.bo') > 0: res.append(scrape_el_deber(current_url, soup))

    if current_url.find('eldia.com.bo') > 0: res.append(scrape_el_dia(current_url, soup))

    if current_url.find('eldiario.net') > 0: res.append(scrape_el_diario(current_url, soup))

    if current_url.find('elpotosi.net') > 0: res.append(scrape_el_potosi(current_url, soup))

    if current_url.find('lapalabradelbeni.com.bo') > 0: res.append(scrape_la_palabra_del_beni(current_url, soup))

    if current_url.find('impresa.lapatria.bo') > 0: res.append(scrape_la_patria(current_url, soup))

    if current_url.find('www.lostiempos.com') > 0: res.append(scrape_los_tiempos(current_url, soup))

    if current_url.find('opinion.com.bo') > 0: res.append(scrape_opinion(current_url, soup))


    file = open('Data\\web-data\\' + urlsplit(base_url).netloc + '_data.json', 'a', encoding='utf-8-sig')
    print('{} items added...'.format(len(res)))
    for r in res:  file.write(r + '\n')
    file.close()

    #ABRE EL ARCHIVO DE LINKS QUE SE ENCUENTRA EN DATA#
    # try:
      
    # except:
    #     links = []
    print("Abriendo archivo")
    file = open('Data\\web-urls\\' + urlsplit(current_url).netloc + '_links.txt', 'r', encoding='utf-8')
    links = file.read().splitlines()
    file.close()
    print(type(links))
    already = len(links)
    print('{:} links already listed...'.format(already))


    scrape_links(base_url, current_url ,soup)

    #SE OBSERVAN LOS LINKS QUE SE VISITARON#
    visited = 0
    for l in links:
        if l.startswith('!'):
            visited += 1
    print('{:} new links detected...'.format(len(links)-already))
    print('{:} links in total and {:} visited...'.format(len(links), visited))
    print('{:.1f}% of the site has been scraped...'.format(100 * visited / (len(links)+1)))
    if visited / (len(links)+1) > 0.8 or len(links) < 10:
        print('Most of the site has been scraped. Terminating...')
        sys.exit()
    #SE ESCRIBEN LOS NUEVOS LINKS EN EL ARCHVIO CORRESPONDIENTE#
    with open('Data\\web-urls\\' + urlsplit(current_url).netloc + '_links.txt', 'w', encoding='utf-8') as file:
        for link in links:  file.write(link + '\n')
    file.close()

    if cycles > 0:      
        destination = base_url
        while len(links) > 0:
            r = random.randint(0, len(links) - 1)
            destination = links[r]
            if destination.startswith('!') == False:
                links[r] = '!' + destination
                break
            else:
                time.sleep(1)
                print("Selected an already visited link. Retrying...")
        print('Going to {}\n'.format(destination[:min(100, len(destination))]))

    # Update link list
    with open('Data\\web-urls\\' + urlsplit(base_url).netloc + '_links.txt', 'w', encoding='utf-8') as file:
        for link in links:  file.write(link + '\n')

    if cycles > 0:
        time.sleep(1)
        cycles -= 1
        download(base_url, destination, cycles)



web_pages = []
web_pages = get_links()
link = 1
download(web_pages[link],web_pages[link],10)
# for w in web_pages:
#     download(w,w, 10)



# for running the projectC:\Users\fabri\AppData\Local\Programs\Python\Python310\python.exe 'D:\Universidad\9no Semestre\Taller De Grado 1\Archivo de Codigo\Web Scrapping VS\main.py'