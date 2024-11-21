# # 171
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4) :
#     print(price_list[i])

# # 172
# # price_list = [32100, 32150, 32000, 32500]
# # for i in range(len(price_list)) :
#     print(i, price_list[i])

# 173
# price_list = [32100, 32150, 32000, 32500]
# for i in range(3,-1,-1) :
#     print(i, price_list[i])

# # 174
# price_list = [32100, 32150, 32000, 32500]
# for i in range(100,121,10) :
#     print(i,price_list[0])

# # 175
# my_list = ["가", "나", "다", "라"]
# # [0]일때 [0,1]
# # [1]일때 [1,2]
# # [2]일때 [2,3] 

# for i in range(1,len(my_list)) :
#     print(my_list[i-1],my_list[i])

# 176
# my_list = ["가", "나", "다", "라", "마"]
# # [0] - [0,1,2]
# # [1] - [1,2,3]
# # [2] - [2,3,4]
# for i in range(1,len(my_list)-1) :
#     print(my_list[i-1],my_list[i],my_list[i+1])

# 177
# my_list = ["가", "나", "다", "라"]
# # [3] -      [3,2]  
# # [2] -      [2,1]  
# # [1] -      [1,0]  
# for i in range(len(my_list)-1,0,-1) :
#     print(my_list[i],my_list[i-1])
#     print(i,i-1)

# # 178
# my_list = [100, 200, 400, 800]
# # [1] [1]-[0]
# # [2] [2]-[1]
# # [3] [3]-[2]
# for i in range(1,len(my_list)) :
#     print(my_list[i]-my_list[i-1])

# # 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# # [1]  [1-1] [1] [1+1]
# for i in range(1, len(my_list)-1) :
#     print((my_list[i-1]+my_list[i]+my_list[i+1])/3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
# 리스트에서 하나씩 뽑아서 변동폭을 구해
# 고가 - 저가 = 변동폭
# 5일간의 변동폭 - 5번 반복
# 없는 리스트를 만들어서 저장하라 했으니 빈 리스트 하나 작성해서 거기에
# 리스트 추가해주는 appent() 사용
volatility=[]
for i in range(len(low_prices)) :
    volatility.append([(high_prices[i]-low_prices[i])])
    
print(volatility)


