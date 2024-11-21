# 201
# def print_coin() :
#     print('bitcoin')

# 202
# print_coin()

# 203
# for i in range(101) :
#     print_coin()

# 204
# def print_coins() :
#     for i in range(101) :
#         print('bitcoin')

# print_coins()

# 205
# 함수의 순서가 잘못 됐음 정의되고 나서 호출해야 됨

# 206
def message() :
    print("A")
    print("B")

# message()
# print("C")
# message()
# # 예측
# print('A\nB\nC\nA\nB')

# 207
# print("A")

def message() :
    print("B")

# print("C")
# message()

# # 예측
# print('A\nC\nB')

# 208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

# 예측 
# A C B E D

# 209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

# 예측
# B A

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

# 예측
# B C B C B C A 
