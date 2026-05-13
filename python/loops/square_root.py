#  print square root 
num=int(input("Enter a number"))
for i in range(1,num+1):
    if num>0:
        perfect=num**0.5
    else:
        print("not a perfect no.")
print("perfect no.is :",perfect)   