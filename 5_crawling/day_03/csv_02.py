# 테이블 데이터를 csv로 저장
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors') # 주소 가져오기
bs = BeautifulSoup(html, 'html.parser')

table = bs.find_all('table', {'class':'wikitable'})[0] # 두개의 테이블중 첫 번째 테이블 사용
rows = table.find_all('tr')

csvfile = open('editors.csv','wt',encoding='utf-8')
writer=csv.writer(csvfile)

try:
    for row in rows:
        csvrow=[]
        for cell in row.find_all['th','td']:
            print(cell.text.strip())
            csvrow.append(cell.text.strip())
        writer.writerow(csvrow)
finally:
    csvfile.close()
