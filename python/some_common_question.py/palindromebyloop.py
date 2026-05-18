num=int(input("Enter a no.:"))
print(num)
original_num=num
rev=0
while num>0:
    number=num%10
    rev=rev*10+number
    num=num//10
print("Reverse of no. is:",rev)
if original_num ==rev:
    print("no. is palindrome")
else:
    print("no. is not palindrome")