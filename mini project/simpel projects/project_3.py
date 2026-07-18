# Product Management System
# Features you can add:
store={} 
print("Add Product choose==1")
print("all product choose==2")
print("search as product choose==3")
print("delete as product choose==4")
print("Update Price choose==5")
print("total count of product choose==6")
print("expensive product choose==7")
print("exit choose==8")
while True:
    choice=int(input("Enter Your choice:")) 
    if choice==1:
        print("Add Product")
        num=int(input("Enter how many product you want to add:"))
        for i in range(num):
         product=(input("enter a product name:"))
         price=int(input("enter the price of product:"))
         store[product]=price
        print(store)
    elif choice==2:
       print("all product")
       for product in store.keys():
          print(product)
    elif choice==3:
       print("search as product")
       search_product=str(input("enter a search product"))
       for product,price,in store.items():
          if search_product==product:
             print("found the product")
             print(product,"=",price)     
    elif choice==4:
        print("delete as product")
        delete_product=str(input("enter a delete product:"))
        if delete_product in store:
           del store[delete_product]
           print("product delete")
        else:
           print("not found in it")
        print(store)   
    elif choice==5:
        print("Update Price")
        numb=int(input("enter how many product you want to updates"))
        for product in range(numb):
         update_product=str(input("enter a product name you want to update their prize:"))
         prize_updated=int(input("enter updated product prize:"))
         if update_product in store:
           store.update({update_product:prize_updated})
         else:
            print("not found in dictionary")
         print(store)   
    elif choice==6:
        print("total count of product")
        print("count of product:",len(store)) 
    elif choice==7:
       print("expensive product")
       max=0
       max_name=""
       for product,value in store.items():
          if value>max:
             max=value
             max_name=product
       print(max_name,"=",value)   
    elif choice==8:
       print("thanku for visiting")
       print("exit")
       break
