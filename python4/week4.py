import urllib.request as ur
from bs4 import *

crc = 0
url = input('Enter URL: ')
rc= int(input('Enter count: '))
pos = int(input('Enter position: '))


def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while crc<rc:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == pos - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    crc += 1
print('Last Url: ', url)
