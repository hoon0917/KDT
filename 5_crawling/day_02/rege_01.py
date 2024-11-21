# 정규 표현식 사용
# 정규식 객체를 생성 : compile(pattern)

import re
# compile() 사용 안함
m = re.match('[a-z]+','Python') # 패턴이 a-z까지인데 검색 문자열이 대문자로 시작하니까 리턴값이 없음(matech 특성)
m2 = re.match('[a-z]+', 'pythoN')
print(m)
print(m2)
print(re.search('apple','I like apple!'))

# comepile() 사용 : 객체 생성
# 생성된 객체는 조건을 매번 쓰기 힘드니까 조건을 하나의 객체로 만든 것,  문자열을 검사할 때 사용하는 것
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))

print('*'*50)
# match() 문자열의 처음부터 검사

print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', 'regexpython'))

print(re.match('[a-z]+', 'regexpythoN'))
# $는 문자열의 마지막부터 검사
print(re.match('[a-z]+$', 'regexpythoN'))

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))

print('*'*50)
print('findall(), search() 사용')

# finall() 함수
# 일치하는 모든 문자열을 리스트로 리턴
p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

# search() 함수
# 일치하는 첫번째 문자만 리턴
result = p.search('I like apple 123')
print(result)

result = p.findall('I like apple 123')
print(result)