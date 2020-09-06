import requests
import re

headers = {
'User-Agent':'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
}

url = 'http://httpbin.org/'
r = requests.get(url + 'get', headers=headers, params='哈哈')
pattern = re.compile('"origin":.*?\d{3}\.\d{3}\.\d{3}\.\d{2}')
ip = pattern.search(r.text)
print(ip)
print(r.content, type(r.content))
print(r.text, type(r.text))
