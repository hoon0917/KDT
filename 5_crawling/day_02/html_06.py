# 형제  : previous_siblings 속성
# 임의의 행을 선택하고 속성을 선택하면 테이블의 이전 행들을 선택

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,'html.parser')

# next_siblings 속성
for sibling in soup.find('tr', {'id':'gift2'}).previous_siblings:
    print(sibling)
    print('-'*30)