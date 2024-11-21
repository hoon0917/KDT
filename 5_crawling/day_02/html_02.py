# CSS속성을 이용한 태그 검색(등장인물의 이름 색깔이 초록색인 것을 이용한 등장 인물 검색)
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

# 등장인물의 이름 : 녹색
name_list = soup.find_all('span', {'class':'green'})
for name in name_list:
    print(name.string)

# find_all(string='검색어')
# string을 통해 tag없이 바로 텍스트 검색
# 검색어 : the prince

prince_lsit=soup.find_all(string='the prince')
print(prince_lsit)
print('the prince_list:', len(prince_lsit))