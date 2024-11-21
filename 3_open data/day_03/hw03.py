import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re



## 지역명 옆 () 삭제
def parse_district_name(city):
    city_name=re.split('[()]',city)
    return city_name[0]


## pie 차트
def draw_pie_chart(male_list, female_list,city_list):
    fig=plt.figure(figsize=(30,15))
    ax1=fig.add_subplot(5,2,1)
    ax2=fig.add_subplot(5,2,2)
    ax3=fig.add_subplot(5,2,3)
    ax4=fig.add_subplot(5,2,4)
    ax5=fig.add_subplot(5,2,5)
    ax6=fig.add_subplot(5,2,6)
    ax7=fig.add_subplot(5,2,7)
    ax8=fig.add_subplot(5,2,8)
    ax9=fig.add_subplot(5,2,9)
    ax10=fig.add_subplot(5,2,10)

    list1=[male_list[0],female_list[0]]
    list2=[male_list[1],female_list[1]]
    list3=[male_list[2],female_list[2]]
    list4=[male_list[3],female_list[3]]
    list5=[male_list[4],female_list[4]]
    list6=[male_list[5],female_list[5]]
    list7=[male_list[6],female_list[6]]
    list8=[male_list[7],female_list[7]]
    list9=[male_list[8],female_list[8]]
    list10=[male_list[9],female_list[9]]
    
    plt.suptitle('대구광역시 구별 남녀 인구 비율',fontsize=20)
    ax1.pie(list1,labels=['남성','여성'],autopct='%.1f%%')
    
    ax2.pie(list2,labels=['남성','여성'],autopct='%.1f%%')
    ax3.pie(list3,labels=['남성','여성'],autopct='%.1f%%')
    ax4.pie(list4,labels=['남성','여성'],autopct='%.1f%%')
    ax5.pie(list5,labels=['남성','여성'],autopct='%.1f%%')
    ax6.pie(list6,labels=['남성','여성'],autopct='%.1f%%')
    ax7.pie(list7,labels=['남성','여성'],autopct='%.1f%%')
    ax8.pie(list8,labels=['남성','여성'],autopct='%.1f%%')
    ax9.pie(list9,labels=['남성','여성'],autopct='%.1f%%')
    ax10.pie(list10,labels=['남성','여성'],autopct='%.1f%%')
    
    ax1.set_title(city_list[0])
    ax2.set_title(city_list[1])
    ax3.set_title(city_list[2])
    ax4.set_title(city_list[3])
    ax5.set_title(city_list[4])
    ax6.set_title(city_list[5])
    ax7.set_title(city_list[6])
    ax8.set_title(city_list[7])
    ax9.set_title(city_list[8])
    ax10.set_title(city_list[9])
    
    plt.show()

    

## 출력값 구하기
def Daegu_gender():

    f=open('gender.csv', encoding='euc-kr') 
    data=csv.reader(f)
    male_list=[]
    female_list=[]
    city_list=[]
    for row in data :
        if '대구광역시' in row[0] :
            male_list.append(int(row[105].replace(',','')))
            female_list.append(int(row[208].replace(',','')))
            city_list.append(parse_district_name(row[0]))
            print(f'{parse_district_name(row[0])} :(남:{row[105]} 여:{row[208]})')   
    draw_pie_chart(male_list,female_list,city_list)

Daegu_gender()


