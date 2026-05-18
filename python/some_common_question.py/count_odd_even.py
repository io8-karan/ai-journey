i=0
even=0
odd=0
while i<5:
    num=int(input("Enter a number="))
    print(num)
    i+=1
    if num%2==0:
        even+=1
        print("count of even no. is:",even)
    elif num%2!=0:
        odd+=1
        print("count of odd no. is",odd)
    else:
        print("invalid input")    
