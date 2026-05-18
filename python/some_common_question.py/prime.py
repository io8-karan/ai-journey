num=int(input("Enter a no.:"))
print(num)
if num<=1:
    
    print("not a prime no.")
else:
    for i in range(2,num):
        if num%i==0:
            print("not a prime no")
            break
    else:
            print("prime no")
           