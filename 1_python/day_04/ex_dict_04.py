# --------------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장함수
# --------------------------------------------------------------------------------
person={'name':'홍길동', 'age':20, 'job':'학생'}
cat={'kind':'코숏', 'weight':'2.5kg', 'color':'검정', 'age':13}
jumsu={'국어':90, '수학':50, '영어':80}

## [연산자] -----------------------------------------------------------------------
# 산술 연산 X
# person+cat

# 멤버 연산자 : in, not in
#               key
print('name' in cat)
print('name' in person)

#               value : dict 타입에서는 key만 멤버 연산자로 확인 가능
print('검정' in cat)
print(20 in person)

# 만약 value 에서 멤버 연산자 쓰고 싶으면 values()로 추출 후 가능 함
a=person.values()
print(20 in a)

## [내장함수]
## - 원소/요소 개수 확인 len()
print(f'cat의 원소개수 : {len(cat)}개')
print(f'person의 원소개수 : {len(person)}개')

## - 원소/요소 정렬 : sorted()
#  - 키 기준으로 정렬
print(f'cat의 원소 정렬 : {sorted(cat)}')
print(f'person의 원소 정렬 : {sorted(person,reverse=True)}')

# - 값 기준으로 정렬 : 여러 타입의 데이터가 값으로 있기 때문에 불가능. 하고 싶으면 타입을 일치 시켜서 해야함
# print(f'cat의 원소 정렬 : {sorted(cat.values())}')

print(f' 점수의 값 기준 오름차순정렬 : {sorted(jumsu.values())}')
print(f' 점수의 키 기준 오름차순정렬 {sorted(jumsu)}')
print(f' 점수의 키/값 묶어서 오름차순정렬 : {sorted(jumsu.items())}')
print(f' 점수의 키/값 묶어서 값 기준 오름차순정렬 : {sorted(jumsu.items(), key=lambda x:x[1])}')