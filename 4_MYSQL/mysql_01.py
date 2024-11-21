import pymysql
import pandas as pd
import csv

# mysql의 sakila 데이터베이스에 연결
conn  = pymysql.connect(host='localhost', user = 'root', 
                        password='1234',db='sakila', charset='utf8')

# 가져올 테이블 선택
# 가져온 테이블을 한번에 dataframe 형태로 만들고 싶으면 conn.cusor(pymysql.cursors.DictCursor)
# dataframe 형태로 오면서 컬럼명도 같이 옴
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from language')

# 헤더 정보 가져오기
desc = cur.description
for i in range(len(desc)):
    print(desc[i][0], end=' ')
print()

# 모든 데이터 가져오기
rows= cur.fetchall()
for data in rows:
    print(data)
print()

# DataFrame으로 변환
language_df = pd.DataFrame(rows)
print(language_df)

# 데이터베이스 연결 종료
cur.close()
conn.close()