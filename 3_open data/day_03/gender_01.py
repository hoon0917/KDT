import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def print_population(population) :
    '''
    특정 지역의 인구 현황을 화면에 출력함
    '''
    for i in range(len(population)) :
        print(f'{i:3d}세: {population[i]:4d}명', end=' ')
        if (i + 1) % 10 == 0 :
            print()
    print()


def draw_gender_population(title,male_num_list, female_num_list) :
    # barh(y축 범위, data)
    plt.barh(range(len(male_num_list)), male_num_list, label = '남성')
    plt.barh(range(len(female_num_list)), female_num_list, label = '여성')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(title +' '+'성별 인구 비율')
    plt.legend()
    plt.show()

def calculate_population():
    f=open('gender.csv',encoding='euc-kr')
    data=csv.reader(f)
    male_num_list=[]
    female_num_list=[]

    district = input('시군구를 입력하세요: ')
    for row in data :
        if district in row[0]:
            for male in row[106:207] :
                male=male.replace(',','')
                male_num_list.append(int(male))
            for female in row[209:]:
                female=female.replace(',','')
                female_num_list.append(-int(female))
            break
    f.close()

    print(f'총 남성 인구수: {sum(male_num_list):,}')
    print_population(male_num_list)
    print('--------------------------------------------')
    print(f'총 여성 인구수: {sum(female_num_list):,}')
    print_population(female_num_list)
    draw_gender_population(district,male_num_list,female_num_list)

calculate_population()