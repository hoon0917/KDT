## [1] outer = 5, inner =5
# for i in range(5):
#     for j in range(5):
#         print(f'j:{j}',end=' ')
#     print(f'i:{i}\\n')
# for i in range(1,6) :
#     print('*'*i)

# for i in range(5):
#     for i in range(i+1):
#         print('*',end='')
#     print()

for i in range(5):
    for j in range(i+1):
        # if i==j :
        #     print('*', )
        # else : 
        #     print(" ",end="")
        print('*'if j >= i else ' ',end='\n' if j>=i else '')