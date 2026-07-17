# contact management system 
contacts=[]
new_contact=[]
while True:
    print("CONTACT MENU")
    print("choice == 1 → Add")
    print("choice == 2 → Show")
    print("choice == 3 → Search")
    print("choice == 4 → Delete")
    print("choice == 5 → Count")
    print("choice == 6 → Update")
    print("choice == 7 → Exit")
    choice=int(input("Enter a choice="))
    if choice==1:
        print("Add Contact Detail")
        num=int(input("enter how many no. wants to add="))
        for i in range(num):
            name=str(input("Enter a Name="))
            number=(input("Enter a number="))
            tup=(name,number)
            contacts.append(tup)
        
    elif choice==2:
        print("show contact")
        for i in contacts:
            print("name=", i[0], "number=", i[1])
    elif choice==3:
        print("search contact")
        named=str(input("Enter a name form we want to serach a no.="))
        found=False
        for i in contacts:
            if i[0]==named:
                 print("name=", i[0], "number=", i[1])
                 found=True
                 break
        if found==False:
         print("not found")
    elif choice==4:
        print("delete contact")
        named=str(input("Enter a name form we want to delete a no.="))
        found=False
        for i in contacts:
            if i[0]==named:
                found=True
                contacts.remove(i)
                break
        if found==False:
         print("not found")
    elif choice==5:
        print("count contact")
        print("total count=",len(contacts))
    elif choice==6:
        print("update contact")
        named=str(input("Enter a name from we want to update a no.="))
        found=False
        for i in contacts:
         if i[0]==named:
            new_contact=input("enter a new no.=")
            index=contacts.index(i)        
            contacts[index]=(named,new_contact) 
            print("Contact updated")
            found=True
            break
        if found==False:
         print("not found")
    elif choice==7:
        print("exit")
        break
    else:
     print("invalid input")