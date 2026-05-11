# validity check of triangle

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

# first check if triangle is valid

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        print("Equilateral → all sides equal", side1, side2, side3)
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles → two sides equal", side1, side2, side3)
    else:
        print("Scalene → all sides different", side1, side2, side3)
else:
    print("Invalid triangle")