# beautifulsoup에 정규식을 활용

## 제품 이미지 검색
## <img src='...'> 태그의 속성['src'] 사용

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

# 정규식: img 다음에 임의의 한 문자가 0회 이상
img_tag = re.compile('/img/gifts/img.*.jpg')
# find_all()에서 img의 src 속성값에 정규식 사용
images = soup.find_all('img', {'src':{img_tag}})

for image in images :
    print(image, end=" -> ['src']속성값:")
    print(image['src'])