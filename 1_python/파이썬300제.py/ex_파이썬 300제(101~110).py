# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입?
# bool

# 102~ 110번은 아래의 출력 결과 예상 문제
# 102
print(3 == 5)
# False

# 103
print(3<5)
# True

# 104
x = 4
print(1 < x < 5)
# True

# 105
print((3 == 3) and ( 4 != 3 ))
# True

# 106
print(3 => 4)
# 잘못된 연산자

# 107
if 4 <3 :
print("Hello World")
# 출력 되는거 없음

# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# Hi, there 출력

# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1 2 4 출력

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

# 3, 5 출력