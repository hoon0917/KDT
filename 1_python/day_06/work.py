# p. 202 17.5
i = 2
j = 5
while i <= 32 or j > 1 :
    print(i, j)
    i = i*2
    j = j-1 

# p. 203 17.6
data=int(input())

while data >= 1350 :
    print(data-1350)
    data=data-1350

# p. 211 18.5`
i=0
while True :
    if i % 10 != 3 :
        i=i+1
        continue
    if i > 73 : break
    print(i,end=' ')
    i=i+1

# p. 212 18.6
start, stop=map(int,input().split())

i = start
while True :
    if i%10 == 3 :
        i=i+1
        continue
    if i > stop : break
    print(i,end=' ')
    i=i+1
  
# p. 218 19.5
for i in range(5):
    for j in range(5):
        if j >= 5 :
            print('★', end="")
        else:
            print(" ",end="")
    print()

# p. 225 20.7
for i in range(1,101):
    if i%22==0 :
        print('PizzBuzz')
    elif i%2 == 0:
        print('Pizz')
    elif i%11 == 0:
        print('Buzz')
    else :
        print(i)

# p. 226 20.8
start,end=map(int,input().split())
if 0 <= start <= 1000 and 10 <= end <= 1000  : 
    for n in range(start,end+1):
        if n%35 == 0 :
            print("PizzBuzz")
        elif n%5 == 0 :
            print('Pizz')
        elif n%7 == 0 :
            print('Buzz')
        else:
            print(n)    
else :
    print('잘못된 숫자입니다. 숫자를 다시 입력해주세요.')