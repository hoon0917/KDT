import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f=open('subwayfee.csv', encoding='utf-8-sig')
data=csv.reader(f)
header=next(data)

min_rate=100
min_row=[]
min_total_count=0

for row in data :
    for i in[4,6] :                                 # 각 행의 필요한 컬럼만 추출
        row[i] = int(row[i])
    total_count = row[4] + row[6]                   # 4,6 열의 사람 수 합 즉, 전체 인원

    # 무임승차 인원이 없고, 총 승차 인원이 1만명 이상
    if (row[6] !=0) and (total_count>=10000) :      
        rate = row[4] / total_count                 # 유임승차 비율 : 유임 승차/전체 인원
        if rate <= 0.5 :                            # 유임승차 비율이 50% 이하
            print(row,round(rate,2))                # 유임승차 비율이 50% 이하인 역들의 유임승차 비율을 소수점 2자리까지 출력
            if rate < min_rate :                    # 유임승차 비율이 임의로 설정해놓은 min_rate 즉, 100보다 낮다면
                min_rate = rate                     # 아래 3개의 값을 업데이트 해라(서울의 모든 역들 중 최소값 찾기 작업)
                min_row = row
                min_total_count = total_count
f.close()

print()
print(f'유임 승차 비율이 가장 낮은 역 : {min_row[3]}역')
print(f'전체 인원 : {min_total_count:,}명'
      f' 유임승차인원 : {min_row[4]:,}명'
      f' 유임승차비율 : {round(min_rate*100,1)}%')

plt.title(min_row[3]+'역 유,무임 승차 비율')
label = ['유임승차','무임승차']
values = [min_row[4],min_row[6]]
plt.pie(values,labels=label,autopct='%.1f%%')
plt.legend(loc=2)
plt.show()