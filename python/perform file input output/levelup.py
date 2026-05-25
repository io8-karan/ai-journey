# # Copy contents of one file into another file.
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# data=f.read()
# print(data)
# f.close()
# f2=open("D:\Karan\python\perform file input output\copy.txt","w+")
# f2.write(data)
# f2.seek(0)
# copy_data=f2.read()
# print(copy_data)
# f2.close()
# #Find longest word in a file check according to alphabetic  not length wise
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# data=f.read()
# word=data.split()
# largest=word[0]
# for i in word:
#     if i>largest:
#         largest=i
# print(largest)
# f.close()   

# #Find longest word in a file
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# data=f.read()
# word=data.split()
# largest=word[0]
# for i in word:
#     if len(i)>len(largest):
#         largest=i
# print(largest)
# f.close()   

# # Count vowels and consonants in a file.
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# vowel_count=0
# consonants_count=0
# for  char in f.read():
#    if len(char) == 1 and char.isalpha():
#     if char.lower() in 'aeiou':
#         vowel_count+=1
#     else:
#        consonants_count+=1
# print("total vowels=",vowel_count)
# print("total consonants count=",consonants_count)
# f.close()

# #Replace all spaces with - in a file.
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# data=f.read()
# new=data.replace(" ","-")
# print(new)
# f.close()

# #Convert file content into uppercase.
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# data=f.read()
# new=data.upper()
# print(new)
# f.close()

# # Remove duplicate lines from a file.
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# unique=[]
# duplicate=[]
# for lin in f:
#     lin=lin.strip()
#     if lin  not in unique:
#         unique.append(lin)
#     else:
#         duplicate.append(lin)
# print(unique)
# print(duplicate)
# f.close()


# #Print only even-numbered lines from a file.
# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# # line_no=1
# # for i in f:
# #     if line_no%2==0:
# #         print(i)
# #     line_no+=1
# data=f.readlines()
# for i in range(len(data)):
#     if (i+1)%2==0:
#         print(data[i])

#Reverse each line of a file.

# f=open("D:\Karan\python\perform file input output\demo.txt","r")
# for i in f.readlines():
#    reverse=i[::-1]
#    print(reverse.strip())
# f.close()

# Search a word in file and count its occurrences.
f=open("D:\Karan\python\perform file input output\demo.txt","r")
found=False
count=0
for i in f:
    if "Karan" in i:
        found=True
        count+=1
if found==True:
 print("found")
else:
 print("not found")

print("total occurance=",count)
f.close()