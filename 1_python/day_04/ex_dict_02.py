# --------------------------------------------------------------------------------
# Dict 자료형 살펴보기
# - 여러가지 데이터를 dict 타입으로 저장
# --------------------------------------------------------------------------------
# [다양한 종류의 키] --------------------------------------------------------------
## - 키가 여러개 정보 합쳐서 사용하는 경우 tuple 타입
## - 예) 홍길동 1996, 홍길동 2000
person={'age':20, ('홍길동',2000):100}
print(person)

## 3명의 정보를 저장
p1={'name':'홍길동', 'age':20, 'job':'학생'}
p2={'name':'조조조', 'age':25, 'job':'무직'}
p3={'name':'주주주', 'age':28, 'job':'주부'}
p4={'name':'홍길동', 'age':78, 'job':'학생'}

persons=[p1,p2,p3,p4]
persons[0],['name']

# - 키 : 나이
persons2={20:{'name':'홍길동', 'job':'학생'},
          25:{'name':'조조조', 'job':'무직'},
          28:{'name':'주주주', 'job':'주부'},
          78:{'name':'홍길동', 'job':'학생'}}
print(persons2)

# - 키 : 이름과 나이 데이터
persons3={ ('홍길동,20'):{'job':'학생'},
           ('조조조,25'):{'job':'무직'},
           ('주주주,28'):{'job':'주부'},
           ('홍길동,78'):{'job':'학생'}}
          
print(persons3[('홍길동,20')])