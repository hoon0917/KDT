## --------------------------------------------------------------------------
## ==> 1줄로 조건식을 축약 : 조건부 표현식
## --------------------------------------------------------------------------
## [실습] 임의의 숫자의 5의 배수 여부 결과를 출력 하세요.
##        단, 5를 제외한 나머지는 고려하지 X
num=int(input())
result=None
if num%5 :
    result='5의 배수 X'
else :
    result='5의 배수 O '
print(result)

print('5의 배수 X') if num%5 else print('5의 배수 O')

## [실습] 문자열을 입력 받아서 문자열의 원소 개수를 저장
## 단, 원소 개수가 0이면 None 저장
## - (1) 입력 받기 input()
## - (2) 원소/요소 갯수 파악하기 len()
## - (3) 원소/요소 갯수 저장 단, 0개면 None

data=len(input())
result=None
if data > 0 :
    result=(f'문자열의 원소 갯수는 {data}개')
else :
    result=None
print(result)
result=(f'문자열의 원소 갯수는 {data}개') if data > 0 else None
print(result)

## [실습] 연산자(4칙연산자 :  + - * /)와 숫자 2개 입력 받기
## - 입력된 연산자에 따라 계산 결과 저장하기
## - 예) 입력 : + 10 3 출력 : 13
data=input().split()
if data[0] == '+' :
    result=int(data[1])+int(data[2])
elif data[0] == '-' :
    result=int(data[1])-int(data[2])
elif data[0] == '*' :
    result=int(data[1])*int(data[2])
else :
    result=int(data[1])/int(data[2])
print(result)


