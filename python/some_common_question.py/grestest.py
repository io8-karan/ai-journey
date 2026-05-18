num1=int(input("Enter Number first:"))
num2=int(input("Enter Second Number:"))
num3=int(input("ENter Third Number:"))
print("User Entered",num1,"\n",num2,"\n",num3)
if(num1>=num2 and num1>=num3):
    print("num1 is greatest")
elif(num2>=num1 and num2>=num3):
    print("num2 is greatest")
else:
    print("num3 is grestest")