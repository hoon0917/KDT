# -------------------------------------------------------------------------------
# 함수와 변수 - 지역/전역 변수
# -------------------------------------------------------------------------------
## 전역변수(Global varibale)
## - 파일(py) 내에 존재하며 모든 곳에서 사용 가능
## - 프로그램 실행 시 메모리 존재
## - 프로그램 종료 시 메모리에서 삭제
## ------------------------------------------------------------------------------
total=100

# -------------------------------------------------------------------------------
##  지역변수(Local varibale)
## - 함수 내에 존재하며 함수에서만 사용 가능
## - 함수 실행 시 메모리 존재
## - 함수 종료 시 메모리에서 삭제
## ------------------------------------------------------------------------------
# 함수기능 : 정수를 덧셈한 후 결과를 반환하는 함수
# 함수이름 : addInt
# 매개변수 : 0개 ~ N개 즉, 가변인자 *nums
# 함수결과 : 정수 result
# ------------------------------------------------------------------------------
def addInt(*nums) :
   total=0
   for n in nums :
        total=total+n
        return total
   
def muiltiInt(*nums) :
   total1=1
   for n in nums :
        total1 *= n
        return total1

## 함수호출 ---------------------------------------------------------------------
result1 = addInt(1)
print(f'result1 : {result1}')

result2 = muiltiInt(5)
print(f'result2 : {result2}')


def addInt(*nums) :
   total=0
   for n in nums :
        total=total+n
        return total
   
def muiltiInt2(*nums) :
   # 전역변수의 값을 변경할 경우 그냥 사용 X
   global total
   for n in nums :
        total *= n
        return total
   
## 함수호출 ---------------------------------------------------------------------
result1 = addInt(1)
print(f'result1 : {result1}')

print(f'전 : total => {total}')
result2 = muiltiInt2(5)
print(f'result2 : {result2}')
print(f'후 : total => {total}')
