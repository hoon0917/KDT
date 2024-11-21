# -----------------------------------------------------
# Dict 전용 함수 즉, 메서드
# -> keys(), values(), items()
# -----------------------------------------------------
person={'name':'홍길동','age':10}

# 메서드 - 값 읽어오는 메서드 get(key, default)-------------------
# - key에 해당하는 value가 없으면 default값을 반환
print(person['name'])
#print(person['gender']) #KeyError
print(person.get('name','몰라'))
print(person.get('gender','없음'))
print(person.get('gender'))

# [메서드 - 키와 값 추가 메서드]-----------------------------------
person['gender']='남'
person.setdefault('height',100)

# [메서드 - 수정 및 추가 업데이트 메서드 update(키=값)]----------------------
# 수정/업데이트
person.update(gendaer='어린이',job='학생')
print(person)

# 딕셔너리 형태
person.update({'phone':'010','birth':'950917'})
print(person)

## (**{'weight':'100','hobby':'judo'}) 

person.update(**{'weight':'100','hobby':'judo'})
print(person)

# 문자열 내에 각각의 알파벳이 몇개인지 세기
# msg="Hello Good Luck"
# a=set(msg) # 중복 삭제를 위해
# save={}
# for m in a :
#     print(m, msg.count(m))
#     save[m]=msg.count(m)
# print(save)
