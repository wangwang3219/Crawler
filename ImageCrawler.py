import chardet
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)