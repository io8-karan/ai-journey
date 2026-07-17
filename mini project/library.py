print( "="*50)
print("LIBRARY MANAGEMENT SYSTEM")
print( "="*50)
class library:
   
    def __init__(self):
       self.storage =[]
       self.no_of_books=0
    def add(self):    
             book=input("Enter a book name You want to add")
             self.storage.append(book)
             self.no_of_books +=1
              
    def show(self):
       return self.storage
    def show_no_books(self):  
       return self.no_of_books
       
lib1=library()
lib2=library()
while True:
    choose=int(input("Enter a  choice which library you want to call1 1 for library 1 and so on="))
    if choose==1:
        while True:
         choices=int(input("Enter your choice 1 for add 2 for  show and 3 for show number fo book and 4 for exit="))
         if choices ==1:
          lib1.add()
         elif choices ==2:
          lib1.show()
         elif choices == 3:
          lib1.show_no_books()
         else:
          print("exit")
          break
    elif choose ==2:
        while True:
         choices=int(input("Enter your choice 1 for add 2 for  show and 3 for show number fo book and 4 for exit="))
         if choices ==1:
          lib2.add()
         elif choices ==2:
          lib2.show()
         elif choices == 3:
          lib2.show_no_books()
         else:
          print("exit")
          break
    elif choose ==3:
        while True:
         choices=int(input("Enter your choice 1  for  show and 2 for show number fo book in both  libraries and 4 for exit="))
         if choices ==1:
          print("Books in library 1=",lib1.show())
          print("Books in library 2",lib2.show())
         elif choices == 2:
          print("Books in library 1=",lib1.show_no_books())
          print("Books in library 2",lib2.show_no_books())
         else:
          print("exit")
          break
    elif choose == 4:
      print("ENd of Program")
      break
    else:
     print("Invalid Input ")
     break