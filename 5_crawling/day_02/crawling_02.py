# Kevin Bacon 위키피디아 URL

# 임의의 위키 페이지에서 모든 링크 목록 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
body_content = bs.find('div', {'id':'bodyContent'})

pattern = '^(/wiki/)((?!:).)*$'
for link in body_content.find_all('a', href = re.compile(pattern)):
    if 'href' in link.attrs:
        print(link.attrs['href'])