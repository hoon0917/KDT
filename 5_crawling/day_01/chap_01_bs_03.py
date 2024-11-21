from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTtile(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)

    try:
        bsobj = BeautifulSoup(html.read(), 'html.parser')
        value = bsobj.body.find(tag)
    except AttributeError as e:
        return None
    return value

tag='h2'
value = getTtile('https://www.pythonscraping.com/pages/page1.html',tag)

if value == None:
    print(f'{tag} could not found')
else:
    print(value)

# ==> 주어진 url에 h2 태그는 존재하지 않음