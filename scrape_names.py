#!usr/bin/env python2

import requests
from bs4 import BeautifulSoup
import time

with open('names_to_scrape.txt', 'r') as f:
    names = f.read().split('\n')

url = 'http://dndlookup.dartmouth.edu/datapage_dartmouth.php'
names_file = open('scraped_names.txt', 'a')

for name in names:
    params = {'name': name, 'fmat': '1'}
    response = requests.get(url, params=params)

    html = BeautifulSoup(response.text)

    if html.find('a'):
        names_file.write(html.find('a').text + '\n')
        print html.find('a').text

    time.sleep(5)

names_file.close()
