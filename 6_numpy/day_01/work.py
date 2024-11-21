import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

seoul_data=pd.read_csv(r'C:\Users\KDP-17\EX_PANDAS6\numpy\day_01\과제1-데이터예시(seoul.csv).csv',encoding='utf-8')

print(seoul_data)

# 역별 승하차 객수 구하기

stations = set()
dict_people_count = dict()

# 역명의 중복 제거한 집합 생성
for i in range(0,len(seoul_data)):
    stations.add(seoul_data.iloc[i]['역명'])

# 역명과 값을 0으로 준 딕셔너리 생성
for station in stations:
    dict_people_count[station]=0
# print(dict_people_count)

# 각 역명에 해당하는 승하차객수 입력
for i in range(0, len(seoul_data)):
  current = seoul_data.iloc[i]
  station = current['역명']
  dict_people_count[station] = dict_people_count[station] + current['승하차객수']
# print(dict_people_count)

# 각 지하철 역별 평균 이용객 수



# # 가장 많은 이용객이 있는 역의 이용객 수
# print(max(data_df['승하차객수']))

# # # 가장 적은 이용객이 있는 역의 이용객 수
# # print(min(data_df['승하차객수']))

# # 이용객수가 가장 많은 역의 이름
# print(data_df['역명'])