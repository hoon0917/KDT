# p49 3.7
print('Hello, world!')
print('Python Programming')




# p.49 3.8
print('Hello, world!')
print('Hello, world!')



# p.62 5.5
print(int(0.2467 * 12 + 4.159))




# p.62 5.6
print(102 * 0.6 + 225)




# p.75 6.7 
a=input('정수를 입력하세요 :')
b=input('정수를 입력하세요 :')
c=input('정수를 입력하세요 :')
a=int(a)
b=int(b)
c=int(c)
print(a+b+c)



# p.75 6.7
a=50
b=100
c=None

print(a)
print(b)
print(c)




# p.75 6.8

a=input('국어 점수를 입력하세요')
b=input('수학 점수를 입력하세요')
c=input('영어 점수를 입력하세요')
d=input('과학 점수를 입력하세요')
a=int(a)
b=int(b)
c=int(c)
d=int(d)
평균=((a+b+c+d)/4)
print(평균)



# p.80 7.4
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')



# p. 81 7.5
year = input('년도:')
month = input('월:')
day = input('일자:')
hour = input('시:')
minute = input('분:')
second = input('초:')
int(year)
int(month)
int(day)
int(hour)
int(minute)
int(second)

print(year, month, day, sep='-', end='')
print('T', end='')
print(hour, minute, second, sep=':')


# p.94 8.4
korean=92
english=47
math=86
science=81
print(korean>50 and english>50 and math>50 and science>50)



# p.95 8.5
국어=(input())
영어=(input())
수학=(input())
과학=(input())

국어=int(국어)
영어=int(영어)
수학=int(수학)
과학=int(과학)

print(국어>=90 and 영어 > 80 and 수학 > 85 and 과학 >=80)



# p. 100 9.3
s = """ Python is a programming language that lets you work quickly
and
intergrate systems more effectively."""
print(s)

# p.101 9.4
s='''\'python\' is a "programming language"
that lets you work quickly
and
intergrate systems more effectivly'''
print(s)