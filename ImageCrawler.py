from urllib import request
from bs4 import BeautifulSoup
import time
import re
import sys

if __name__ == "__main__":
    #创建txt文件
    file = open('一念永恒.txt', 'w', encoding='utf-8')
    #一念永恒小说目录地址
    target_url = 'http://www.biqukan.com/1_1094/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    time.sleep(20)
    target_html = target_response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(target_html,'lxml')
    #搜索文档树,找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #使用查询结果再创建一个BeautifulSoup对象,对其继续进行解析
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    #计算章节个数
    numbers = (len(download_soup.dl.contents) - 1) / 2 - 8
    print(download_soup.dl.contents)