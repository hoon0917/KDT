# -------------------------------------------------------------------------
# 제어문 - while 반복문
# ------------------------------------------------------------------------- 
## [실습] 3단 출력하기 단, while문으로
# num = 10
# while num > 10 :
#     print(num)
#     num=num-1

num=1 
while num < 10 :
    print(f'3*{num} = {3*num}')
    num=num+1

## [실습] 1 ~ 30 범위의 수 중에서 홀수만 출력, while문으로
## [1] 1 ~ 30 숫자 while문으로 출력
num=1
while num < 31 :
    if num%2 :
        print(num,end=', ')
    num=num+1 

print("")

num=1
while num < 31 :
    print(num,end=', ')
    num=num+2 


