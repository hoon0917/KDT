import csv
f=open(r'C:\Users\KDP-17\EX_PANDAS6\data\daegu.csv','r',encoding='utf-8')
data=csv.reader(f)
count=0
for row in data :
    if count > 5 :
        break
    else :
        print(row)
        count= count+1

f.close()
fin=open(r'C:\Users\KDP-17\EX_PANDAS6\data\daegu.csv','r',encoding='utf-8-sig')
data=csv.reader(fin)

fout=open(r'C:\Users\KDP-17\EX_PANDAS6\data\daegu-utf8.csv','w',newline='')
wr=csv.writer(fout)


for row in data:
    for i in range(len(row)):
        row[i]=row[i].replace('\t',"")
    print(row)
    wr.writerow(row)
fin.close()
fout.close()
print('파일 저장 완료')

def get_minmax_temp(data):
    header = next(data)
    min_temp=100
    min_date=''

    max_temp=-999
    max_date=''

    for row in data :
        if row[3] == "":
            row[3] = 100
        row[3] = float(row[3])

        if row[4] == "":
            row[4]=-999
        row[4]=float(row[4])

        # 최저 기온 계산
        if row[3] <min_temp :
            min_temp=row[3]
            min_date=row[0]

        # 최고 기온 계산
        if row[4]>max_temp :
            max_temp=row[4]
            max_date=row[0]
    print('-'*50)
    print(f'대구 최저 기온 날짜 : {min_date}, 온도: {min_temp}')
    print(f'대구 최저 기온 날짜 : {max_date}, 온도: {max_temp}')


def main():
    f=open('daegu-utf8.csv',encoding='utf-8-sig')
    data=csv.reader(f)
    get_minmax_temp(data)
    f.close()


main()



