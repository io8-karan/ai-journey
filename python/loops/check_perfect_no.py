  # check perfect number or not 
num=int(input("Enter a number"))
sum=0
for i in range(1,num-1):
    if num%i==0:
        print("divisor is:",i) 
        sum+=i
print("sum:",sum)    
if sum==num:
    print("perfect number")
else:
    print("Not a perfect number")  