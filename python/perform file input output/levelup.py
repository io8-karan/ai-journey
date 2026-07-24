import os
import shutil as s
print(os.getcwd())



os.chdir(r"C:\Karan\ai journey\python\perform file input output")
# file=["notes.txt","merge.txt","notes2.txt","notes4.txt"]
# for filename in file:
#     found="Python"
#     with open(filename,"r")as f:
#         for data in f:
#          if found in data:
#             print(f"found in {filename}")
#             break
#          else:
#             pass

# rename the file name 
# print(os.getcwdb())
# i=1
# for file in os.listdir("."):
#     if file.endswith(".txt"):
#         os.rename(file,f"file{i}.txt")
#         i+=1
# print(file)

# # find longest file and shortest file method 1
# maximum_size=0
# minimum_size = float("inf")
# for file in os.listdir("."):
#    size=os.path.getsize(file)
#    print(f"file Name :{file}={size}")
#    if size>maximum_size:
#       maximum_size=size
#       largest_file=file
#    elif size < minimum_size:
#       minimum_size=size
#       smallest_file=file
# print(f"Longest File is {largest_file} with {maximum_size} bytes")
# print(f"smalllest File is {smallest_file} with {minimum_size} bytes")

# #method 2
# # find longest file
# maximum_size=0
# for file in os.listdir("."):
#    if os.path.isfile(file):
#      size=os.path.getsize(file)
#      break
# minimum_size=size

# for file in os.listdir("."):
#    size=os.path.getsize(file)
#    print(f"file Name :{file}={size}")
#    if size>=maximum_size:
#       maximum_size=size
#       largest_file=file
#    elif size <= minimum_size:
#       minimum_size=size
#       smallest_file=file
# print(f"Longest File is {largest_file} with {maximum_size} bytes")
# print(f"smalllest File is {smallest_file} with {minimum_size} bytes")



with open("file1.txt","r")as file:
 for data in file:
    i=0 
    with open(f"part{i}.txt","a")as file1:
            data1=file1.write(data)     
                       
                            

              