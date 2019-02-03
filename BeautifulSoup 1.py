import urllib.request
import re
from bs4 import BeautifulSoup

def main():
    url = "http://baike.baidu.com/view/284853.htm"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    # 输出"href"中包含"item"的片段
    for each in soup.find_all(href = re.compile('item')):
        # ','.join[a,b]为'a,b'， ''.join[a,b]即将a和b连接起来中间不留空
        print(each.text, '->', ''.join(['http://baike.baidu.com', each['href']]))
if __name__ == "__main__":
    main()