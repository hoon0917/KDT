import csv
import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

def parse_disctrict_name(city):
    
    '''행정구역 명칭에서 숫자부분을 제거함
    - 서울특별시 종로구(111100000)'''

    city_name=re.split('[()]',city)         # 행정구역 명칭의 () 삭제
    return city_name[0]

def print_population(population):
    '''
    특정 지역의 인구 현황을 화면에 출력함
    '''
    
    for i in range(len(population)) :                               # len(population)이 나이의 범위
        print(f'{i:3d}세: {population[i]:4d}명',end=' ')            
        if (i+1)% 10 == 0:                                          # 0~9세를 표현하기 위해 사용
            print()

def draw_population(city_name,population_list):
    '''
    특정 ㅣ역에 대한 인구 분포를 그래프로 나타냄(plot)
    - city_name : 지역이름
    - populaton_list : 0~100세 이상까지 인구수 리스트
    '''

    plt.title(f'{city_name} 인구 현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')
    plt.bar(range(101),population_list)
    plt.xticks(range(0,101,10)) # 0세 ~ 100세 이상
    plt.show()


def get_population(city):
    f=open('age.csv',encoding='euc-kr')
    data=csv.reader(f)
    next(data)

    population_list=[]
    full_district_name=''
    for row in data :
        if city in row[0]:
            full_district_name=parse_disctrict_name(row[0])         # parse 함수는 도시의 이름 뒤에 붙어 있는 ()를 지우기 위해 있는 것이고
            for data in row[3:]:                                    # ()가 지워진 도시이름 뒤에 연령들이 붙어있는 리스트 형태가 되어 있을거니까 0번 원소를                                             
                data=data.replace(',','')                           # 가져와 full_district 로 함
                population_list.append(int(data))
            break   # 처음으로 일치하는 도시명만 검색하기 위함
    f.close()
    print_population(population_list)
    draw_population(full_district_name,population_list)

city=input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)를 입력하세요 :')
get_population(city)
