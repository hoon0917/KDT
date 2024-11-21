# 081
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b=scores

#082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b,*valid_score=scores

#083
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score,b=scores

#084
temp={}

#085
icecream={'메로나':1000,'폴라포':1200,'빵빠레':1800}

#086
icecream['죠스바']=1200
icecream['월드콘']=1500
print(icecream)

#087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f"메로나 가격 : {ice['메로나']}원")

#088
ice['메로나']=1300
print(ice)

#089
del ice['메로나']
print(ice)

#090
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 에러 이유 : 없는 딕셔너리 사용