# ----------------------------------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# ----------------------------------------------------------------------------
# [메서드 - 요소 추가 메서드 append(데이터)]
datas=[1,3,5]

# # 새로운 데이터 추가 : 제일 마지막 원소 추가
# datas.append(100) 
# print(f'datas의 개수: {len(datas)}개,{datas} ')

# datas.append(100) 
# print(f'datas의 개수: {len(datas)}개,{datas} ')

# # [메서드 - 요소 추가 메서드 insert(인덱스, 데이터]
# datas.insert(0, 300)
# print(f'datas의 개수: {len(datas)}개,{datas} ')

# datas.insert(-1, 300)
# print(f'datas의 개수: {len(datas)}개,{datas} ')

#[실습 : 임의의 정수 숫자 10개 저장하는 리스트 생성]
# - 임의의 숫자 random 모듈
# - 빈 리스트 생성
import random as rad

nums=[]
# while True :
#     nums=rad.randint(1, 50)
#     a.append(nums)
#     if a.count() == 10 : break

for cnt in range(10):
    n=rad.randint(1,50)
    nums.append(n)
print(f'nums => {nums}')

for cnt in range(10):
    nums.append(rad.randint(1,50))
print(f'nums => {nums}')

# [메서드 - 요소 삭제 메서드 remove()]
# - 존재하지 않는 데이터 삭제 시 ERROR 발생함
datas.remove(1)
print(f'datas의 개수: {len(datas)}개,{datas} ')

# 리스트 안에 들어있는 특정 숫자가 몇개인지 파악하고 갯수만큼 전체 삭제
for cnt in range(datas.count(1)) : # count()의 () 안 숫자는 어떤 숫자 없앨지 적어놓은거
    datas.remove(1)