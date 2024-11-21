# 전방 탐색(lookahead)
# 전방 긍정 탐색(?=) : 패턴과 일치하는 문자열을 만나면 패턴 앞의 문자열 반화
# 전방 부정 탐색(?!) : 패턴과 일치하지 않는 문자열 만나면 패턴 앞 문자열 반환

import re

# 후방 금정 탐색
## ('am' 다음에 문자가 1개 이상 있으면, 해당 문자열 리턴)
lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:10')
print(lookbehind1)

## ':' 뒤에 문자가 1개 이상 있으면 해당 문자열 리턴
lookbehind2 = re.search('(?<=:).+', 'USD: $51')

# 후방 부정 탐색
## 공백 다음에 $ 기호가 없고 숫자가 1개 이상이고 공백이 있는 경우
lookbehind3 = re.search(r'\b(?<!\$)\d+\b', 'I paid $30 for 100 apples')


