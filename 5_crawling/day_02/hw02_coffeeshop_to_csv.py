from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv


# 필요한 부분만 출력
result =[]
for num in range(1,51):
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={num}&sido=&gugun=&store='

    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('td',{'class':'center_t'})
    # print(titles[0])
    
    region=titles[0].text
    title=titles[1].text
    address=titles[3].text
    phone_number=titles[5].text
    list=[title,region, address, phone_number]
    result.append(list)
# print(result)


# 출력1
print(f'매장이름:{title}, 지역:{region}, 주소:{address}, 전화번호:{phone_number}')


# DataFramr으로 저장
hollysdf=pd.DataFrame(result, columns=('매장이름','지역','주소','전화번호'))
# # print(hollysdf)

# # DataFrame -> csv로 저장
# # csv로 저장하면서 인덱스 설정
hollysdf.to_csv('hollys_branches.csv',encoding='utf-8', index=False)

# 출력 프로그램 만들기
# 특정 지역에 있는 커피 매장 출력하기
# 저장된 hollys_brances.csv 파일 읽음
# while True, 지역 검색, len()
# 검색한 지역명이 주소컬럼에 포함 되어 있는지 확인
# 인덱스 번호 수정

while True :
    name= input('검색할 매장의 지역을 입력하세요:')
    if name == 'quit':
        break
    else:
        data=pd.read_csv('hollys_branches.csv')
        data2=data[data['지역'].str.contains(name)]
        print(f'검색된 매장 수: {len(data2)}')
        data2.index=range(1,len(data2)+1)
        print(data2)

    
       
