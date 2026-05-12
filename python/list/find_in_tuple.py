# find element in tuple or not   
tup=(10,20,30,40,50)
x=int(input("enter a no.to find in list:"))
for i in tup:
     if x==i:
        print("found")
        break
else:
 print("not found")   
 
