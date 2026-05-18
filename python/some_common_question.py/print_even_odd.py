number=[]
for i in range(6):
    num=int(input("enter a no."))
    number.append(num)
print(number)    
for num in number:    
    if num%2==0:
     print("even no.",num)
    else:
      print("odd no.",num) 

