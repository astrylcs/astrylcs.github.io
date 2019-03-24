import os, requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

directory = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(directory, '_data', 'posts.yml')

with open(data_path, 'r') as f:
    last_line = f.readline().strip()

html = requests.get('https://www.facebook.com/astrolojiyolculugu/posts').content

# with open('./Desktop/a.html') as f:
#     html = f.read()

soup = BeautifulSoup(html, 'html.parser')

links = soup.findAll('a', {'class': '_5pcq'})
paths = [urlparse(link['href']).path for link in links]
values = [path.rstrip('/').split('/')[-1] for path in paths]
lines = ['- ' + value for value in values if value]

try:
    index = lines.index(last_line)
except ValueError:
    print('...')
    index = len(lines)

print(*lines[:index], sep='\n')
