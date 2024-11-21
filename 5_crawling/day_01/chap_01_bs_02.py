# 신뢰할 수 있는 연결과 예외 처리

# 페이지 못 찾는 경우 : HTTPerror
# 서버 못 찾는 경우 : URLerror

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try :
    html = urlopen('http://www.pythonscraping.com/pages/error.html')    # 비정상 페이지
    # html = urlopen('https://www.pythonscraping.com/pages/page1.html') # 정상 페이지
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else :
    print('It worked')
