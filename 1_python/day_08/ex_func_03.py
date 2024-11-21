# -------------------------------------------------
# 사용자 정의 함수 - 실습
# 함수 기능 : 원하는 단의 구구단을 출력해주는 기능 함수
# 함수 이름 : gugu
# 매개 변수 : num1
# 함수 결과 : 구구단 출력 print(result)
# -------------------------------------------------
def gugu(num1) :
    for i in range(1,10):
        print(f'{num1} * {i} = {num1*i}') 


gugu(6)




# -------------------------------------------------
# 함수 기능 : 파일의 확장자를 반환해주는 기능 함수
# 함수 이름 : ext
# 매개 변수 : file_name
# 함수 결과 : 확장자 str
# ------------------------------------------------- 
# 리스트에 있는 원소를 각각 뽑아서 '.'을 기준으로 뒤로 슬라이싱
def ext(files):
    for file in files :
        idx=file.rfind('.')
        result=file[idx+1:]
    return result
    
test=ext('ㅎest.mxm')
print(test)

# [방법2]
# def extract(file_name):
#     return(file_name[file_name.rfind('.')+1:])

# print(extract('abc.txt','abc.jpg'))


    

