# reverse of string 

str1=str(input("Enter String:"))
print("User Entered String is:",str1)
print("Reverse of String is:")
print(str1[::-1])
print("\n")

# palindrome

rev=str1[::-1]
print("Reverse of String is:",rev)
if(str1==rev):
    print("String is palindrome")
else:
    print("String is not palindrome")

# first half od string

print("User Entered String is:",str1)
new= str1[0:3]
print("Sliced String is a:",new)

#  last half of string 

new2=str1[-3:]
print("Sliced String is:",new2)

#exclude first and last character

new3=str1[1:5]
print("Sliced String is:",new3)

#skip one character

new4=str1[0:5:2]
print("Sliced String is:",new4)

# before mid reverse and after same string 

mid=len(str1)//2
new5=str1[:mid][::-1]+str1[mid:]
print("Sliced String is:",new5)

#mid include with one after and befor e

new6=str1[mid-1:mid+2]
print("Sliced String is:",new6)

# Removed Suffix String

new7=str1.removesuffix("n")
print("Removed Suffix String is:",new7)

#swap fo first and last bit
    
new8=str1[-1]+str1[1:-1]+str1[0]
print("First and Last Character Interchanged String is:",new8)
new8=str1[-2:]+str1[2:-2]+str1[0:2]
print("First and Last Character Interchanged String is:",new8)

#Rotate string left by 2 means add first two letter at the end of string and remove from start

new9=str1[2:]+str1[:2]
print("Rotate String Left by 2 is:",new9)

#Rotate string right by 2 means add last two letter at the start of string and remove from end

new10=str1[-2:]+str1[:-2]
print("Rotate String Right by 2 is:",new10)


