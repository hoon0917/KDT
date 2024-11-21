import csv
f=open('age.csv', encoding='euc-kr')
data=csv.reader(f)
header=next(data)

# row[0] : 행정구역
for row in data :               # 가져온 data의 각 행별로 산격3동이 있는지 확인
    if '산격3동' in row[0] :    # 즉, 산격3동이 들어가 있는 행 추출
        print(row)
f.close()