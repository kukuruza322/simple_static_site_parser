# installed BeautifulSoup is needed.
# just run the script and information about all upcoming events from python.org will be display in console.
# enjoy!

import requests
from bs4 import BeautifulSoup as BS


url = 'https://www.python.org/'


def get_info(url):
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    events = soup.find_all('div', class_="medium-widget event-widget last")[0].find_all('li')
    for line in events:
        print(line.text)


get_info(url)
