html_example='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

from bs4 import BeautifulSoup

# <head> 태그 검색
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())

print('-------------select_one() 함수 -------------------------')
# 첫 번째 <h1> 태그 검색
h1 = soup.select_one('h1') # 첫 번째 <h1> 태그 검색
print(h1)

# select_one() 함수 예제
# <h1> 태그의 id 검색 : #id
## <h1> 태그의 id가 'footer' 인 항목 추출
footer = soup.select_one('h1#footer')
print(footer)

# 클래스 이름 검색 : 태그.클래스 이름
class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.string)
print(class_link['href'])


# 계층적 하위 태그 접근 #1
## 부모태그 > 자식태그 형식으로 접근 : 태그가 단계적으로 존재할 때
link1 = soup.select_one('div#link > a.external_link')
print(link1)

##find() 함수와 비교
link_find = soup.find('div',{'id':'link'})

external_link = link_find.find('a',{'class':'external_link'})
print('find external_link:', external_link)

print('---------------------------------------')
# 계층적 하위 태그 접근 #2 : 공백으로 하위 태그 선언
# 상위태그 하위태그 형식으로 접근 : 자손 관계의 하위 태그
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)

#<div id='link> 내부의 <a class='internal_link> 검색
internal_link = soup.select_one('div#link a.internal_link')
print(internal_link['href'])
print(internal_link.text)

print('--------------select() 함수----------------')
### select() 함수
# 모든 <h1> 태그 검색 후 리스트 형태로 리턴
h1_all = soup.select('h1')
print(h1_all)

# 모든 url 링크 검색
# html 문서의 모든 <a> 태그의 href 값 추출
url_links = soup.select('a')
for i in url_links:
    print(i['href'])

#<div id = 'class1'> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')

print(div_urls)
print(div_urls[0]['href'])

#<div id = 'class1'> 내부의 모든 <a> 태그는 자손 관계
# - 공백으로 구분할 수 있음
div_urls2 = soup.select('div#class1 a')
print(div_urls2)

# 여러 항목 검색하기
## <h1> 태그의 id가 'heading'과 'footer'를 모두 검색
## - 쉼표로 나열함

h1 = soup.select('#heading, #footer')
print(h1)

## <a> 태그의 class 이름이 'external_link와 internal_link 모두 검색
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)