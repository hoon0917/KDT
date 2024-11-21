# ------------------------------------------------------------------
# str 데이터 타입 전용 함수 즉, 메서드 살펴보기
# ------------------------------------------------------------------
## [1개 문자열을 여러개 문자열로 분리해주는 메서드 split()]
## - 분리기준 -> 기본값 : 공백
msg=' Happy New Year '
result=msg.split()
print(f' result => {result},type(result)')

phone='010-9897-1375'
presult=phone.split('-')
print(presult)

msg='오늘은 날씨가 좋군요. 내일도 날씨가 좋을까요?'
result=msg.split('.')
print(result)

## [여러개 문자열을 1개 문자열로 합쳐주는 메서드 join()]
## - 형식 : 합칠문자.join(여러개 문자열)
## -> 010*9897*1375

con='+*'
phone2=con.join(presult)
print(phone2)
