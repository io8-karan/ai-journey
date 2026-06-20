
# Create a login/signup system using file handling and functions.
try:
 print("login/signup system")
 print("choose=1 for sign up")
 print("choose=2 for login ")
 print("choose=3 for exit")
except ValueError:
 
# sign up section    
 def signup():
      try: # try section 
        print("Enter a detail for sign up")
        username=input("Enter username=")
        password=input("Enter your Password=")
        f=open("d:/ai journey/python/perform file input output/detail.txt","r+")
        for data in f.readlines():
             new=data.strip()
             new=new.split(",")
             if username==new[0]:
              print("user already exist")
              break
        else:
              f.write(username + ',' + password + "\n")
              print("New user Successfully added")
             
#except section 

      except ValueError:
        print("Value Error")
      except IndexError:
        print("Index Error")
      except FileNotFoundError:
        print("File not found error")
      except Exception as e:
        print("Other error:", e) 
    
#login Section
           
def login():
    
    try: # try section 
      print("Enter a detail for login")
      username_login=input("Enter username=")
      password_login=input("Enter your Password=")
      found=False
      f=open("d:/ai journey/python/perform file input output/detail.txt","r")
      for data in f.readlines():
           new=data.strip()
           new=new.split(",")
           if username_login==new[0] and password_login==new[1]:
                found=True
                break
      if found:
           print("Login Successfully")
       
      else:
           print("Login Failed")
      f.close()
    
# except section

    except ValueError:
        print("Value Error")
    except IndexError:
        print("Index Error")
    except FileNotFoundError:
        print("File not found error")
    except Exception as e:
        print("Other error:", e) 
        
# choice section

while True:
    choice=int(input("Enter a choice="))
    if choice==1:
         signup()
    elif choice==2:
         login()
    elif choice==3:
         print("|Exit")
         break
    else:
         print("invalid option")
