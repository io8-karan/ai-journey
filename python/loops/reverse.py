# reverse 
num=int(input("Enter a number: "))
rev=0
i=0
while num>0:
    number=num%10
    rev=rev*10+number
    num=num//10
    i+=1
print("Reverse of no. is:",rev)   