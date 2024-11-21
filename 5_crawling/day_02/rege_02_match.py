# Match, groups 사용

import re

tel_checker = re.compile(r'^(\d{2,3})-(\d{3,4})-(\d{4})$') # '-'가 포함안되는 이유 : \-가 되어 있기 때문에 특수기호로 인정

print(tel_checker.match('02-123-4567'))
match_groups = tel_checker.match('02-123-4567').groups() # 매칭 되는 전체 문자 튜플 리턴
print(match_groups)

print('-------- 잘못된 예시 --------')
print(tel_checker.match('053-950-45678')) # 숫자 자리수  벗어남
print(tel_checker.match('0523-4567'))     # '-'가 없음


# Match, replace 사용
print('****************** match, replace 사용 *******************')

tel_number = '053-950-4567'
tel_number = tel_number.replace('-','')
print(tel_number)

tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234')) # 02-395-1234

# group, groups, group(index)
print('***************group, groups 사용 **********************')

tel_checker = re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
m = tel_checker.match('02-123-4567')

print(m.groups())
print('group():', m.group())
print('group(0):', m.group(0))
print('group(1):', m.group(1))
print('group(2,3):', m.group(2,3))
print('start():', m.start()) # 매칭된 문자열의 시작 인덱스
print('end():', m.end())     # 매칭된 문자열의 마지막 인덱스 +1


# 휴대전화번호
#(?:0|1|[6-9])
# -? 뒤에 따라 나오는 숫자를 하나의 그룹으로 합침

print('**********************휴대폰 사용*******************************')
cell_phone = re.compile('^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$')

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))
print(cell_phone.match('010-1234567'))