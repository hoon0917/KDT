import csv
max= [0,0,0,0]
max_station=['','','','']
label=['유임승차','유임하차','무임승차','무임하차']

# with 구문 : 자동으로 파일을 close()시킴
with open('subwayfee.csv',encoding='utf-8-sig') as f :
    data = csv.reader(f)
    next(data)

    for row in data :
        for i in range(4,8):
            row[i] = int(row[i])                                # 각 행의 숫자를 정수로 전환해서 계산가능하게 해줌
            if row[i] > max[i-4] :                              # 각 행의 값이 max리스트보다 크다면
                max[i-4] = row[i]                               # max 리스트의 각 열에 row[i]의 값을 업데이트 해라
                max_station[i-4] = row[3]+' '+row[1]
                             

for i in range(4):
    print(f'{label[i]}: {max_station[i]} {max[i]:,}명')