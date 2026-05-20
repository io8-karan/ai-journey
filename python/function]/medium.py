# # Create a function to find maximum of two numbers
# def check_max(a,b):
#     if a>b:
#         print(f"{a} is max")
#         return a
#     elif b>a:
#         print(f"{b} max")
#         return b
#     else:
#         print("both equal5")     
# print(check_max(5,8))

# # Create a function to count vowels in a string

# def count_vowel(str):
#      count=0
#      for ch in str:
#          if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#              count+=1
#              return count
# print(count_vowel("apple"))   
# # Create a function to find factorial of a number
# def fact(n):
#     factorial=1
#     for i in range(1,n+1):
#         factorial=factorial*i
#     return factorial
# print(fact(4))

# #Create a function to reverse a string
# def reverse(str):
#      return (str[::-1])
# print(reverse("karan"))

# #Create a function to reverse a number
# def reverse_num(num):
#     rev=0
#     while num>0:
#       number=num%10
#       rev=rev*10+number
#       num=num//10
#     return rev
# print(reverse_num(12345))

# #Create a function to count elements in list
# number=[1,2,3,4,5,6,7,8,9]
# def count(list):
#     return len(list)
# print(count(number))
 
#  #Create a function to count elements in list
# number=[1,2,3,4,5,6,7,8,9]
# def count(list):
#     count=0
#     for _ in list:
#      count+=1
#     return count
# print(count(number))    

# #Create a function to find sum of list elements
# number=[1,2,3,4,5,6,7,8,9]
# def sum(list):
#     sums=0
#     for i in list:
#         sums=sums+i
#     return sum
# print(sum(number))    

# # Create a function to remove duplicates from list
# number=[1,2,3,2,4,3,5,6,5,7,68,76,9,5,7845,5]
# digit=[1,2,3,4,5,6,7,.8,9,0,78,6,765,34,8,234,2,67,432,7,43,7]
# def remove(list):
#     after_removal=set(list)
#     return after_removal
# print(remove(number))
# print(remove(digit))

# #Create a function to find common elements between two lists using set and in this ordered are suffled
# number=[1,2,3,2,4,3,5,6,5,7,68,76,9,5,7845,5]
# digit=[1,2,3,4,5,6,7,.8,9,0,78,6,765,34,8,234,2,67,432,7,43,7]
# def common(list1,list2):
#     set1=set(list1)
#     set2=set(list2)
#     set3=set1.intersection(set2)
#     list3=list(set3)
#     return list3
# print(common(number,digit))

#Create a function to find common elements between two lists
number=[1,2,3,3,3,3]
digit=[1,2,3,4,5,6,7,.8,9]
def common(list1,list2):
    common_list=[]
    for i in list1:
        if i in list2:
            common_list.append(i)
    return common_list
print(common(number,digit))            

#Create a function that returns highest marks from dictionary
student={
    "marks1":60,
    "marks2":70,
    "marks3":80
}
def find_max(dict):
    max=0
    max_name=""
    for key,value in dict.items():
        if value>max:
            max_name=key
            max=value
            
    return max_name,max
print(find_max(student))    