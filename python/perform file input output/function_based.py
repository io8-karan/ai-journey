# # Create a login/signup system using file handling and functions.
# print("login/signup system")
# print("choose=1 for sign up")
# print("choose=2 for login ")
# print("choose=3 for exit")
# def signup():
#         print("Enter a detail for sign up")
#         username=input("Enter username=")
#         password=input("Enter your Password=")
#         f=open("D:\Karan\python\perform file input output\detail.txt","a")
#         f.write(username + "," +password +"\n")
#         f.close()
# def login():
#       print("Enter a detail for login")
#       username_login=input("Enter username=")
#       password_login=input("Enter your Password=")
#       f=open("D:\Karan\python\perform file input output\detail.txt","r+")
#       found=False
      
#       for  data in f:
#             data=data.strip()
#             stored_username,stored_password=data.split(",/")
#             if stored_username==username_login and stored_password==password_login:
#                   found=True
#       if found==True:
#         print("login successfully")  
#       else:
#            print("details not matched")
#       f.close()    
# while True:
#     choice=int(input("Enter a choice="))
#     if choice==1:
#        signup()
#     elif choice==2:
#          login()
#     elif choice==3:
#          print("|Exit")
#          break
#     else:
#          print("invalid option")




#  Notes saving  app
print("Notes Saving App")
def  show_menu():
 print("choose=1 for showing Menu")
 print("choice=2 fro add notes in flies")
 print("choice=3 for read and display notes")
 print("choice=4 for updating notes")
 print("choice=5 for deleting file data")
 print("choose=6 for exit")
def add():
 notes=input("Enter your Note=")
 f=open("D:\Karan\python\perform file input output\detail.txt","a")
 f.write(notes + "\n")
 f.close()
def read():
 f=open("D:\Karan\python\perform file input output\detail.txt","r")
 data=f.read()
 print(data)
 f.close()
def update():
 f=open("D:\Karan\python\perform file input output\detail.txt","r+")
 line_no=input("Enter A line no.=")
 for i in f:
   if line_no==i:
    updates_notes=input("Enter updating data=")
    f.write(updates_notes)
 data=f.read()
 print(data)
 f.close()
def delete():
 f=open("D:\Karan\python\perform file input output\detail.txt","r")
 delete_notes=input("Enter deleting data=")
 data=f.readlines()
 f.close()
 f=open("D:\Karan\python\perform file input output\detail.txt","w")
 for line in data:  
  if delete_notes==line.strip():
   continue
  f.write(line)
 f.close()

while True:
    choice=int(input("Enter a choice="))
    if choice==1:
       show_menu()
    elif choice==2:
         add()
    elif choice==3:
      read()
    elif choice==4:
      update()
    elif choice==5:
      delete()
    elif choice==6:
         print("|Exit")
         break
    else:
         print("invalid option")