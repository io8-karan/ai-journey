
#check prime``
num=int(input("Enter a limit:"))
count=0
if num<=1:
    print("not a prime no.")
for i in range(2,num+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            count+=1          
print("count of prime no. is",count)