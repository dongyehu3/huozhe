import requests


# # 如果设置成False会报警告，可以设置忽略警告, 下边这个导入urllib3爆红线不会报错
# from requests.packages import urllib3
#
# urllib3.disable_warnings()
res = requests.get('https://www.12306.cn', verify=False)
print(res.status_code, res.encoding)
with open('12306-1.html', 'w', encoding='ISO-8859-1') as f:
    f.write(res.text)

# 也可以设置本地证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组
# res = requests.get(url, cert=('path1', 'path2'))
