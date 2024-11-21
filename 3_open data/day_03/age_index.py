# --------------------------------------------------------------------------
# age 파일의 인덱스 뽑아오기
# --------------------------------------------------------------------------

import csv

f=open('age.csv',encoding='euc-kr')
data=csv.reader(f)
header=next(data)
# print(header)
print('--------------------------------------')
print('age.csv index')
print('--------------------------------------')
for i in range(len(header)):
    print(f'[{i:3}]:{header[i]}')       # {1:3} : 3자리의 공간에 i값 출력

f.close