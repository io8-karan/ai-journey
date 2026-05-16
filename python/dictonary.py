# Count frequency of each character in a string using dictionary
dict={}

str1=str(input("enter a string :"))
print(str1)
for  char in str1:
    if char in dict:
       dict[char]=dict[char]+1
    else:
      dict[char]=1
print(dict)        

# # Group words by their length using dictionary
# words=[]
# word_group={}
# num=int(input("enter how many words in list:"))
# for i in range(num):
#    words.append(input("enter a words in list:"))
# print(words)  
# for word in words:
#    length=len(word)
#    print(word,"=",length) 
#    if length in word_group:
#       word_group[length].append(word)
#    else:
#       word_group[length]=[word]    
# print(word_group)

# # Invert a dictionary — swap keys and values 
# temp=""
# students={
#     "name":"karan",
#     "age":"17",
#     "roll_no":"230280072"
#
# invert={}


# # by using temp variable 
# for key,value in students.items():
#        temp=key
#        key=value
#        value=temp
#        invert[key]=value
# print(invert)   


# #simply do 
# for key,value in students.items():
#     invert[value]=key
# print(invert)    
    