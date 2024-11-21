# result=[]
# sub=[]
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# for i in data :
#     for j in i :
#         sub.append(j*1.00014)

# # 모르겠다 물어봐야징
# print(sub)
# print(result)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# for i in ohlc[1:] :
#     print(i[3])

# for i in ohlc[1:] :
#     if i[3] > 150 :
#         print(type(i[3]))
#         print(i[3])

# print('end')
# for i in ohlc[1:] :
# #     if i[3] >= i[0] :
# #         print(i[3])

# volatility=[]
# for i in ohlc[1:]:
#     volatility.append(i[1]-i[2])

# print(volatility)
# total=0
# for i in ohlc[1:] :
#     total=total+(i[0]-i[3])

# print(total)


#### 194번 리스트 안에 리스트로 들어가는 원리가 궁금해애애앵
print(round((77/(183*183))*10000,2))