import requests

data = {
    'name': 'hh',
    'age': '33'
}

r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
print(type(r.request), r.request)