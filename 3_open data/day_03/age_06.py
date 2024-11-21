import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_pie_chart(city,population_list,label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%',
            startangle=90, 
            textprops={'fontsize':8})
    
    plt.legend(loc=1)
    plt.title(city + '학령 인구 비율')
    plt.show()

def draw_donut_chart(city,population_list,label_list) :

    plt.pie(population_list, labels=label_list, autopct='%.1f%%',
            startangle=90,
            pctdistance=0.85, textprops={'fontsize':6})

    center_circle = plt.pie((0,0),0.7,facecolor='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.legend()
    plt.title(city + '학령 인구 비율')
    plt.show()


def get_population(row,start,end):
    population = 0
    for num in row[start:end+1]:
        num = num.replace(',','')
        num = int(num)
        population += num
    return population 



def shcool_age_population(city):
    city_population = 0
    non_shcool_pop = 0
    shcool_age_pop =0

    label_list=['초등학생','중학생','고등학생','대학생','비학령인구']
    population_list =[]

    f=open('age.csv',encoding='euc-kr')
    data=csv.reader(f)
    header=next(data) # 헤더 정보 건너뜀

    for row in data :
        if city in row[0]:
            city_population=row[1]
            city_population=city_population.replace(',','')
            city_population=int(city_population)


            # 초등학생 인구 계산: 6세[9] ~ 11세[14]
            elementary_pop = get_population(row,9,14)
            population_list.append(elementary_pop)

            # 중학생 인구 계산: 12세[15] ~ 14세[17]
            middleshcool_pop = get_population(row,15,17)
            population_list.append(middleshcool_pop)

            # 고등학생 인구 계산: 15세[18] ~ 17세[20]
            highschool_pop = get_population(row,18,20)
            population_list.append(highschool_pop)

            # 대학생 인구 계산: 18세[21] ~ 21세[24]
            university_pop = get_population(row,21,24)
            population_list.append(university_pop)

            shcool_age_pop = (elementary_pop + middleshcool_pop + 
                              highschool_pop + university_pop)
            
            # 비학령 인구 계산
            non_shcool_pop = city_population - shcool_age_pop
            population_list.append(non_shcool_pop)
            break
    
    
    school_age_pop_rate = round((shcool_age_pop*100)/city_population,1)

    print(f'전체 인구수: {city_population:,}')
    print(f'학령 인구수: {shcool_age_pop:,}')
    print(f'학령 인구 비율: {school_age_pop_rate}%')

    draw_pie_chart(city,population_list,label_list)
    draw_donut_chart(city,population_list,label_list)


city=input('학령인구를 분석할 도시 이름: ')
shcool_age_population(city)