def print_menu() :
    print(f'{"*":*^15}')
    print(f'{"즐거운 신체검사":*^8}')
    print(f'{"*":*^15}')
    print(f'{"* 1  시력입력 *":15}')
    print(f'{"* 2  혈압입력 *":15}')
    print(f'{"* 3  BMI입력  *":15}')
    print(f'{"* 4  현재점수 *":15}')
    print(f'{"* 5  입대기준 *":15}')
    print(f'{"* 6  결과보기 *":14}')
    print(f'{"*":*^15}')


def float_check(str) :
    if '.' in str :
        str = str.split('.')
        if str[0].isdecimal() and str[1].isdecimal() :
            return True
        else :
            return False
    else :
        return False
    

result=[0,0,0,0,0]
while True :
    
    print_menu()
    
    choice=input('1 ~ 6 사이 숫자를 눌러 메뉴를 선택해주세요.')
    if choice.isdecimal() :
        choice=int(choice)
    else :
        print('1 ~ 6 사이 숫자를 눌러 메뉴를 선택해주세요.')
        continue
    
    if choice == 1 :
        while True :
            leye=input('교정된 왼쪽 시력을 입력하세요.(예: 0.8) : ')
            if float_check(leye) :
                leye=float(leye)
                if 0.0 <= leye <= 9.0 :
                    if 0.6 < leye  :
                        result[0] = 10
                        break
                    else :
                        result[0]=5
                        break  
                else : 
                    print('왼쪽 시력을 다시 입력해주세요.')
                    continue
            else :
                print('왼쪽 시력을 다시 입력해주세요.')
                continue            
        while True :
            reye=input('교정된 오른쪽 시력을 입력하세요.(예: 0.8) : ')
            if float_check(reye) :
                reye=float(reye)
                if 0.0 <= reye <= 9.0 :
                    if 0.6 < reye  :
                        result[1] = 10
                        break
                    else :
                        result[1]=5
                        break 
                else :
                    print('오른쪽 시력을 다시 입력해주세요.')
                    continue
            else :
                print('오른쪽 시력을 다시 입력해주세요.')
                continue  
    if choice == 2 :
        while True :
            shi=input('수축기 혈압을 입력해주세요 (예 140) :')
            if shi.isdecimal()  :
                shi=int(shi)
                if 10 <= shi <= 300 :
                    if shi >= 140 :
                        result[2]=5
                        break
                    else :
                        result[2]=10
                        break
                else :
                    print('수축기 혈압을 다시 입력해주세요.')
                    continue
            else :
                print('수축기 혈압을 다시 입력해주세요.')
                continue      
        while True :    
            rel=input('이완기 혈압을 입력해주세요 (예 90) :') 
            if rel.isdecimal() :
                rel=int(rel)
                if 10 <= rel <= 300 :
                    if rel >= 90 :
                        result[3]=5
                        break
                    else :
                        result[3]=10
                        break
                else :
                    print('이완기 혈압을 다시 입력해주세요.')
                    continue
            else :
                print('이완기 혈압을 다시 입력해주세요.')
                continue   

    if choice == 3 :    
        while True :
            height = input('키를 입력해주세요 (예 182.5) : ')
            if float_check(height) :
                    height=float(height)
                    if 10 <= height <= 250 :
                        break
                    else :
                        print('키를 다시 입력해주세요.')
                        continue        
            else :
                print('키를 다시 입력해주세요.')
                continue    
        while True :
            weight = input('몸무게를 입력해주세요 (예 77.0) : ')
            if float_check(weight) :
                    weight=float(weight)
                    if 10 <= weight <= 250 :
                        break
                    else :
                        print('몸무게를 다시 입력해주세요.')
                        continue   
            else : 
                print('몸무게를 다시 입력해주세요')
                continue
        bmi = weight/(height*height)
        bmi=(bmi*10000)
        if bmi < 16 or bmi >= 35 : 
            result[4]=5
        else : 
            result[4]=10   
    
    if choice == 4 :
        print(f"좌_시력: {result[0]}점, 우_시력: {result[1]}점, 혈압_수축기: {result[2]}점, 혈압_이완기: {result[3]}점, BMI: {result[4]}점 \n총점: {sum(result)}점 입니다.")

    if choice == 5 :
        print('총점 45점 이상 : 현역 ')
        print('총점 35점 이상 45점 미만 : 재검')
        print('총점 25점 이상 35점 미만 : 공익')
        print('총점 25점 미만 : 면제')

    if choice == 6 :
        if 0 in result :
            print('아직 하지 않은 검사가 있습니다.\n현재점수를 보고 진행 하지 않은 검사를 해주세요.')
            continue
        if sum(result) >= 45 : print("""!!!!!!!축하드립니다!!!!!! 현역입영 대상입니다!!!!!
        ~~                                                                                          
      :@###=*~.,                                                                                    
    @@@@@@@@@@@=                                                                                    
    @@=     ,=@=                                                                                    
   ,$         .=                                                                                    
   ,   .$ .=   $                                                                                    
   !    =  -   -                                                                                    
   $    $ ::   -                                                                                    
         !-     ,                                                                                   
 ;-  ;   .   ~  $.#                                                                                 
~.   = -*-~=-;   ~:                                                                                 
 -    - :==:.~    -                                                                                 
  -   .      .  :.                                                                                  
 -~:  !     ,  ,-                                                                                   
 -  =  :- .~,  ;                                                                                    
 .~ #.  ,::. ,,                                                                                     
  =   @:~  ~;~                                                                                      
 .- .. $*;!;;;!                                                                                     
 ~    .#:;:;!:;                                                                                     
 -   ;  !~;!;!!                                                                                     
  *    .$!=#*,                                                                                      
  .=..#:;;==!:                                                                                      
     $:::*;***                                                                                      
    .::;#*#::!:                                                                                     
    .$$@#-$#$@=                                                                                     
  -=$$$$$-$$$$$$=""")
        elif 35 <= sum(result) < 45 : print('재검 대상입니다.') 
        elif 25 <= sum(result) < 35 : print('아쉽게도 공익이네요...')   
        else : print('면제입니다ㅠㅠㅠㅠㅠㅠㅠㅠ')
        result=[0,0,0,0,0]
        break




         