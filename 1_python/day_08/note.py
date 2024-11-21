# print('hello world'.replace('world','python'))

# # str.maketrans, translate
# table=str.maketrans('aebcd','12345')
# print('apple'.translate(table))

# # join 
# print(' '.join(['apple','berry']))
# print('-'.join(['apple','pear']))

# # lstrip, rstrip, strip
# print('  python'.lstrip())
# print('opopop     '.rstrip())
# print('   popopo popopo '.strip())

# print('oooooffffff'.lstrip('o'))

# print('python'.ljust(10))
# print('python'.rjust(10))
# print('python'.center(10))

# print('python'.upper().rjust(10))
# print('35'.zfill(5))
# # zfill : ()안 숫자로 문자열 길이를 맞추는데 빈 공간은 0으로 채움

# print('apple'.find('p'))
# print('apple'.rfind('p'))

# find : 찾을 문자열 없으면 -1 반환
# index : 찾을 문자열 없으면 ERROR 발생

# print('apple'.count('p'))
# count : 해당 문자열이 몇개 있는지 확인
# print(''.replace('','the'))
num=[1,2,3]
print(*num)