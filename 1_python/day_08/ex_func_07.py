# -------------------------------------------------------------------
# 사용자 정의 함수
# -------------------------------------------------------------------
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수2개 num1, num2
# - 함수결과 : 연산 결과 반환
def deot(num1,num2):
    return num1+num2

def bbel(num1,num2):
    return num1-num2

def gob(num1,num2):
    return num1*num2

def na(num1,num2):
    return num1/num2 if num2  else '0으로 나눌 수 없음'

# -------------------------------------------------------------------
# 함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 data, cnt, sep=' '
# 함수 결과 : 유효 여부 True/False
# --------------------------------------------------------------------
def check_data(data,count,sep=' '):
    # 데이터 여부
    if len(data) :
        # 데이터 분리 후 갯수체크
        data2=data.split(sep)
        return True if count == len(data2) else False 
    else :
        return False
    
print(check_data('+ 10 3',3))
print(check_data('',3))
print(check_data('1   ',3))

# 함수 사용하기 즉, 호출
# [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아서 연산 결과를 출력해주세요.
# - input('연산자, 숫자1, 숫자2 :').split()

data1, data2, data3=input('연산자, 숫자1, 숫자2를 입력해주세요').split()
data2 = int(data2)
data3 = int(data3)
if data1 == '+' :
    print(deot(data2,data3))
elif data1 == '-' :
    print(bbel(data2,data3))
elif data1 == '*' :
    print(gob(data2,data3))
else :
    print(na(data2,data3))

#방법2
# if data1 not in ['+','-','*','/']:
#     print(f'{data1} 잘못된 연산자 입니다.')

    






