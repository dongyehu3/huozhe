import requests


url = 'http://httpbin.org/'
# r = requests.get(url + 'get')
# # 自动解码
# print(r.text)

data = {
    'name': 'haha',
    'age': 33
}
# 带参数的get请求
r = requests.get(url + 'get', params=data)
print(r.text)
# 自动把json格式的返回数据解析成字典,不是json格式的话会报错json.decoder.JSONDecodeError
print(r.json(), type(r.json()))
