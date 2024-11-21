# ------------------------------------------------
# 내장함수 print() 사용법
# - 모니터 즉, 콘솔/터미널에 출력하는 함수
# - 문법 : print(argument, argument, argument ...)
#           print()
# ------------------------------------------------
# 변수 설정 : 나이, 이름, 성별 저장하기

age=30
name='감자'
gender='여자'

# 모니터에 출력하기

print(age)
print(name)
print(gender)
print(age, name, gender)

# 2개의 정수 덧셈 결과 출력하기 -------------------------------------
num1=1
num2=9
print(num1 + num2)
# 출력 결과에 대한 설명을 앞에 적고 결과를 나오게
# 1+9 => 10
print(f'num1 + num2 => {num1+num2}')

# ==> 서식지정자(Format String) 방식
# ==> 화면 출력 글자를 만들고 그 글자안에 특정 결과를 출력하는 형식
# ==> 글자 내부에 정수 결과 넣기 : ' %d ' %변수명 또는 %수식
# ==> 글자 내부에 실수 결과 넣기 : ' %f ' %변수명 또는 %수식
# ==> 글자 내부에 글자 결과 넣기 : ' %s ' %변수명 또는 %수식
# 1+9 화면에 수식 출력하기
print('%d + %d = %d' %(num1, num2, num1+num2))

# 9 / 1 = 9 화면에 출력하기
print('%d / %d = %f' %(num2, num1, num2/num1) )
print('%s / %s = %s' %(num2, num1, num2/num1) )

# ==> F-Strig 방식
# ==> 형식 : f' {변수명 또는 수식  또는 데이터}     '
print(f'{num1} + {num2} => {num1+num2}')
print(f'{num2} / {num1} => {num2/num1}')