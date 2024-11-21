# p.270 22.9
a=['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b=[i for i in a if len(i) == 5]

# p.271 22.10
start,stop=map(int,input().split())
num =[2**i for i in range(start,stop+1)]
print(num)
num.pop(1)
num.pop(-2)
print(num)

# 2번 방법
# result=[]
# for i in range(start,stop+1):
#     a=2**i
#     result.append(a)
    
# result.pop(1)
# result.pop(-2)
# print(result)  


# p.328 25.7
maria={'korean':94, 'english': 91, 'math':89, 'science':83}
avg=sum(maria.values())/len(maria)

# p.328 25.8
keys=input().split()
value=map(int,input().split())

x=dict(zip(keys,value))
print(x)
x= {key: value for key,value in x.items() if 'delta' not in key and value != 30}
print(x)

