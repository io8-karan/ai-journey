
# check armstrong no.=s a positive integer that equals the sum of its own digits, each raised to the power of the total number of digits in the number. 

num=(input("enter a no."))
temp=num
sum=0
i=0
count_digit=len(num)    
while temp > 0:
     number=temp%10
     rev=number**count_digit
     sum+=rev
     temp=temp//10
     i+=1
if sum == num:
     print("Armstrong number")
else:
     print("Not an Armstrong number")
