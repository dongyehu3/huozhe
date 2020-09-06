from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
'User-Agent':'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
'Host':'httpbin.org'
}

dict = {
    'name': 'haha'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')

# headers不用转为bytes，但是data需要，urlopen没有headers参数,想传递headers必须用Request对象
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 额外添加headers
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)')

response = request.urlopen(req)
print(response.read().decode('utf-8'))
