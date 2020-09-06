import re
import json
import requests

# img class="board-img" src="src"

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):

    pattern = re.compile('<dd>.*?>(\d+?)<.*?data-src="(.*?)".*?"name".*?a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?integer.*?>(.*?)</.*?fraction.*?>(.*?)</.*?</dd>', re.S)
    result = pattern.findall(html)

    for item in result:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip(),
            'time': item[4].strip(),
            'score': item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i * 10)