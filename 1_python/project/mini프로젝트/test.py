from PIL import Image

def display_jpeg_image(image_path):
    try:
        image = Image.open(image_path)
        print(image)
    except Exception as e:
        print("Error:", e)
peg_image_path = "C::\\Users\\KDP-17\\Desktop\\제목 없음.jpg"

def print_menu() :
    print(f'{"*":*^15}')
    print(f'{"즐거운 신체검사":*^8}')
    print(f'{"*":*^15}')
    print(f'{"* 1  시력입력 *":15}')
    print(f'{"* 2  혈압입력 *":15}')
    print(f'{"* 3  BMI입력  *":15}')
    print(f'{"* 4  결과보기 *":14}')
    print(f'{"*":*^15}')

result=[0,0,0,0]
while True :
    
    print_menu()
    
    choice=input('1~9사이 숫자를 눌러주세요')
    if choice.isdecimal() :
        choice=int(choice)
    else :
        print('1~9 사이 숫자를 입력해주세요.')
        continue

    if choice == 1 :
        eye=list(map(float,input('교정된 좌, 우 시력을 입력하세요(예: 0.8 0.9) : ').split()))
        print(eye)
        if len(eye) == 2 :
            print(eye)
            if eye[0] >= 0.6 and eye[1] >= 0.6 :
                result[0]=10
            else :
                result[0]=5
        else :
            print('시력을 다시 입력해주세요.')

    if choice == 2 :
        shi=input('수축기 혈압을 입력해주세요 (예 140) :')
        if (len(shi) == 2 or len(shi) == 3) and shi.isdecimal()  :
            shi=int(shi)
            if shi >= 140 :
                result[1]=5
            else :
                result[1]=10
        else :
            print('수축기 혈압을 다시 입력해주세요.')
        rel=input('이완기 혈압을 입력해주세요 (예 90) :') 
        if rel.isdecimal() and (len(rel) == 2 or len(rel) == 3) :
            rel=int(rel)
            if rel >= 90 :
                result[2]=5
            else :
                result[2]=10
        else :
            print('이완기 혈압을 다시 입력해주세요.')
    
    if choice == 3 :    
        height = input('키를 입력해주세요 (예 182.5) : ')
        if height.isdecimal() : # 실수를 입력 받아서 isdecimal 이 false면 실수인거임 이걸로 실수 확인 가능
           height=float(height)
        else :
            height = float(height)
        weight = input('몸무게를 입력해주세요 (예 77.5) : ')
        if weight.isdecimal() :
            weight=float(weight)
        else : 
            weight = float(weight)
        print(type(weight),type(height))
        bmi = weight/(height*height)
        bmi=(bmi*10000)
        if bmi > 23 : 
            result[3]=5
        else : 
            result[3]=10
        
    if choice == 4 :
        print(result)
        if sum(result) >= 35 : print('!!!!!!!축하드립니다!!!!!! 현역입니다!!!!!')
        elif 25 <= sum(result) < 35 : print('재검 대상입니다.')    
        else : print('아쉽게도 면제입니다ㅠㅠㅠㅠㅠㅠㅠㅠ')
        result=[0,0,0,0,0]


# 같은 걸 한번 더 했을때 리스트에 계속 추가된다는 문제가 있음 해결
# 전부 다 실수입력을 위한 확인 필요
# 숫자 말고 다른거 집어 넣었을 때 어떡할래?



         
#shi.isdecimal() and