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
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
   
#  data=file.read()
#  if "java" in data:
#   with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","w")as file:
#    data1=data.replace("java","Java")
#    file.write(data1)
#    print(data1)
#   print("replaced")
#  else:
#   print("word not found")
   
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#     leng=[]
#     for count,data in enumerate(file):
        
#         length=len(data)
#         print(f"Line {count+1} Length:",length)
#         leng.append(length)
    
#     maximum=max(leng)
#     for count,data in enumerate(leng):
#         if maximum == data:
#             print(f"line no.{count+1} is longest line")
#         else:
#             pass

# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#     line=file.readlines()
#     longest=max(line,key=len)
#     print("Longest line=",longest)
#     print("Line No.",line.index(longest)+1)

# #  14. Remove Blank Lines
# # Create another file without blank lines.
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file:
#    with open(r"C:\Karan\ai journey\python\perform file input output\notes2.txt","w")as file1:
#     for line in file:
#      if line.strip()!="":
#        file1.write(line)
            
#      else:
#             pass

# # merging files
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt","r")as file,open(r"C:\Karan\ai journey\python\perform file input output\notes2.txt","r")as file1:
#    data1=file.read()
#    data2=file1.read() 
# with open(r"C:\Karan\ai journey\python\perform file input output\merge.txt","w")as f:
#    f.write(data1)
#    f.write("\n")
#    f.write(data2)



# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt", "r") as f1, open("merged.txt", "w") as out:
#     s.copyfileobj(f1, out)

# with open(r"C:\Karan\ai journey\python\perform file input output\notes2.txt", "r") as f2, open("merged.txt", "a") as out:
#     s.copyfileobj(f2, out)
# with open(r"C:\Karan\ai journey\python\perform file input output\merged.txt", "w") as f2:
#     for filename in ["C:\\Karan\\ai journey\\python\\perform file input output\\notes.txt","C:\\Karan\\ai journey\\python\\perform file input output\\notes2.txt"]:
#         with open(filename) as file:
#             for line in file:
#                 f2.write(line)

# count uppercase and lower case

# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt", "r") as file:
  
#       count_upper=0
#       count_lower=0
#       for data in file.read(): 
#                  if data.isupper() :
#                        count_upper+=1
#                  elif data.islower():
#                        count_lower+=1
#                  else:
#                         pass
#       print("Uppercae:",count_upper)
#       print("Lowercase:",count_lower)

# Vowel Count
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt", "r") as file:
  
#       count_vowel=0
#       for data in file.read(): 
#                  if data in 'aeiouAEIOU':
#                          count_vowel+=1
#                  else:
#                          pass
#       print("Vowel=",count_vowel)           

# #. Print Alternate Lines
# with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt", "r") as file:
#     counter = 0

#     for count, data in enumerate(file, start=1):
#         if count % 2 != 0:
#             if data.strip():
#                 print(f"Line {count}: {data}", end="")
#             else:
#                 counter += 1

#     print("\nEmpty alternate lines:", counter)

# remove dublicate line
with open(r"C:\Karan\ai journey\python\perform file input output\notes.txt", "r") as file:
    seen=set()
    list=[]
    for line in file:
        line=line.strip()
        if line not in seen:
         seen.add(line)
         list.append(line)
    
with open(r"C:\Karan\ai journey\python\perform file input output\notes4.txt", "w") as f:
          for data in list:
           f.write(data)
           f.write("\n")
