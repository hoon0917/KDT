# 121
# msg=input()
# if 'a' <= msg <= 'z' :
#     print(msg.upper())
# else :
#     print(msg.lower()) 

# 122
# score=int(input('점수 입력 :'))
# if score > 80 :
#     print('grade is A')
# elif score > 60 :
#     print('grade is B')
# elif score > 40 :
#     print('grade is C')
# elif score > 20 :
#     print('grade is D')
# else :
#     print('grade is E')

# 123
# money=input().split()
# money1=float(money[0])
# money2=money[1]
# if money2 == '달러' :
#     print(f'{money1*1167}원')
# elif money2 == '엔' :
#     print(f'{money1*1.096}원')
# elif money2 == '유로' :
#     print(f'{money1*1268}원')
# else :
#     print(f'{money1*171}원')

# 124
# number1, number2, number3= map(int,input().split())
# print(max(number1,number2,number3))

# 125
# number=input('휴대폰 번호 입력 :')
# if number[:3] == '011' :
#     print('당신은 SKT 사용자입니다.')
# elif number[:3] == '016' :
#     print('당신은 KT 사용자입니다.')
# elif number[:3] == '019' :
#     print('당신은 LGU 사용자입니다.')
# else : 
#     print('알수없음')

# 126
# data=input('우편번호 입력 :')
# gang=['0','1','2']
# do=['3','4','5']
# if data[2] in gang :
#     print('강북구')
# elif data[2] in do :
#     print('도봉구')
# else :
#     print('노원구')

# # 127
# jumin=input('주민등록번호 입력 : ')
# if jumin[7] == '1' or jumin[7] == '3' :
#     print('남자')
# else :
#     print('여자')

# 128
jumin=input('주민등록번호 입력 :')
seoul=['00','01','02','03','04','05','06','07','08']
if jumin[8:10] in seoul :
    print('서울 입니다.')
else :
    print('서울이 아닙니다.')

# 129
# jumin=input('주민등록번호 입력:').split('-')
# jumin1=jumin[0]
# jumin2=jumin[1][:6]
# print(int(jumin1[0]))
# print(int(jumin2[0]))
# data= int(jumin1[0])*2+int(jumin1[1])*3+int(jumin1[2])*4+int(jumin1[3])*5+int(jumin1[4])*6+int(jumin1[5])*7\
# + int(jumin2[0])*8+int(jumin2[1])*9+int(jumin2[2])*2+int(jumin2[3])*3+int(jumin2[4])*4+int(jumin2[5])*5
# num=str(11-(data%11))

# if jumin[1][-1] == num[-1] :
#     print('유효한 주민번호')
# else :
#     print('유효하지 않은 주민번호')

# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# move= float(max_price) - float(min_price) :
# if float(opening_price)+ move > max_price:
#     print('상승장')
# else : 
#     print('하락장')