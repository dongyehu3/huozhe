import requests

proxies = {
    'http':'代理ip',
    'https': '代理ip'
}
res = requests.get(url, proxies=proxies)

# 如果代理需要认证，那就用http://user:password@host:port这种形式
# proxies = {
#     'http': 'http://username:password@ip:port',
# }