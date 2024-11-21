# ------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# ------------------------------------------------------------------
msg='Hello 0705'

# [원소/요소 인덱스 찾기 메서드 - find(문자1개 또는 문자열)]
# - 'H'의 인덱스
idx=msg.find('H')
print(f'H의 인덱스 : {idx}')

idx=msg.find('7')
print(f'7의 인덱스 : {idx}')

idx=msg.find('llo')
print(f'llo의 인덱스 : {idx}')

# - 'llO'의 인덱스 ==> 대소문자 일치, 존재하지 않으면 -1 결과로 줌
idx=msg.find('llO')
print(f'llO의 인덱스 : {idx}')

# [원소/요소 인덱스 찾기 메서드 - index(문자1개 또는 문자열)]
# - 'H'의 인덱스
idx=msg.index('H')
print(f'H의 인덱스 : {idx}')

# -h의 인덱스 : 존재하지 않으면 Error 발생
# 'h'가 있는지 확인부터 하면 됨
if 'h' in msg :
    idx=msg.index('h')
    print(f'h의 인덱스 : {idx}')
else :
    print('h가 존재하지 않습니다')

# ---------------------------------------------------------------------
# 문자열에 동일한 문자가 여러개 존재 하는 경우
# ---------------------------------------------------------------------
msg='Good Luck Good'

# - 'o'의 인덱스 찾기 => 첫번째 'o'의 인덱스
# idx=msg.find('o') 
# print(f'o의 첫번째 인덱스 : {idx}')

# # - 'o'의 인덱스 찾기 => 두번째 'o'의 인덱스
# idx=msg.find('o',idx+1) # find 기본모양 : find(str,0)
# print(f'o의 두번째 인덱스 : {idx}')

# # - 'o'의 인덱스 찾기 => 세번째 'o'의 인덱스
# idx=msg.find('o',idx+1) # find 기본모양 : find(str,0)
# print(f'o의 세번째 인덱스 : {idx}')

# # - 'o'의 인덱스 찾기 => 네번째 'o'의 인덱스
# idx=msg.find('o',idx+1) # find 기본모양 : find(str,0)
# print(f'o의 네번째 인덱스 : {idx}')

cnt=msg.count('o')
idx=-1
for n in range(cnt):
    idx=msg.find('o',idx+1)
    print(f'{n+1}번째 o의 인덱스 : {idx}')

# ---------------------------------------------------------------------
# 문자열의 뒷부분부터 찾기 하는 메서드 ==>rfind()
# ---------------------------------------------------------------------
msg='happy'

# - 첫번째 'p' 인덱스 찾기 ==> 뒤에서부터 p를 찾으니 3 출력
idx=msg.rfind('p')
print(f'p의 인덱스 : {idx}') 

# - 두번째 'p' 인덱스 찾기 ==>
idx=msg.rfind('p',0,idx) # rfind(str,시작 인덱스, 끝 인덱스+1)
print(f'p의 인덱스 : {idx}') 

# - 파일명에서 확장자 txt
files=['hello.txt','2024년상반기경제분석.doc','kakao_12345566789.jpg']
for file in files :
    idx=file.rfind('.')
    print(file[idx+1:])