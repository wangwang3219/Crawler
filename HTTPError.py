from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.huya.com/WangWang3219.html"
    try:
        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        print(html)
    except error.HTTPError as e:
        print(e.code)