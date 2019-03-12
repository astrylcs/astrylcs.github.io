import os, requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

directory = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(directory, '_data', 'posts.yml')

with open(data_path, 'r') as f:
    last_line = f.readline().strip()

html = requests.get('https://www.facebook.com/astrolojiyolculugu/posts').content

# with open('../../Desktop/a.html') as f:
#     html = f.read()

soup = BeautifulSoup(html, 'html.parser')

links = soup.findAll('a', {'class': '_5pcq'})

for link in links:
    href = link['href']
    if href.startswith('/astrolojiyolculugu'):
        path = urlparse(href).path
        splits = path.split('/')
        value = splits[-1]
        if splits[-1] == '':
            value = splits[-2]
        line = '- ' + value
        if last_line == line:
            break
        print(line)
