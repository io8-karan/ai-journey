
# check no. enter is digit, alphabet or special character

char = str(input("Enter a character: "))
if char.isdigit():
    print("char is digit")
elif char.isalpha():
    print("char is alphabet")
else:
    print("char is special character")

# or
char = str(input("Enter a character: "))
if char.isalnum():
    print("char is digit or alphabet")
else:
    print("char is special character")