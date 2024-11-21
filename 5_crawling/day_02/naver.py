# 네이버 블로그에 ChatGPT 검색 하면 나오는 제목하고 url, 간단한 내용 출력

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
# 검색어에 한글 쓰고 싶으면 from urllib.parse import quete
# query = quote('챗지피티) # 한글 검색어 전달

query='ChatGPT'
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'

html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
blog_results = soup.select('a.title_link') # 검색된 블로그의 타이틀
print('검색 결과 수:', len(blog_results))
search_count = len(blog_results)
desc_results = soup.select('a.dsc_link') # 검색된 블로그 결과의 간단한 설명

for i in range(search_count):
    title = blog_results[i].text
    link = blog_results[i]['href']
    print(f'{title}, [{link}]') # 제목하고, url
    print(desc_results[i].text) # 간단한 설명
    print('-'*80)
