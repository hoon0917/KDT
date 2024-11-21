# dict(키1=값1,키2=값2)         키1=값1 형태 여기에 키는 '' 빠져야 됨
# dict(zip([키1,키2]),[값1,값2])    집으로 리스트 형태 합치기
# dict([(키1,값1),(키2,값2)])       튜플 형태
# dict({키1:값1,키2:값2})           딕셔너리 형태
a=dict(zip(['health','health_regen','mana'],[500,3.5,250]))
print(a) 
b=dict(health=100,mana=200)
print(b)
c=dict([('health',100),('mana'=200)])
print(c)