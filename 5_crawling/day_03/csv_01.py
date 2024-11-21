# 데이터를 csv로 저장
import csv

csvfile = open('test.csv', 'w', encoding='utf-8')           # 파일 객체 생성
try:
    writer = csv.writer(csvfile)
    writer.writerow(('number', 'number+2', '(number+2)^2')) # 헤더 정보

    for i in range(10):
        writer.writerow((i, i+2, pow(i+2)))                 # 내부 내용 입력
except Exception as e:
    print(e)
finally:
    csvfile.close()
