i = 0
largest = None

while i < 5:
    num = int(input("Enter number: "))
    print("You entered:", num)
    i+=1
    if largest is None or num>largest:
     largest = num
print("Largest:", largest)