# 기능1 : 기업 이름 및 url 저장 리스트 만들기

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import collections 
collections.Callable = collections.abc.Callable


# 기본 크롤링
url= 'https://finance.naver.com/sise/sise_market_sum.naver'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
company = soup.find('tbody') 


# print(company)

# URL 및 기업 이름 리스트 저장
company_name=[]
company_url=[]
for name in company.find_all('a', {'class': 'tltle'}):
    a_tag=name.text
    company_name.append(a_tag)
    url=name['href']
    true_url='https://finance.naver.com'+url
    company_url.append(true_url)

company_url=company_url[:10]
company_name=company_name[:10]

# print(company_url)
# 세부 주식 정보 출력
# 삼성전자 선택


def pynance(num):
    
    
    url2=company_url[0]
    html2=urlopen(url2)
    soup2 = BeautifulSoup(html2,'html.parser')

    company_list=[]
    company=soup2.find_all('em',{'class':'no_up'})
    for blind in company:
        span_tag=blind.find_all('span', {'class':'blind'})
        for a in span_tag:
            list= a.text
            company_list.append(list)

    print(company_url[num-1])
    print(f'종목명: {company_name[num-1]}')
    print(f'종목코드: {company_url[num-1][-6:]}')
    print(f'현재가:{company_list[num-1]}')
    print(f'고가:{company_list[3]}')
    print(f'시가:{company_list[4]}')
       

def menu():
    print('-'*30)
    print('[네이버 코스피 상위 10대 기업 목록]')
    print('-'*30)
    print('[1] 삼성전자')
    print('[2] SK하이닉스')
    print('[3] LG에너지솔루션')
    print('[4] 삼성바이오로직스')
    print('[5] 현대차')
    print('[6] 삼성전자우')
    print('[7] 셀트리온')
    print('[8] 기아')
    print('[9] KB금융')
    print('[10] 신한지주')

while True :
    menu()
    choice_input = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료)'))
    if choice_input == 1 :
        pynance(1)
    if choice_input == 2 :
        pynance(2)
    if choice_input == 3 :
        pynance(3)
    if choice_input == 4 :
        pynance(4)
    if choice_input == 5 :
        pynance(5)
    if choice_input == 6 :
        pynance(6)
    if choice_input == 7 :
        pynance(7)
    if choice_input == 8 :
        pynance(8)
    if choice_input == 9 :
        pynance(9)
    if choice_input == 10  :
        pynance(10)


    if choice_input == -1 :
        break
print('프로그램 종료')


    
