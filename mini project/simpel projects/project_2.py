sub1=int(input("ENter sub1 Marks:"))
sub2=int(input("ENter sub2 Marks:"))
sub3=int(input("ENter sub3 Marks:"))
sub4=int(input("ENter sub4 Marks:"))
sub5=int(input("ENter sub5 Marks:"))
print("Your sub1s MArks is:",sub1)
print("Your sub2 MArks is:",sub2)
print("Your sub3 MArks is:",sub3)
print("Your sub4 MArks is:",sub4)
print("Your sub5 MArks is:",sub5)
total=sub1+sub2+sub3+sub4+sub5
print("Your Total Marks is:",total)
per=total/5
print("Your Percentage is:",per)
if(per>=90 and per<=100):
    print("Your Grade is A+")
elif(per>=80 and per<90):
    print("Your Grade is A")
elif(per>=70 and per<80):
    print("Your Grade is B+")
elif(per>=60 and per<70):
    print("Your Grade is B")
elif(per>=50 and per<60):
    print("Your Grade is C")
elif(per>=40 and per<50):
    print("Your Grade is D")
elif(per>=33 and per<40):
    print("Your Grade is E")
elif(per>=0 and per<33):
    print("Your Grade is F")
else:
    print("Invalid Percentage")