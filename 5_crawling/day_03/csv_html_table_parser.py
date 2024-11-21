import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parse
import pandas as pd
import collections

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors') # 주소 가져오기
bs = BeautifulSoup(html, 'html.parser')

table = bs.find('table', {'class':'wikitable'})
table_data = parse.make2d(table)

# 테이블의 2행 출력
print('[0]:', table_data[0])
print('[1]:', table_data[1])

# pandas DataFrame 으로 저장
df = pd.DataFrame(table_data[2:], columns=table_data[1])
print(df.head())

# csv파일로 저장
df.to_csv('editors1.csv', encoding='utf-8')
# csvfile = open('editors1.csv','w',encoding='utf-8')
# Writer = csv.writer(csvfile)