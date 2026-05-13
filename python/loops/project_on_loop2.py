# grading system    
total = 0
fail = False

for i in range(1, 6):
    while True:
        marks = int(input(f"Enter marks of subject {i}: "))
        if 0 <= marks <= 100:
            total = total + marks
            if marks < 60:
                fail = True
            break
        else:
            print("Invalid! Enter between 0-100")

percentage = total / 5

print("Total:", total)
print("Percentage:", percentage, "%")

if fail:
    print("Grade F - Fail")
elif percentage >= 90:
    print("Grade A - Excellent")
elif percentage >= 80:
    print("Grade B - Very Good")
elif percentage >= 70:
    print("Grade C - Good")
elif percentage >= 60:
    print("Grade D - Average")
else:
    print("Grade F - Fail")