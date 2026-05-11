# check a no. enter by user is multiple of any two both no.

num = int(input("Enter a number: "))
check_no_1 = int(input("Enter check_no_1: "))
check_no_2 = int(input("Enter check_no_2: "))
if num % check_no_1 == 0 and num % check_no_2 == 0:
    print("num is multiple of both check_no_1 and check_no_2")