# 전방 탐색(lookahead)
# 전방 긍정 탐색(?=) : 패턴과 일치하는 문자열을 만나면 패턴 앞의 문자열 반화
# 전방 부정 탐색(?!) : 패턴과 일치하지 않는 문자열 만나면 패턴 앞 문자열 반환

import re

# 전방 긍정 탐색
## ( 문자열이 won을 포함하고 있으면 won 앞의 문자열 리턴)
lookahead1 = re.search('.+(?=won)', '1000 won')
if(lookahead1 != None):
    print(lookahead1.group())
else:
    print('None')

## 
lookahead2 = re.search('.+(?=am)', '2023-01-26 am 10::50:55')
print(lookahead2.group())

# 전방 부정 탐색
## (4자리 숫자 다음에 '-'를 포함하지 않으면 앞의 문자열 리턴)
lookahead3 = re.search('\d{4}(?!-)','010-1234-5678')
print(lookahead3)