
import string
from bs4 import BeautifulSoup

def clean_soup(soup):
    t = soup.get_text(separator=' ')
    t = t.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('\"', ' ').replace('\'', ' ').strip()
    while '  ' in t:
        t = t.replace('  ', ' ')
    return t