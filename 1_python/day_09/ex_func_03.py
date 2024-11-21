# -----------------------------------------------------------------
# 함수(function) 이해 및 활용
# 함수기반 계산기 프로그램
# - 사칙연산 기능별 함수 생성 => 덧 곱 뺄 나
# 2개 정수만 계산
# 함수이름 : chic
# 매개변수 : num1,num2
# 함수결과 : 정수 result
# -----------------------------------------------------------------
def add3(num1,num2):return num1+num2
def bbe(num1,num2):return num1-num2
def muilti(num1,num2):return num1*num2
def div(num1,num2):return num1/num2
  
# ------------------------------------------------------------------
# 함수기능 : 계산기 메뉴를 출력하는 함수
# 함수이름 :print_menu
# 매개변수 : 없음
# 함수결과 : 없음
# ------------------------------------------------------------------
def print_menu() :
    print(f'{"*":*^16}')
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"*  1  덧  셈   *":16}')
    print(f'{"*  2  뺄  셈   *":16}')
    print(f'{"*  3  곱  셈   *":16}')
    print(f'{"*  4  나눗셈   *":16}')
    print(f'{"*  5  종  료   *":16}')
    print(f'{"*":*^16}')

# print(f'{"*":*^16}')     # 가운데 정렬
# print(f'{"*":*>16}')     # 오른쪽 정렬
# print(f'{"*":*<16}')     # 왼쪽  정렬

## ------------------------------------------------------------------
# 함수기능 : 연산 수행 후 결과를 반환하는 함수
# 함수이름 :calc
# 매개변수 : 함수명, str 숫자 2개, str 연산자 1개
# 함수결과 : 없음
# ------------------------------------------------------------------
def calc(func,num1,num2,op) :
    num1=int(num1)
    num2=(int(num2))
    print(f'결과 : {num1} {op} {num2} = {func(num1,num2)}')




## 계산기 프로그램 --------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택시 프로그램 종료
# => 반복 ---> 무한반복 : while True
## ------------------------------------------------------------------
while True :
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    choice=input('메뉴 선택 :')
    if choice.isdecimal() :
        choice=int(choice)
    else :
        print('1~9 사이 숫자를 입력해주세요.')
        continue

    # 종료 조건(5번 메뉴) 처리
    if choice == 5 :
        print('프로그램을 종료합니다.')
        break
    elif choice == 1 : # 덧셈
        print('덧셈')
        num1,num2 = input('정수 2개(예: 1 2)').split()
        calc(add3,num1,num2,'+')
    elif choice == 2 : # 뺄셈
        print('뺄셈')
        num1,num2 = input('정수 2개(예: 1 2)').split()
        calc(bbe,num1,num2,'-')
    elif choice == 3 : # 곱셈
        print('곱셈')
        num1,num2 = input('정수 2개(예: 1 2)').split()
        calc(muilti,num1,num2,'*')
    elif choice == 4 : # 나눗셈
        print('나눗셈')
        num1,num2 = input('정수 2개(예: 1 2)').split()
        calc(div,num1,num2,'/')
    else :
        print('선택된 메뉴는 없습니다.')

