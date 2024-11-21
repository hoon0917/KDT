# 1000개 뉴스 검색

import datetime
date_string = 'Tue, 13 Aug 2024 09:02:00 +0900'


# strptime : str -> datetime
pdate = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S +0900')
print(type(pdate))

# strftime : datetime -> str
pdate_string = pdate.strftime('%Y-%m-%d %H:%M%S')
print(type(pdate_string))
print(pdate_string)
