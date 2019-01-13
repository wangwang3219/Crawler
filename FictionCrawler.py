import requests
from bs4 import BeautifulSoup

server = 'http://www.biqukan.com/'
ret = requests.get('https://www.biqukan.com/1_1408/')
html = ret.text
bf = BeautifulSoup(html,'html.parser')
texts = bf.find_all('div',class_='listmain')
a_bf = BeautifulSoup(str(texts[0]),'html.parser')
a_texts = a_bf.find_all('a')
self_nums = len(a_texts[13:])
for each in a_texts[13:]:
    try:
        print(each.string, server + each.get('href'))
        download_req = requests.get(str(server + each.get('href')))
        download_html = download_req.text
        download_bf = BeautifulSoup(download_html, 'html.parser')
        download_text = download_bf.find_all('div', class_='showtxt')
        download_text = download_text[0].text.replace('\xa0' * 8, '\n\n')
        with open('E:/python/Data/飞剑问道.txt', 'a', encoding='utf-8') as f:
            f.write(each.string + '\n')
            f.writelines(download_text)
            f.write('\n\n')
    except:
        continue