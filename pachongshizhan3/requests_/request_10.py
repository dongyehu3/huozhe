from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'haha'
}

headers = {
'User-Agent':'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',

}
s = Session()
# Request对象有个方法叫prepare（），会返回一个准备好的请求对象，但是如果直接session.send这个请求对象的话，不会携带cookies等信息，要想携带就要用session.prepare_request
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)