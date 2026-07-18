  '''# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode'''


import random as r
letters="abcdefghijklmnopqrstuvwxyz"
choice=int(input("Enter 1 for encoding and 2 for decoding="))

# encoding section 

if choice == 1:
 
 letter=input("Enter a letter=")
 words=letter.split()
 final_encode=[]
 for word in words:
  if len(word)< 3:
   reverse=word[::-1]
   final_encode.append(reverse)

  elif len(word) >= 3:
   new_word=word[1:]
   new_word1=new_word+word[0]

   random_start_word=""
   for i in range(3):
     random_start_word +=r.choice(letters)
   random_end_word=""
   for i in range(3):
     random_end_word +=r.choice(letters)
   wordss=random_start_word + new_word1 + random_end_word
   final_encode.append(wordss)
 result=" ".join(final_encode)
 print("Encoded word is=",result)

# decoding section 

elif choice==2:    
  final_decode=[]
  letter=input("Enter a word=")
  words=letter.split()
  for word in words:
   if len(word)< 3:
       reverse=word[::-1]
       final_decode.append(reverse)
   
   elif len(word) >= 3:
       remove_start=word[3:]
       remove_end=remove_start[0:len(remove_start)-3]
       remove_last=remove_end[-1:]
       without_last_word=remove_end[0:len(remove_end)-1]
       wordss=remove_last + without_last_word
       final_decode.append(wordss)
  result=" ".join(final_decode)
  print("Decoded word is=",result)
else:
 print("invalid input")