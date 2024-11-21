# 멜론 웹사이트 접근 #2
# 사용자 정보 추가해서 웹사이트가 로봇으로 인식 못하도록 했음

from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup


# 샘플 코드 1
# urllib.error.HTTPError: HTTP Error 406: Not Acceptable 발생



melon_url = 'https://www.melon.com/chart/index.htm'
urlrequest = Request(melon_url, headers={'User-Agent':'Mozilla/5.0'})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
print(soup)