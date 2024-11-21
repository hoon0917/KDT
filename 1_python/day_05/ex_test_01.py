# --------------------------------------------------------------------------------------
# [실습 1] 글자 입력 받기
#          입력 받은 글자(a~z, A~Z)의 코드값을 출력합니다.
# --------------------------------------------------------------------------------------

data=input('글자입력(예 a~z,A~Z) :')
# 문자 => 코드값 변환 내장함수 : ord(1개)
# if len(data) > 0 :
#     if len(data) == 1 :
#         if 'a'<= data <='z' or 'A' <= data <= 'Z': 
#             print(f'{data}의 코드값 {ord(data)}')
#         else : 
#             print('알파벳을 입력하세요.')
#     else :
#         print('1개의 문자만 입력하세요')
# else :
#     print('입력된 데이터가 없습니다.')

if (len(data) == 1) and ('a'<= data <='z' or 'A' <= data <= 'Z') :
        print(f'{data}의 코드값 {ord(data)}')
else :
    print('1개의 알파벳 문자만 입력해야 합니다.\n입력된 데이터를 확인하세요.')

# 여러개의 문자열 ord 적용법
print(list(map(ord,data)))


# ------------------------------------------------------------------------------------
# [실습2] 점수를 입력 받은 후 학점을 출력합니다.
# - 학점 : A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F
# A+ = 96 ~ 100
# A = 95
# A- = 94 ~ 90

jumsu=int(input())
if 0 <= jumsu <=100 :
    if jumsu >=96 :
        print('학점 :A+')
    elif jumsu == 95 :
        print('학점 :A')
    elif 90 <= jumsu <= 94 :
        print('학점 :A-')
    elif 86 <= jumsu <= 89 :
        print('학점 :B+')
    elif jumsu == 85 :
        print('학점 :B')
    elif 80 <= jumsu <= 84 :
        print('학점 :B-')
    elif 76 <= jumsu <= 79 :
        print('학점 :C+')
    elif jumsu == 75 :
        print('학점 :C')
    elif 70 <= jumsu <= 74 :
        print('학점 :C-')
    elif 66 <= jumsu <= 69 :
        print('학점 :D+')
    elif jumsu == 65 :
        print('학점 :D')
    elif 60 <= jumsu <= 64 :
        print('학점 :D-')
    else :
        print('학점 : F')
else :
    print("잘못된 점수")

jumsu=75
grade=''
if 0 <= jumsu <=100 :
    if jumsu > 95 : grade='A+'
    elif jumsu == 95 : grade='A'
    elif jumsu >= 90 : grade='A-'
    elif jumsu > 85 : grade='B+'
    elif jumsu == 85 : grade='B'
    elif jumsu >= 80 : grade='B-'
    elif jumsu > 75 : grade='C+'
    elif jumsu == 75 : grade='C'
    elif jumsu >= 70 : grade='C-'
    elif jumsu > 65 : grade='D+'
    elif jumsu == 65 : grade='D'
    elif jumsu >= 60 : grade='D-'
    else : grade='F'
    print(grade)
else :
    print("잘못된 점수")