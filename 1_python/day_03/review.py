# 001
print("Hello World")

# 002
print("Mary\'s cosmetics")

# 003
print('신씨가 소리질렀다. "도둑이야".')

# 004
print(r"c:\Windows")

# 005
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n : 줄바꿈 문자 \t 탭 문자

# 006
print("오늘은", "월요일")
# 오늘은 월요일

#007
print("naver","kakao","sk","samsung", sep=";")

#008
print("naver","kakao","sk","samsung", sep="/")

#009
print("first", end="");print("second")

#010
print(5/3)

#011
삼성전자 = 50000
총_평가금액 = 삼성전자 * 10
print(총_평가금액) 

#012
시가총액=298000000000000
현재가=50000
PER=15.79
print(f'시가총액 : {시가총액}')
print(f'현재가 : {현재가}원')
print(f'PER : {15.79}')


#013
s="hello"
t="python"
print(s,t,sep="! ")

#014
print(2+(2*3))

#015
a="132"
print(type(a))

#016
sum_str="720"
sum_str=int(sum_str)
print(type(sum_str))  

#017
num=100
num=str(num)
print(type(num))

#018
a="15.79"
a=float(a)
print(type(a))

#019
year="2020"
year=int(year)
print(year-1,year-2,year-3)

#020
air=48584
total=air*36
print(total)

#021
letters='python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[4:])

#023
string="홀짝홀짝홀짝"
print(string[::2])

#024
string='PYTHON'
print(string[::-1])

#025
phone_number =  "010-1111-2222"
a=phone_number[:3]
b=phone_number[4:8]
c=phone_number[9:]
print(a,b,c, sep=" ")

#026
phone_number =  "010-1111-2222"
a=phone_number[:3]
b=phone_number[4:8]
c=phone_number[9:]
print(a,b,c, sep="")

#027
url = "http://sharebook.kr"
print(len(url))
print(url[-2:])

#028
# lang = 'python'
# lang[0]='P'
# 문자형은 변경 및 삭제 불가

#029
string='abcdfe2a354a32a'
string=string.replace('a','A')
print(string)
print(type(string))

#030
string='abcd'
string.replace('b','B')
print(string)

#031
a='3'
b='4'
# 예상 :34
print(a+b)

#032
print('H1'*3)
#예상 : H1H1H1

#033
print('-'*80)

#034
t1='python'
t2='java'
t3= t1 + " " + t2 + " "
print(t3*4)

#035
name1= "김민수"
age1 = 10
name2='이철희'
age2=13
print('이름 : %s 나이 : %d' %(name1,age1 ))
print('이름 : %s 나이 : %d' %(name2,age2 ))

#036


#037
print(f'이름 : {name1} 나이 : {age1}')
print(f'이름 : {name2} 나이 : {age2}')

#038
상장주식수= '5,969,782,550'
data=(상장주식수.replace(',',''))
상장주식수=int(data)
print(type(상장주식수))

#039
분기 = '2020/03(E) (IFRS연결)'
print(분기[:7])

#040
data="  삼성전자  "
a=data.strip()
print(a)

#041
ticker = 'btc_krw'
print(ticker.upper())

#042
ticker='BTC_KRW'
print(ticker.lower())

#043
a='hello'
print(a.capitalize())

#044
file_name="보고서.xlsx"
print(file_name.endswith(('xlsx')))

#045
file_name="보고서.xlsx"
print(file_name.endswith(('xlsx','xls')))

#046
file_name="2020_보고서.xlsx"
print(file_name.startswith('2020'))

#047
a= "hello world"
print(a.split())

#048
ticker='btc_krw'
print(ticker.split('_'))

#049
date='2020-05-01'
print(date.split('-'))

#050
data="039490    "
data=data.rstrip()
print(data)

#051
movie_rank=['닥터 스트레인지','스플릿','럭키']
print(movie_rank)

#052
movie_rank.append('배트맨')
print(movie_rank)

#053
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

#054
del movie_rank[3]
print(movie_rank)

#055
del movie_rank[2:]
print(movie_rank)

#056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

print(lang1+lang2)

#057
nums=[1,2,3,4,5,6,7]

print(max(nums))
print(min(nums))

#058
nums=[1,2,3,4,5]
print(sum(nums))

#059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060
nums=[1,2,3,4,5]
a=sum(nums)
b=len(nums)
print(a/b)

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

#063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#064
nums=[1,2,3,4,5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0],interest[1],interest[2],interest[3],interest[4])
print(" ".join(interest))

#067
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#068
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#069
string="삼성전자/LG전자/Naver"
print(string.split('/'))

#070
data=[2,4,3,1,5,10,9,]
data.sort()
print(data)

#071
my_varibale=()
print(my_varibale,type(my_varibale))

#072
movie_rank=('닥터 스트레인지','스플릿','럭키')
print(movie_rank)

#073
data=(1,)
print(data,type(data))

#074
# t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 에러 발생 이유 : 튜플은 원소 변경 및 삭제 불가

#075
t = 1,2,3,4
# t의 타입은 튜플 타입,원소 뒤에 ','가 있기 때문

#076
t = ('a','b','c')
t=list(t)
t=('A',"B","C")
print(t)
print(type(t))

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest))

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest= tuple(interest)
print(type(interest))

#079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# 결과 : 변경 사항 없음, 튜플은 변경 및 삭제 불가능

#080
a=tuple(range(2,100,2))
print(a,type(a))