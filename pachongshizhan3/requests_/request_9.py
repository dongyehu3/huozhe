import requests


# # 设置超时， timeou是连接和读取的时间总和， 分开指定可以传入一个元组（x, y）
# r = requests.get(url, timeout=timeout)
#
# # 设置认证
# r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
from requests.auth import HTTPBasicAuth

r = requests.get('https://github.com/login', auth=HTTPBasicAuth('dongyehu3', 'destroyer3C'))
# 或者
r = requests.get(url, auth=('username', 'password'))


print(r.status_code)
print(r.text)
print(r.cookies)
login = requests.get('https://github.com/notifications', cookies=r.cookies)
print(login.text)