import random as rad
# lotto=[0,0,0,0,0,0]
# idx=0
# while True :
#     num=rad.randint(1,45)
#     if num not in lotto :
#         lotto[idx] = num
#         idx=idx+1
#     if idx == 6 : break
# print(lotto)


## [실습] 로또 프로그램을 만들어주세요.
## - 1~45 범위에서 중복되지 않는 6개 추출
## - 반복 횟수 알수없음
##   무한반복문
## - 종료조건? 중복아닌 6개 숫자 => list, set, dict



# list 사용해서 lotto 만들기
lotto=[0,0,0,0,0,0]
idx=0
while True :
    num=rad.randint(1,45)
    if num not in lotto :
        lotto[idx]=num
        idx=idx+1
    if idx == 6 : break
print(lotto)


# lotto=set()
# while len(lotto) < 6 :
#     num=rad.randint(1,45)
#     lotto.add(num)
# print(lotto)


lotto=set()
while len(lotto) < 6 :
    num=rad.randint(1,45)
    lotto.add(num)
print(lotto)

lotto=[0,0,0,0,0,0]
idx=0
while True :
    num=rad.randint(1,45)
    if num not in lotto :
        lotto[idx]=num
        idx=idx+1
    if idx==6 : break
print(lotto)
