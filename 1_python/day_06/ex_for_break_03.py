dan=int(input("출력 원하는 단 입력 :"))
isbreak=False
for d in range(2,10) :
    print(f'\n[{d}단]', end='  ')
    for n in range(1,10):
        print(f'{d} * {n} = {d*n:2}',end=' ')
        if n == d : break
    if n==dan : break