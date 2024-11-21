# 링크간 무작위 이동하기

# 임의의 위키 페이지에서 모든 링크 목록 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

random.seed(None)

def getlinks(atricleurl):
    html = urlopen('https://en.wikipedia.org' + atricleurl)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {'id':'bodyContent'})
    wikiurl = bodyContent.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    return wikiurl

links = getlinks('/wiki/Kevin_Bacon')
print('links 길이:', len(links))
while len(links)>0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links=getlinks(newArticle)