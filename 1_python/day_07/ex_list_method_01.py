# ----------------------------------------------------------------------------
# 리스트 전용의 함수 즉, 메서드(Method)
# - 리스트의 원소/요소를 제어하기 위한 함수들
# ----------------------------------------------------------------------------

import random as rad

# [1] 실습 데이터 => 임의의 정수 숫자 10개로 구성된 리스트
datas=[1,7,3,9,3,15,26,3,48,59]

# [메서드 - 요소 인덱스를 반환하는 메서드 index()]
# -> 13의 인덱스를 찾기
# -> 왼쪽 >>>> 오른쪽으로 찾기
idx=datas.index(48)
print(f' 48의 인덱스 : {idx}')

# -> 0의 인덱스를 찾기  ==> 존재하지 않는 데이터의 경우 ERROR
if 0 in datas :
    idx=datas.index(0)
    print(f' 13의 인덱스 : {0}')
else :
    print(f'0은 없는 데이터 입니다.')

# 리스트 내에 있는 숫자중 중복된 숫자 인덱스 찾기
# 3의 인덱스 찾기
if 3 in datas :
    idx=datas.index(3)
    print(f' 첫번째 3의 인덱스 : {idx}')

if 3 in datas :
    idx=datas.index(3,idx+1)
    print(f' 두번째 3의 인덱스 : {idx+1}')

if 3 in datas :
    idx=datas.index(3,idx+1)
    print(f' 세번째 3의 인덱스 : {idx+1}')


# [메서드 - 데이터가 몇개 존재하는지 갯수 파악하는 메서드 count(데이터)]
cnt=datas.count(3)
print(f'3의 개수 : {cnt}개')

idx=0
for n in range(cnt):
    idx=datas.index(3,idx if not n else idx+1 )
    print(f'{n+1}번째 3의 인덱스 : {idx}')