# 전체 사이트 데이터 수집 소스
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

pages = set()
count = 0
def getlinks(pageurl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageurl))
    bs = BeautifulSoup(html, 'html.parser')
    try :
        print(bs.h1.get_text()) # <h1> 태그 검색
        print(bs.find('div', attrs={'id':'mw-content-text'}).find('p').text)
    except AttributeError as e:
        print(e)

    pattern = '^(/wiki/)((?!:).)*$'
    for link in bs.find_all('a',href=re.compile(pattern)):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print('-'*40)
                count += 1
                print(f'[{count}]: {newpage}')
                pages.add(newpage)
                getlinks(newpage)

getlinks('')

