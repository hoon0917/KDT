# 클래스 생성

class VendingMachine:
    def __init__(self,input_dict):
        self.input_money=0
        input_dict={'coffee':100, 'cream':100, 'sugar':100,
                        'water':500, 'cup':5, 'change':0}
        self.inventory= input_dict
        
    def run(self):
        money=input('동전을 투입하세요:')
        if money >= 300 :
            print(money)
        else :
            print(f'투입된 돈 {money}원이 300원보다 작습니다')
            print(f'{money}원을 반환합니다')
            print('-'*20)
            print('커피 자판기 동작을 종료합니다.')
            print('-'*20)
        
VendingMachine
        