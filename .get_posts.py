import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# html = requests.get('https://www.facebook.com/astrolojiyolculugu/posts').content

with open('../../Desktop/a.html') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

links = soup.findAll('a', {'class': '_5pcq'})

for link in links:
    href = link['href']
    if href.startswith('https://www.facebook.com/astrolojiyolculugu'):
        path = urlparse(href).path
        splits = path.split('/')
        value = splits[-1]
        if splits[-1] == '':
            value = splits[-2]
        print('- '+value)