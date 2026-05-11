# check pass and fail

mark1 = int(input("Enter mark1: "))
mark2 = int(input("Enter mark2: "))
mark3 = int(input("Enter mark3: "))
total = mark1 + mark2 + mark3
percentage = total / 3
print(percentage)
if percentage >= 33 and percentage <= 100:
    print("pass")
else:
    print("fail")
if percentage >= 90 and percentage <= 100:
    print("grade A")
elif percentage >= 80 and percentage < 90:
    print("grade B")
elif percentage >= 70 and percentage < 80:
    print("grade C")
elif percentage >= 60 and percentage < 70:
    print("grade D")
elif percentage >= 33 and percentage < 60:
    print("grade E")
else:
    print("grade F")
