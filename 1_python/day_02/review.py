# file 매개변수 사용하기

# season=input('좋아하는 계절 입력')
# counrty=input('좋아하는 나라 입력')
# trip=input('좋아하는 여행 입력')

# Filename = 'test02.txt'

# f=open(Filename, 'w', encoding='utf-8')
# print(f'좋아하는 계절은 {season}', file=f )
# print(f'좋아하는 나라는 {counrty}', file=f )
# print(f'좋아하는 여행은 {trip}', file=f )
# f.close()

# # 입력 값에 변수 2개 이상 저장하기
# a,b = input('숫자 두개 입력하세요 :').split()
# split : 나누다
# 변수 1개만 설정해서 공백 있는 문자열 넣으면 공백을 기준으로 list 타입 변수 저장
# 변수 2개 이상 설정하면 각각의 변수에 string 타입으로 변수 저장


# a,b=map(int, input('숫자 두개를 입력해주세요 :').split(','))

# print(a+b)

# a,b,c = map(int, input('숫자를 입력하세요 :').split())

# print(a+b+c)

# a,b,c,d =  map(int, input().split())

# 평균 = int((a+b+c+d)/4)

# print(평균)

# year, month, day, hour, minute, second = input().split()
# print(year, month, day, sep='-', end='')
# print('T',end='')
# print(hour, minute, second, sep=':')

# 국어, 영어, 수학, 과학 = map(int,input().split())
# print(국어>=90 and 영어 > 80 and 수학 >85 and 과학 >=80)

# a,b,c,d =  map(int, input().split())

# 평균 = ((a+b+c+d)/4)

# print(평균)

# input 함수에 일일이 int 넣기 힘드니까 map 사용
# 문법 : 변수 : map(int, input().split())

# a,b,c = map(int,input().split())

# print(a+b+c)

