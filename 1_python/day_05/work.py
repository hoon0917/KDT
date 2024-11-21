# p.193 16.5
x= [49, -17, 25, 102, 8, 62, 21]

for i in x :
    print(i*10, end = " ")

# p.193 16.6
dan=int(input())
if dan in range(10) :
    for i in range(1,10) :
        print(f'{dan} * {i} = {dan*i}')
else :
    print("잘못된 숫자입니다. 다시 입력하세요.")