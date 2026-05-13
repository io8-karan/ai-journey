    # count digits 
num=int(input("Enter a number: "))
count=0
while num>0:
    num=num//10
    count+=1
print("count of digits is",count)
#wrong approach because when num big they run unnecessary and num will at the zero and if we want to use later they are empty not to use .

#instead of this we use len() method or store original no. to another no.
num1=input("Enter a number: ")
length=len(num1)
print(length)