## 반복문과 조건문 혼합
## [실습]  -----------------------------------------------------------------
## 메시지를 입력 받습니다.
## 알파벳 대문자인 경우 소문자로, 소문자인 경우 대문자로 upper(),lower()
## 나머지는 그대로 출력하기
## --------------------------------------------------------------------------------------------
msg="Merry Christmas"

for m in msg :
    if 'a'<= m <= 'z' :
        print(m.upper(),end='')
    elif 'A' <= m <= 'Z' :
        print(m.lower(),end='')
    else :
        print(m,end='')

print("    ")
for m in msg :
    if 'a'<= m <= 'z' :
        print(chr(ord(m)-32),end='')
    elif 'A' <= m <= 'Z' :
        print(chr(ord(m)+32),end='')
    else :
        print(m,end='')

# print(chr(ord(m)-32)) # 소문자 -> 대문자. 원소의 코드(ord)으로 소문자-> 대문자 변환 후 chr을 이용해서 다시 문자로 변환
# print(chr(ord(m)+32)) # 대문자 -> 소문자

print("  ")

for m in msg :
    if m.isupper() :
        print(m.lower(),end='')
    elif m.islower():
        print(m.upper(),end='')
    else :
        print(m,end="")