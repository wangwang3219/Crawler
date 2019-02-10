import re
import json
from bs4 import BeautifulSoup
from urllib import request, parse

if __name__ == '__main__':
    ip = 'https://v.qq.com/x/cover/0hrejqzlvdyr03k/d00277okb4u.html?'
    get_url = 'http://www.90go.org/x2/tong.php?url=%s' % ip

    get_movie_url = 'http://www.90go.org/x2/api.php'

    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
        'Referer':'http://www.90go.org/x2/tong.php?url=%s' % ip
    }

    get_url_req = request.Request(url = get_url, headers = head)
    get_url_response = request.urlopen(get_url_req)
    get_url_html = get_url_response.read().decode('utf-8')
    bf = BeautifulSoup(get_url_html, 'lxml')

    a = str(bf.find_all('script'))

    pattern = re.compile("url : '(.+)',", re.IGNORECASE)
    url = pattern.findall(a)[0]

    get_movie_data = {
        'up':'0',
        'url':'%s' % url,
    }
    get_movie_req = request.Request(url = get_movie_url, headers = head)
    get_movie_data = parse.urlencode(get_movie_data).encode('utf-8')
    get_movie_response = request.urlopen(get_movie_req, get_movie_data)
    get_movie_html = get_movie_response.read().decode('utf-8')
    print(get_movie_data['url'])