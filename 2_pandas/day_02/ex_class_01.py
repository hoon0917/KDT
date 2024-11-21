# ----------------------------------------------------------------
# 클래스(Class)
# - 객체지향언어(oop)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 잇는 데이터가 가진 속성과 기능 명시
# 구성요소 : 속성/attribute/field + 기능/method
# ----------------------------------------------------------------
# 클래스 정의 : 햄버거를 나타내느 클래스
# 클래스 이름 : Bugger
# 클래스 속성 : 번, 패티, 야채, 치즈
# 클래스 기능 : 햄버거 설명 기능 
# ----------------------------------------------------------------
# 클래스를 가지고 객체생성 코드를 짜야지 객체 생성할 수 있음
# self에는 객체의 주소값이 들어감
class Bugger :
    kind='맥도날드'
    # 힙 영역에 객채 생성 시 속성값 저장 기능
    def __init__(self,bread,patty,veg,kind) :
        self.bread=bread
        self.patty=patty
        self.veg=veg
        self.kind=kind    
    # 기능 즉 method
    def printInfo(self):
        print(f' 브랜드 : {self. kind}')
        print(f' 빵 종류 : {self. bread}')
        print(f' 패티 종류 : {self. patty}')
        print(f' 야채 종류 : {self. veg}')
    # 속성을 변경하거나 읽어 오는 메서드 => getter/setter 메서드(만들어야 됨)
    def get_bread(self) :  # ==> bread의 속성을 읽어주는 메서드 
        return self.bread 

    def set_bread(self,bread):  # ==> bread 속성을 변경해주는 메서드
        self.bread=bread
        #  
## 객체 생성----------------------------------------------------------
# 불고기 버거 객체 생성
bugger1=Bugger('브리오슈','불고기','양상추 토마토 양파','롯데리아')

# 치즈버거 객체 생성        
bugger2=Bugger('참깨곡물빵','쇠고기','양상추 토마토 양파 치즈','맥도날드')

# 버거 정보 확인
bugger1.printInfo()
# 속성 읽는 방법 : (1) 직접 접근해서 읽기, (2) 간접 접근해서 읽기 - getter 메서드 사용
print(bugger1.bread, bugger1.set_bread())

# 속성 변경 방법 : (1) 직접 접근해서 변경, (2) 간접 접근해서 변경 - setter 메서드 사용
# (1) 직접 접근 변경
bugger1.bread='들깨빵'
# (2) 간접 접근 변경
bugger1.set_bread('참깨빵')
bugger2.printInfo()

