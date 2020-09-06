import re

content = 'Hello 1234567 World_This is a Regex Demo'

# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group()) # 整个的匹配结果
# print(result.span()) # 匹配的位置

result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1)) # 获取第一个分组的内容
print(result.span())
