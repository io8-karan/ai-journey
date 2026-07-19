#Create a file and write your name into it.
#Read and print all contents of a file.

f=open("D:\Karan\python\perform file input output\demo.txt","w+")
f.write("My name is Karan.\nI am 20 year old")
data=f.read()
print(data)
f.close()

#Count total characters in a file.

f=open("D:\Karan\python\perform file input output\demo.txt","r")
count=0
for i in f.read():
     count+=1
print("Total no. of character=",count)

#Count total words in a file.

f.seek(0)
data=f.read()
words=data.split()
print("Total no. of words=",len(words))

#Count total lines in a file.

f.seek(0)
data=f.readlines()
print("Total no. of lines=",len(data))
f.close()

# Append your city name into an existing file.

f=open("D:\Karan\python\perform file input output\demo.txt","a+")
f.write("\ni am live in bathinda ")
f.seek(0)
data=f.read()
print(data)
f.close()
#Read first 10 characters from a file.

f=open("D:\Karan\python\perform file input output\demo.txt","r")
data=f.read(10)
print(data)
f.close()

#Read a file line by line using loop.

f=open("D:\Karan\python\perform file input output\demo.txt","r")
for i in f:
    print(i)
f.close()
    