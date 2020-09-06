from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit


# # urlparse是用来解析url的， 把url安协议，域名等分开，可以添加scheme参数，当url没有协议名是，会使用此参数的值
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# # 返回的值实际是个元组，可以用下标取值,也可以用.名来取值
# print(result.path, result[5])
#
# # urlunparse接受一个可迭代对象，长度必须为6，否则会报错，返回组装后的url
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))



# # urlsplit和urlparse类似但是不单独解析params，只返回5个结果，params会合并到path中,也返回一个元组类型，和urlparse一样，可以用下标和.名读取
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)
#
# #urlunsplit,接受长度为5的可迭代对象
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))



# urljoin()会将后边那个url补充到前边那个url，无论第一个url有没有该部分都以第二个url为准
# urlencode()将字典转换为url字符串形式，一般用来转换请求参数和post请求体
# parse_qs()将请求参数转换为字典相当于urlencode的逆向
# parse_qsl()将参数转换为元组列表
# quote()将内容转换为url编码的格式有中文时常用
# unquote()quote的逆向

