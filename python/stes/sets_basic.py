# create a set and print all element
sets={10,20,3,0,40,50,60,70,80,4}  
# add and remove element
sets.add(15)
sets.remove(4)
print(sets)
#search element in found in set or not
search=int(input("enter a searching element:"))
for i in sets:
    if search in sets:
        print("found")
        break
else:
    print("not found")

# total number in set
print(len(sets))    