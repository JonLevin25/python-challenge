import requests
from bs4 import BeautifulSoup
import pickle
import re
import urllib3
import os

url = "http://www.pythonchallenge.com/pc/def/peak.html"
filename = 'banner.p'

def save_pickle_from_url(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag = soup.find('peakhell')
    file = tag['src']

    url_directory = os.path.split(url)[0]
    url_file = f'{url_directory}/{file}'
    response = requests.get(url_file)
    with open(filename, 'wb+') as file:
        file.write(response.content)

def get_pickle_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

if __name__ == '__main__':
    # save_pickle_from_url(url, filename)
    data = get_pickle_from_file(filename)

    parsed = pickle.loads(data)
    processed = [[(tup[0], chr(tup[1]))for tup in p] for p in parsed]
    for p in parsed:
        for c, count in p:
            print(c * count, end='')
        print()

