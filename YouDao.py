import json
import urllib.parse
import urllib.request

def trans():
    content = input("请输入需要翻译的内容：")
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1508333076510'
    data['sign'] = '1b4945929576aa885ae480f99cc87a3f'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    html = json.loads(html)
    target = html['translateResult'][0][0]['tgt']
    print("翻译结果：%s" % target)

trans()
while(1):
    value = input("是否需要继续翻译：Y/N ? \n")
    if value == 'N':
        break
    elif value == 'Y':
        trans()
    else:
        print('输入错误')