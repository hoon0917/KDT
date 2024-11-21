# next_sibling, previous_sibling
# 태그 하나만 반환
# 문자열 마지막에 whitespace(\n,\r등) 있는 경우

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html,'html.parser')

sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print('siblng1:', sibling1)
print(ord(sibling1)) # odr(문자): 문자의 unicode 정수 리턴

# next_sibing.netx_sibling 이용
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.next_sibling
print(sibling2)