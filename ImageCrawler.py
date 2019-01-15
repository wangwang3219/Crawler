import requests
from bs4 import BeautifulSoup

target = 'https://unsplash.com/'
req = requests.get(url=target)
print(req.text)