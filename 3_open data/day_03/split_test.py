# str.split() 테스트

temp_string='1;2,3:456.789'

print(temp_string.split(';,'))          # (;,)을 단일 구분자로 취급
print(len(temp_string.split(';,')))           
                  
print(temp_string.split(','))           # 하나의 구분자만 가능
print(len(temp_string.split(',')))
city='대구광역시 북구 산경3동(237293)'
print(city.split('('))