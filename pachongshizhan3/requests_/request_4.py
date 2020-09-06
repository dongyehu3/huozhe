import requests


# # 传文件
# files = {'file': open('filename', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# 获取和设置cookies
r = requests.get('http://www.baidu.com')
print(r.cookies)

# for 不会开辟作用域，但是推导式会
for item in r.cookies.items():
    print(*item)
# 设置cookies
jar = requests.cookies.RequestsCookieJar()
jar.set(*item)

# 设置cookies可以用字典也可以用cookiejar对象
r = requests.get('http://www.baidu.com', cookies=jar)
print(r.text)