import random


heungboo_total=0
nolboo_total=0
sticks=[0,0,0,0]
while True :    
    while True :
            if heungboo_total >=20 :
                break 
            for i in range(4):
                sticks[i]=random.randint(0,1)
            if sum(sticks) == 4 :
                heungboo_total += 5
                print(f' 흥부 {sticks}: 모 (5점)/총 ({heungboo_total}점) -->')
            elif sum(sticks) == 0 :     # 윷
                heungboo_total += 4
                print(f' 흥부 {sticks}: 윷 (4점)/총 ({heungboo_total}점) -->')
            elif sum(sticks) == 3 :     # 도
                heungboo_total += 1
                print(f' 흥부 {sticks}: 도 (1점)/총 ({heungboo_total}점) -->')
                break
            elif sum(sticks) == 2 :     # 개
                heungboo_total += 2
                print(f' 흥부 {sticks}: 개 (2점)/총 ({heungboo_total}점) -->')
                break
            elif sum(sticks) == 1 :     # 걸
                heungboo_total += 3
                print(f' 흥부 {sticks}: 걸 (3점)/총 ({heungboo_total}점) -->')
                break
    if heungboo_total >= 20 :
        print(f' 흥부 승리 => 흥부: {heungboo_total}. 놀부:{nolboo_total}')
        break
    elif nolboo_total >= 20 :
        print(f' 놀부 승리 => 흥부: {heungboo_total}. 놀부:{nolboo_total}')
        break    
    while True : 
            if nolboo_total >=20 :
                break      
            for i in range(4):
                sticks[i]=random.randint(0,1)
            if sum(sticks) == 4 :
                nolboo_total += 5
                print(f' {" "*30}<-- 놀부 {sticks}: 모 (5점)/총 ({nolboo_total}점) ')
            elif sum(sticks) == 0 :     # 윷
                nolboo_total += 4
                print(f' {" "*30}<-- 놀부 {sticks}: 윷 (4점)/총 ({nolboo_total}점) -->')
            elif sum(sticks) == 3 :     # 도
                nolboo_total += 1
                print(f' {" "*30}<-- 놀부 {sticks}: 도 (1점)/총 ({nolboo_total}점) -->')
                break
            elif sum(sticks) == 2 :     # 개
                nolboo_total += 2
                print(f' {" "*30}<-- 놀부 {sticks}: 개 (2점)/총 ({nolboo_total}점) -->')
                break
            elif sum(sticks) == 1 :     # 걸
                nolboo_total += 3
                print(f' {" "*30}<-- 놀부 {sticks}: 걸 (3점)/총 ({nolboo_total}점)  -->')
                break
    if heungboo_total >= 20 :
        print(f' 흥부 승리 => 흥부: {heungboo_total}. 놀부:{nolboo_total}')
        break
    elif nolboo_total >= 20 :
        print(f' 놀부 승리 => 흥부: {heungboo_total}. 놀부:{nolboo_total}')
        break        
       
              
               
        
            
        


