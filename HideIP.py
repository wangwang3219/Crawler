import urllib.request

if __name__ == "__main__":
    #访问网址
    url = 'https://ip.cn/'
    #创建ProxyHandler
    proxy_support = urllib.request.ProxyHandler({'https':'218.17.139.5:808'})
    #创建Opener
    opener = urllib.request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36')]
    #安装OPener
    urllib.request.install_opener(opener)
    #使用自己安装好的Opener
    response = urllib.request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)