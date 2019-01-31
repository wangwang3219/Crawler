import json
import urllib.parse
import urllib.request

def trans():
    content = input("请输入需要翻译的内容：")
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['i'] = content
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    # Form_Data['sign'] = '1b4945929576aa885ae480f99cc87a3f'
    # Form_Data['salt'] = '1508333076510'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTION'
    Form_Data['typoResult'] = 'true'
    # 使用urlencode方法转换标准格式
    data = urllib.parse.urlencode(Form_Data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    response = urllib.request.urlopen(url, data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 将已编码的 JSON 字符串解码为 Python 对象
    html = json.loads(html)
    # 找到翻译结果
    target = html['translateResult'][0][0]['tgt']
    # 打印翻译信息
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