# ------------------------------------------------------------------------------------------
# 내장함수
# ------------------------------------------------------------------------------------------
# 숫자 데이터 절대값 계산해주는 내장함수 abs(n)
a=print(abs(-9))

print(type(a))

# 최대값, 최솟값 찾아주는 내장함수 max(), min()

print(max(10,3), min(10,3))

# 제곱근 계산 내장함수 pow()

print('연산자 ** :', 2**3)
print('내장함수 pow :', pow(2,3))

# 파일관련 내장함수 open(파일명, 동작모드, 인코딩)
# -기본값 : 동작모드 - 읽기 read
#          인코딩 - 시스템 따라서 
FILENAME = '0628.txt'

#(1) 파일열기 - 쓰기모드
file=open(FILENAME, 'w', encoding='utf-8')
#(2) 데이터 쓰기
file.write("Hello\n",)
file.write("감자")
#(3) 파일 닫기
file.close()