# p. 303 24.4
# path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
# filename=path.split('\\')
# print(len(filename))
# print(filename[-1])

# p. 305 24.5
# 문자열을 입력 받아야 함 input()
# the의 개수 출력 count(the)
# 단, 모든 문자가 소문자인 the 
# them, their, there등은 빼야함
# msg=input().split()
# data2=[]
# for data in msg :
#     if data == 'the' :
#         data2.append(data)  

# print(len(data2))


# p. 305 24.6
# 가격의 길이는 9
# 오른쪽 정렬
# 천단위로 , 넣기
# msg=list(map(int,input().split(';')))
# msg=sorted(msg,reverse=True)
# for i in msg :
#     print('{0:>9,}'.format(i))

# p. 384 29.7
def get_quotient_remainder(num1,num2) :
    return (f'몫: {num1//num2}, 나머지: {num1%num2}')

get_quotient_remainder(10,3)

# p. 384 29.8
# 사칙 연산 함수 만들기
x,y=map(int,input().split())
def sachic(num1,num2) :
    return (f'덧셈 : {num1+num2}, 뺄셈 : {num1-num2}, 곱셈 : {num1*num2}, 나눗셈 : {num1/num2}')

print(sachic(10,20))


