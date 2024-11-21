# start, stop=map(int,input().split())

# a=[2**i for i in range(start,stop+1)]
# a.pop(1)
# a.pop(-2)
# print(a)

# result=[]
# for i in range(start,stop+1):
#     a=2**i
#     result.append(a)
    
# result.pop(1)
# result.pop(-2)
# print(result)  

data1=input().split()
data2=map(int,input().split())

a=dict(zip(data1,data2))
print(a)
x={key:value for key,value in a.items() if 'd' not in key and 3 != value }
print(x)