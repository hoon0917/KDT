import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tabulate


# 데이터 입력 받기
df = pd.read_csv('ch2_scores_em.csv',encoding='utf-8',index_col='student number')
df.head()

scores = np.array(df['english'][:10])
print(scores)

scores_df = pd.DataFrame({'score':scores},
                         index=pd.Index(['A','B','C','D','E','F',
                         'G','H','I','J']))

print(scores_df)

# 평균값 구하기
print(np.mean(scores))

# 중앙값 : 데이터를 크기 순으로 나열할 때 정확히 중앙에 위치하는 값
sorted_scores = np.sort(scores)
print(sorted_scores)

# 최빈값
print(pd.Series([1,1,1,2,2,3]).mode())

# 분산과 표준편차
# 편차 : 각 데이터가 평균으로부터 떨어져 있는 정도
mean = np.mean(scores)
deviation = scores - mean
print(deviation)

# summery_df에 편차 열 추가
summery_df = scores_df.copy()
summery_df['deviation'] = deviation # deviation은 위에서 구한 편차
print(summery_df)

# 편차 비교
# 편차의 평균은 항상 0이 나옴
print(summery_df.mean())

# 분산
# 분산 : 편차의 제곱
# 분산 구하기 1) 편차에 제곱해주기
np.mean(deviation**2)

# 분산 구하기 2) np.var()함수 사용하기
print(np.var(scores))

# numpy로 분산 구하기
# summery_df에 편차의 제곱 열 추가
summery_df['square of deviation'] = np.square(deviation)
print(summery_df)

print(summery_df.mean())

# 표준편차
print(np.sqrt(np.var(scores,ddof=0)))

print(np.std(scores,ddof=0))

# 범위와 사분위 범위
# 범위 구하기
print(np.max(scores) - np.min(scores))

# 사분위 범위 : 상위수%와 하위수%에 위치하는 값의 차이
# 사분위 범위 공식 : IQR = Q3 - Q1
scores_Q1 = np.percentile(scores,25)
scores_Q3 = np.percentile(scores,75)
scores_IQR = scores_Q3 - scores_Q1
print(scores_IQR)

# describe로 전체 정보 보기
print(pd.Series(scores).describe())

# 데이터의 정규화
z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)
print(z)

# 데이터의 주요지표
## 50명의 영어점수 array
english_scores = np.array(df['english'])

# series로 변환하여 describe() 표시
pd.Series(english_scores).describe()

# 도수분포표
freq,_ = np.histogram(english_scores, bins =10, range=(0,100))
print(freq)

## 0~10, 10~20 ... 이라는 문자열 리스트 작성
freq_class = [f' {i} ~ {i+10}' for i in range(0,100,10)]

## freq_class를 인덱스로 DAtaFrame 작성
freq_dist_df = pd.DataFrame({'frequency':freq},
                            index=pd.Index(freq_class,name = 'class'))
print(freq_dist_df)

# 계급값
## 가 ㄱ계급을 대표하는 값으로 계급의 중앙값을 이용
class_value = [(i+(i+10))//2 for i in range(0,100,10)]
print(class_value)

# 상대도수
rel_freq = freq / freq.sum()
print(rel_freq)

# 누적상대도수
## 해당 계급까지의 상대도수의 합
cum_rel_freq = np.cumsum(rel_freq)
print(cum_rel_freq)

# 히스토그램 작성
fig = plt.figure(figsize=(10,8))

ax = fig.add_subplot(111)
freq,_,_ = ax.hist(english_scores, bins=10, range=(0,100))
ax.set_xlabel('score')
ax.set_ylabel('person number')
ax.set_xticks(np.linspace(0,100,10+1))
ax.set_yticks(np.arange(0,freq.max()+1))
plt.show()

## 계급수를 25, 계급폭을 4점으로 하는 히스토그램을 주넉 상대도수의 꺾은선 그래프와 함께 그림
fig = plt.figure(figsize=(10,8))
ax1= fig.add_subplot(111)
ax2=ax1.twinx()

weights = np.ones_like(english_scores) / len(english_scores)
rel_freq,_,_ = ax1.hist(english_scores,bins=25,
                        range=(0,100), weights=weights)

cur_rel_freq = np.cumsum(rel_freq)
class_value = [(i+(i+4))//2 for i in range(0,100,4)]

ax2.plot(class_value, cum_rel_freq, ls='--', marker='o', color='gray')

ax2.grid(visible=False)

ax1.set_xlabel('score')
ax1.set_ylabel('person number')

plt.show()