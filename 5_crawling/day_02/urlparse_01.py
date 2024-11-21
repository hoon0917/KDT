# 인터넷 크롤링 : URL 구조

from urllib.request import urlparse

urlsting1 = 'https://shopping.naver.com/home/p/index.naver'

url = urlparse(urlsting1)
print(url.scheme)
print(url.netloc)
print(url.path)