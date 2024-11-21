# -----------------------------------------------------------------
# 함수(function) 이해 및 활용
# 함수기반 계산기 프로그램
# - 사칙연산 기능별 함수 생성 => 덧 곱 뺄 나
# 2개 정수만 계산
# 함수이름 : chic
# 매개변수 : num1,num2
# 함수결과 : 정수 result
# -----------------------------------------------------------------
def chic(num1,str,num2):
    if str == '+' :   return num1+num2
    elif str == '-' : return num1-num2
    elif str == '*' : return num1*num2
    elif str == '/' : return num1/num2

## 계산기 프로그램 -----------------------------------------------
# - 사용자가 종료를 원할때 종료 => 'x' 'X' 입력 시 break
# - 연산방식과 숫자 데이터 입력 받기
while True :
    # 1. 입력 받기
    req=input('연산(+,-,*,/)방식과 정수 2개 입력(예시 : + 10 2)')
    # 2. 종료 조건 검사
    if req == 'x' or req =='X' : 
        print('계산기를 종료합니다.')
        break
    # 입력에 대한 연산 방식과 데이터 추출 '+ 10 2'
    op, num1, num2 = req.split()
    # str 정수 ==> int로 변환
    num1=int(num1)
    num2=int(num2)
    # 연산 방식에 따라서 계산 진행
    if op =='+' :
        print(f'{num1}+{num2}={num1+num2}')
    elif op=='-':
        print(f'{num1}-{num2}={num1-num2}')
    elif op == '*' :
        print(f'{num1}*{num2}={num1*num2}')
    elif op=='/' :
        print(f'{num1}/{num2}={num1/num2}')
    else :
        print('지원되지 않는 연산자 입니다.')