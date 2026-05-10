list=[3, 7, 2, 9, 4, 6, 1]
sum=0
for i in list:
    sum=sum+i
print(sum)  

count=0
ana=str("banana")
for i in ana:
    if i=="a":
        count+=1
print(count)        

list=[10,20,30,40,50,60,70]
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)   

# Q10. You have a list of words — print only the words that are palindromes.

list=["madam", "hello", "racecar", "world", "level"]
list1=[]

for i in list:
    if i==i[::-1]:
     print(i)    
