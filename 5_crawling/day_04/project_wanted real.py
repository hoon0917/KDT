
# 원티드 채용 공고 페이지 크롤링

from bs4 import BeautifulSoup
import collections 
collections.Callable = collections.abc.Callable
from collections import Counter
import requests
from konlpy.tag import Okt
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

html = open('html2.txt',encoding='utf-8').read()
soup = BeautifulSoup(html,'html.parser')
position_id=[]

# 주요업무 리스트
work_list=[]

# 각 카드별 주소 id 찾기
company_id = soup.find_all('li',{'class':'Card_Card__WdaEk'})
for i in company_id:
    a_tags=i.find_all('a')
    for a_tag in a_tags:
        data_positon_id = a_tag.get('data-position-id')
        position_id.append(data_positon_id)

# 주요업무 리스트 출력
for i in range(len(position_id)):
    url = 'https://www.wanted.co.kr/wd/' + position_id[i]
    
    url_list = requests.get(url)
    soup = BeautifulSoup(url_list.text, 'html.parser')

    work_text = soup.get_text()
    start = work_text.find('주요업무')
    end = work_text.find('자격요건')
    work_list.append(work_text[start:end].replace('•',''))

# 텍스트 형태소 분석
okt= Okt()
sentences_tag=[]
for sentence in work_list:
    morph = okt.pos(sentence)
    sentences_tag.append(morph)
    # print(morph)


# 명사, 형용사, 영단어 리스트에 추가
noun_adj_list=[]
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        if tag in ['Noun']:
            noun_adj_list.append(word)

# 형태소별 count
counts = Counter(noun_adj_list)
tags = counts.most_common(50)
tag_dict = dict(tags)

# 제외할 단어 설정
tag_dict = dict(tags)

stopwords=['개발', '및', '위', '등', '수', '업무', '데이터', '서류', '인터뷰', '신규', '개발자', '고객', '통해', '보수', '코드', '기업',
           '를', '기술', '시스템', '분석', '활용', '기반', '진행', '관련' ]
for stopword in stopwords:
    if stopword in tag_dict:
        tag_dict.pop(stopword)


# 언어 설정
path = r'c:\Winodos\Fonts\malgun.ttf'

# wordcloud 생성
img_mask=np.array(Image.open('cloud.png'))
wordcloud = WordCloud(font_path=path, width=800, height=600,
                      background_color='white', max_font_size=200,
                      repeat=True,
                      colormap='inferno', mask=img_mask)
cloud = wordcloud.generate_from_frequencies(tag_dict)
plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

# csv로 크롤링 결과물 저장
workdf= pd.DataFrame(noun_adj_list)
workdf.to_csv('work.csv',encoding='utf-8')

'''
1. 텍스트 형태소 분석
2. 분석 된 단어 work_list에 넣어줌
3. work_list 가지고 클라우드 생성
4. work_list csv로 저장 후 데이터 프레임 생성
'''