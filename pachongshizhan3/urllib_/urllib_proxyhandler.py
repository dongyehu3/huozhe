from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
import  http.cookiejar, urllib.request


proxy_handler = ProxyHandler({
    # 'http': 'http://127.0.0.1:9743',
    # 'https': 'https://127.0.0.1:9743'
})

# 构建cookiehandler
# 1，构建cookie对象，请求之后 cookie就会存储在这个对象中
cookie = http.cookiejar.CookieJar()
# 2，构建cookiehandler
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = build_opener(proxy_handler)

# add_handler方法可以给opener额外添加handler，也就是构建opener的时候传一个，用add_handler再额外添加其他的handler
opener.add_handler((cookie_handler))

try:
    res = opener.open('http://www.baidu.com')
    print(res.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# 输出cookie
for item in cookie:
    print(item.name + '=' + item.value)

# 将cookie存储为文件
# 1， 构建cookie对象，这时用文件名初始化
cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
# 请求之后。。。。。

# 2，存储cookie
cookie.save(ignore_discard=True, ignore_expires=True)
# 3, 用load（）来读取cookie文件
# 也是先构建cookie对象，然后调用cookie.load(filename)来读取文件
