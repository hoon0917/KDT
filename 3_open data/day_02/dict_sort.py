dict_file ={'Seoul':['South Korea','Asia', 9655000],
            'Tokyo':['Japan', 'Asia', 14110000],
            'Beijing':['China', 'Asia', 21540000],
            'London':['United Kingdom', 'Europe', 14800000],
            'Berlin':['Germany', 'Europe', 3426000],
            'Mexico City':['Mexico', 'America', 21200000]}


def print_menu():
    print('-'*30)
    print('1. 전체 데이터 출력')
    print('2. 수도 이름 오름차순 출력')
    print('3. 모든 도시의 인구수 내림차순 출력')
    print('4. 특정 도시의 정보 출력')
    print('5. 대륙별 인구수 계산 및 출력')
    print('6. 프로그램 종료')


## 1.  딕셔너리의 인덱스 번호 이용한 넘버링과 key 와 value 값 출력
def choice_1():
    for i, (key, value) in enumerate(dict_file.items()) :
        print(f' [{i+1}] {key}: {value}')


## 2.  딕셔너리 인덱스 번호 사용, value 값 리스트 벗겨서 출력, 숫자는 천단위 표시
def choice_2():
    for i, (key,value) in enumerate(sorted(dict_file.items())) :
        # print(value)
        print(f'[{i+1}]{key} :{value[0]} {value[1]} {value[2]:,}')


## 3.  보류
# dict_file_reverse=sorted(dict_file.items(), key = lambda x : x)
# def choice_3():
    
    
#     for i,(key, value) in enumerate(dict_file_reverse) :
#         print(f'[{i+1}] {key} {value}')

## 4.  특정 도시의 정보 출력
# - 화면에서 입력받은 수도 이름이 딕셔너리의 key에 존재하면 해당 도시의 정보 출력
# - 존재하지 않으면 문구 출력
def choice_4():
    city=input('도시를 입력하세요 : ')
    if city in dict_file.keys() :
        print(f'도시:{city}')
        print(f'국가:{dict_file.get(city)[0]}, 대륙:{dict_file.get(city)[1]}, 인구수:{dict_file.get(city)[2]:,}')
    else :
        print(f'도시이름:{city}는 key에 없습니다.')
        
         
        # print(f'국가:{dict_file.values[0]}')


## 5.  대륙별 인구수 계산 및 출력
# - 화면에서 대륙 이름을 입력 받고 해당 대륙에 속한 국가들의 인구수 출력 및 인구수 합 출력
# - 잘못된 대륙 이름 검사는 없음

def choice_5():
    continent=input('대륙을 입력하세요:')
    if any(continent in values for values in dict_file.values()):
        print(f'{dict_file.get(continent)[0]}')

## 6. 프로그램 종료

while True :
    print_menu()
    choice = input('메뉴를 입력하세요 :')
    if choice.isdecimal() :
        choice= int(choice)
    else :
        print('1~6 사이 숫자를 눌러 메뉴를 선택해주세요.')
        continue    

    if choice == 1 :
        choice_1()
    
    if choice == 2 : 
        choice_2()
    
    # if choice == 3 :
    #     choice_3()
    
    if choice == 4:
        choice_4()

    if choice == 5 :
        choice_5()

    if choice == 6 :
        break