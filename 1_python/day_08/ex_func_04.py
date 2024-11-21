# -------------------------------------------------------------------
# 사용자 정의 함수
# -------------------------------------------------------------------
# 목적 : 매개변수의 개수를 유동적으로 0개 ~ N개까지 가능하도록
# 형태 : def 함수명(*변수명) <= 0개 ~ N개 데이터
# -------------------------------------------------------------------

# ---------------------------------------------------------------------
# 함수 기능 : 정수를 덧셈 한 후 결과를 반환/리턴 하는 함수
# 함수 이름 : add
# 매개 변수 : 0개 ~ N개
# 함수 결과 : 덧셈 계산값 result
# ---------------------------------------------------------------------
def add(*nums):
    total=0
    for i in nums:
       total=total+i
    return total
        


## 함수 호출 -----------------------------------------------------------
print(add())
print(add(1,1,1))
print(add(5,6))
print(add(8,6,4,9,1,56,8,1,5))