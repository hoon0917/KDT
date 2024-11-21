# 211
# def 함수(문자열) :
#     print(문자열)

# 함수("안녕")
# 함수("Hi")

# # 예측
# # 안녕
# # Hi

# # 212
# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)
# # 예측
# # 7 15

# # 213
# #함수() 괄호 안에 매개변수 1개를 줘야 함

# # 214
# # 같은 타입 2개 입력 받아야 함

# # 215
# def print_with_smile(str) :
#     print(str,':D',sep='')

# print_with_smile('Hello')

# # 216
# print_with_smile('안녕하세요')

# # 217
# def print_upper_price(int):
#     print_with_smile(int*1.3)

# # 218
# def print_sum(num1,num2):
#     print(num1+num2)

# print_sum(5,1)

# # 219
# def print_ari(num1,num2) :
#     print(f'{num1} + {num2} = {num1+num2}')
#     print(f'{num1} - {num2} = {num1-num2}')
#     print(f'{num1} * {num2} = {num1*num2}')
#     print(f'{num1} / {num2} = {num1/num2}')

# print_ari(3,4)

# 220
def print_max(a,b,c) :
    max_num = 0
    if a > max_num : max_num = a
    if b > max_num : max_num = b
    if c > max_num : max_num = c
    print(max_num)
       

print_max(1,2,3)
print(max(1,2,3))
