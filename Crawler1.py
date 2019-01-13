import requests
from bs4 import BeautifulSoup

target = 'http://www.biqukan.com/1_1094/5403177.html'
req = requests.get(url = target)
html = req.text
bf = BeautifulSoup(html, "html5lib")
texts = bf.find_all('div', class_ = 'showtxt')
print(texts[0].text.replace('\xa0'*8,''))
