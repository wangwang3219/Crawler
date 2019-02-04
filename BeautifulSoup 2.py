import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def main():
    keyword = input("请输入查询词:")
    keyword = urllib.parse.urlencode({'word':keyword})
    response = urllib.request.Request("http://baike.baidu.com/item/word?%s" % keyword)
    response.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400')
    response = urllib.request.urlopen(response)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")

    for each in soup.find_all('a',href = re.compile('item')):
        content = ''.join([each.text])
        href = urllib.parse.quote(each['href'])
        url2 = ''.join(["http://baike.baidu.com", href])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'lxml')
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, '->', url2])
        print(content)

if __name__ == '__main__':
    main()