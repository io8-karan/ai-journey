# smallest find

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if num1 < num2 and num1 < num3:
    print("num1 is smallest", num1)
elif num2 < num1 and num2 < num3:
    print("num2 is smallest", num2)
else:
    print("num3 is smallest", num3)
