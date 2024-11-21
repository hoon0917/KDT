# p.149 12.4
camille = {'health':575.6,'movement_speed':340}
print(camille['health'])
print(camille['movement_speed'])

# p.150 12.5
data1=input().split()
data2=input().split()
data3=dict(zip(data1,data2))
print(data3)

# p. 164 13.6
x=5
if x != 10 :
    print('ok')

# p. 165 13.7
data1=int(input())
data2=str(input())
if data2 in 'Cash3000' :
    print(f'{data1-3000}')
else :
    print(f'{data1-5000}')

# p. 174 14.6
Written_test = 75
coding_test=True
if Written_test >= 80 and coding_test == True :
    print('합격')
else :
    print('불합격')

# p.174 14.7
jumsu=input().split()
jumsu=list(map(int,jumsu))
if jumsu[0]>=0 and jumsu[0]<=100 and jumsu[1]>=0 and jumsu[1]<=100 and jumsu[2]>=0 and jumsu[2]<=100 and jumsu[3]>=0 and jumsu[3]<=100 :
    jumsu=(sum(jumsu))/4
    if jumsu >= 80 :
        print('합격')
    else :
        print('불합격')
else :
    print('잘못된 점수')

# p.180 15.3
x=int(input())
if 11<= x <= 20 :
    print('11~20')
elif 21 <= x <= 30 :
    print('21~30')
else :
    print('아무것도 해당하지 않음')

#p. 180 15.4
age=int(input())
if 7 <= age <= 12 :
    print(9000-650)
elif 13<= age <=18 :
    print(9000-1050)
else :
    print(9000-1250)