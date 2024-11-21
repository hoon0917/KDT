# 신검 만들기
# 1. 시력 입력 
#  1-1. 왼쪽 시력 입력(교정 시력)
#   1-1-1. 0.1 이하 면제 아니면 현역
#  1-2. 오른쪽 시력 입력(교정 시력)
#   1-2-1. 0.1 이하 면제 아니면 현역
#  1-3. if 왼쪽 or 오른쪽 == '면제': 면제
#  1-4. result1 == 현역 or 면제
# 2. 혈압 입력
#   2-1. 수축기 입력 140 이상 
#   2-1-1. 한번 더 수축기 입력
#   2-1-2. 수축기 140이상 면제
#   2-2. 이완기 입력 90 이상 
#   2-2.1 이완기 재측정 후 입력
#   2-2-2. if 이완기 >= 90 : 면제
#   2-3. 수축기 or 이완기 == '면제' :면제
#   2-4. result2 == 현역 or 면제
# 3. 체중 및 키 입력 후 BMI 계산
#   3-1. BMI 30 이상 == 면제
#   3-2. result3 == 현역 or 면제
# 4.
# result==현역 and result2==현역 and result3 == 현역 :
#     print(현역)
# else :
#     print(면제)

# 합격이면 10점 불합격이면 5점을 줘서
# 총점 >= 20 : 현역
# 10 < 총점 < 20 : 재검대상
# # 총점
# eye=input('교정된 좌, 우 시력을 입력하세요(예: 0.8 0.9) : ').split()
# # if float(eye) :
# #     if len(eye) == 2 and isinstance(eye[:1]):
# #         print(eye)
# #         if eye[0] >= 0.6 and eye[1] >= 0.6 :
# #             print('10점입니다.')
# #         else :
# #             print('5점입니다.')
# #     else :
# #         print('시력을 다시 입력해주세요.')


# if isinstance(eye[0],float) :
#     print('실수입니다')
# else : 
#     print('실수가 아닙니다')

# input()으로 입력 받고 문자열을 isinstance로 검사하면 무조건 실수가 아니라고 뜰꺼고
# 처음부터 map으로 float을 씌우자니 특수기호는 float이 씌워지지가 않는다

# 반복문을 통해 실수를 입력하게 하는 함수를 만들어서 넣어야 되겠네

# while True :
#     eye=input('좌,우 시력을 입력하세요 (예 : 1.0 0.9)').split()
#     if eye.isdigit() : 
#         print('실수입니다.')
#         break
#     else :
#         print('잘못된 입력입니다. 시력을 다시 입력해 주세요2.')
    # if len(eye) == 2 :
    #     if eye[0] >= 0.6 and eye[1] >= 0.6 :
    #         print('10점입니다.')
    #     else : 
#     #         print('5점입니다.')
#     # else : 
#     #     print('잘못된 입력입니다. 시력을 다시 입력해 주세요3.')
# def float_check(str) :
#     if '.' in str :
#         str = str.split('.')
#         if str[0].isdecimal() and str[1].isdecimal() :
#             return True
#         else :
#             return False
#     else :
#         return False
    
# result=[0,0]

# leye=input('교정된 왼쪽 시력을 입력하세요.(예: 0.8) : ')
# if float_check(leye) : 
#     leye=float(leye)
# else :
#     print('왼쪽 시력을 다시 입력해주세요.')   
# print(type(leye))    

# if leye >= 0.6 :
#     result[0] = 10   
# else :
#     result[0]=5
# print(result)
      
