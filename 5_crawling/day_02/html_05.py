# 형제  : next_siblings 속성
# 임의의 행을 선택하고 속성을 선택하면 테이블의 다음 행들을 모두 선택

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,'html.parser')

# next_slblings 속성
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
    print('-'*30)