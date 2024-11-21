lux4= dict({'health':490,'mana':150})
print(lux4)

print(lux4['health'])
print(lux4)

lux4['health']= 350
print(lux4)

# 딕셔너리는 변경 가능
lux4['mana_regen']=19.5
print(lux4)

# print(lux4['mana_hp'])

print('health' in lux4)

print('health' not in lux4)
print(lux4,len(lux4))

print(lux4['health'])
