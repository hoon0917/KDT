# 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현

#  daegu-utf8.csv 또는 daegu-utf8-df.csv 파일 이용
#  데이터 구조
#  ['날짜', '지점', '평균기온', '최저기온', '최고기온’]
#   [0]       [1]       [2]       [3]         [4]
#  화면에서 측정할 달을 입력 받아서 진행
#  해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산
# - 최고기온 및 최저기온 데이터를 이용하여 입력된 달의 각각 평균값을 구함
# - 문자열 형태의 ‘날짜’ 열의 데이터는 datetime 으로 변경함:
#  하나의 그래프 안에 2개의 꺾은선 그래프로 결과를 출력
# - 마이너스 기호 출력 깨짐 방지
# - 입력된 월을 이용하여 그래프의 타이틀 내용 변경
# - 최고 온도는 빨간색, 최저 온도는 파란색으로 표시하고 각각 마커 및 legend를 표시
# --------------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib



def draw_two_plots(title,x_data,max_temp_mean,label_y1,min_temp_mean,label_y2):
    plt.rcParams['axes.unicode_minus']=False
    plt.plot(x_data,max_temp_mean,marker='s',markersize=6,color='r',label=label_y1)
    plt.plot(x_data,min_temp_mean,marker='s',markersize=6,color='b',label=label_y2)
    plt.xticks(x_data)

    plt.title(title)
    plt.legend()
    plt.show()




def main() :
    weather_df=pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'],format='%Y-%m-%d')

        
    
    first_year=int(input('시작 연도를 입력해주세요 :'))
    last_year=int(input('마지막 연도를 입력해주세요 :'))
    search_month=int(input('기온 변화를 측정할 달을 입력하세요: '))

    max_year_mean_temp_list=[0]*(last_year-first_year+1)
    min_year_mean_temp_list=[0]*(last_year-first_year+1)
   
    # 연도 입력 받기
    for i in (range(last_year - first_year + 1)) :
        max_decade_df=weather_df[(weather_df['날짜'].dt.year == first_year+i)&
                                   (weather_df['날짜'].dt.month == search_month)]
        max_year_mean_temp_list[i]=round(max_decade_df['최고기온'].mean(),1)
  
        min_decade_df=weather_df[(weather_df['날짜'].dt.year == first_year+i)&
                                   (weather_df['날짜'].dt.month == search_month)]
        min_year_mean_temp_list[i]=round(min_decade_df['최저기온'].mean(),1)
      


    print(f'{first_year}년부터 {last_year}년까지 {search_month}월의 기온 변화')
    print(f'{search_month}월 최저기온 평균 : {min_year_mean_temp_list}')
    print(f'{search_month}월 최고기온 평균 : {max_year_mean_temp_list}')
    
    x_data=[]
    for i in range(last_year - first_year + 1):
        x_data.append(first_year+i)
    draw_two_plots(f'{first_year}년부터 {last_year}년까지 {search_month}월 기온 변화',
                   x_data,max_year_mean_temp_list,'최고기온',
                   min_year_mean_temp_list,'최저기온')


main()
        


    
    

    
