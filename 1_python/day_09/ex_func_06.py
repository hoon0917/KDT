# ------------------------------------------------------------
# 람다표현식 또는 람다함수
# - 1줄 함수, 익명 함수
# - 형식 : lambda 매개변수 : 실행코드
# ------------------------------------------------------------
# names={1:'Kim',2:'Adam',3:'Zoo'}

# # 정렬하기 => 내장함수 sorted() ---> list 반환
# # [기본] key로 정렬
# result=sorted(names.items())
# print('오름차순 정렬[key 기준]',result)

# # value로 정렬 => names.items() --> (1,'kim'),(2,'Adam'),(3,'Zoo')
# result=sorted(names.items(),key=lambda items :items[1])
# print('오름차순 정렬[value 기준]',result)

# print('-'*10)

# sorted("This is a test string from Andrew".split())
# print(result)

# print('-'*10)

# print(sorted("This is a test string from Andrew".split(), key=str.lower))
# print(result)

## map()와 lambda ---------------------------------------------------------
data=[11,22,33,44]

# - 각 원소의 값에 곱하기 2해서 다시 리스트로 저장
def muilti2(value) : return value * 2
# data2=list(map(muilti2,data))
data2=list(map(lambda a:a*2,data))
print(data2)