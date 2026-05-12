# #coversion list to tuple ,tuple to list
lis=[]
num=int(input("enter element in tuple:"))
for i in range(num):
    lis.append(int(input("enter a no.:")))
lis=tuple(lis)
print(lis)    
tup=list(lis)
print(tup)
