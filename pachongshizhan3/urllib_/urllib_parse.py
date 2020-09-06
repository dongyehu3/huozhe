from urllib.parse import urlparse, urlencode, urljoin, quote
from urllib.request import urlopen

# 要想使用urllib拼接查询参数的话只能先把查询字典用urlencode转换为字符串，然后用手动拼接的方法，
params = {'wd': '哈哈', 'ie': 'utf-8'}
url_2 = 'http://httpbin.org/get?wd=哈哈'
print(quote(url_2)) # 把url编码

result = urlencode(params)
print(result)
url = 'http://httpbin.org/get'
url_1 = url + '?' + result
print(url_1)
res = urlopen(url_1)
print(res.read().decode('utf8'))