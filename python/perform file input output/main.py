import os 
import shutil as s
# print("Current working directory:", os.getcwd())
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","w")as file:
#     file.write("Hello Python\nWelcome to fle HAndling\n")

# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","a")as file:
    
#     file.write("Learning NeverStops\n")
    
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#     for count,line in enumerate(file,start=0):
#        print(len(f"Line {count}"))

 # character counting 

# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#   counter=0
#   for line in file:
#     print(len((line.strip())))
#     counter+=len((line.strip()))
#   print("Total character=",counter)  
            
# #    word counting
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#     counter=0
#     for line in file:
#         print(len(line.split(" ")))
#         counter+=len(line.split(" "))
#     print("Total words=",counter)

# # counting lines
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#     counter=0
#     for line in file:
#         counter+=1
#     print("Total lines=",counter)

#copying file
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#  s.copy(r"C:\Karan\ai journey\python\perform file input output\notes.txt",r"C:\Karan\ai journey\python\perform file input output\notes1.txt")
 
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#   with open(r"C:\Karan\ai journey\python\perform file input output\notes2.txt","w")as file1:
#    for line in file:
#     file1.write(line)


#prine line number
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#     for count ,data in enumerate(file,start=1):
#         print(f"Line {count} : {data.strip()}")

# # reverse the content
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#    for line in file.readlines()[::-1]:
#     print(line.strip())  

# #found word
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#    found="Python"
#    data=file.read()
#    if found in data.strip():
#       print("found")
#    else:
#       print("Not")
#    print(data)

# Replace Word
with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r+")as file:
   found="Python"

   for data in file:
    if found in data.strip():
      print("found")
      data=data.replace("Python","Java")
      file.write(data)
    else:
      print("Not")

   
