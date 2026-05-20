# # #Create a function for calculator (+, -, *, /)
# # def calculator(a,b,operator):
# #     if operator=="+":
# #         return a+b
# #     elif operator=="-":
# #         return a-b
# #     elif operator=="*":
# #         return a*b
# #     elif operator=="/":
# #         if b==0:
# #             print("not divisible")
# #         else:
# #             return a/b
# #     else:
# #         print("invalid input")

# # print(calculator(4,5,"*"))        

# # #Create a function to generate Fibonacci series
# # def fibonacci(num):
# #     a=0 
# #     b=1
# #     for i in range(num):
# #      print(a,end=" ")
# #      c=a+b
# #      a=b
# #      b=c 
# # fibonacci(8)
   
# #    #Create a function to check palindrome string

# # def palindrome(str):
# #    str_copy=str
# #    copy=str_copy[::-1]
# #    if str==copy:
# #       return "palindrome"
# #    else:
# #       return "not"
# # print(palindrome("racecar"))

# # #Create a function to count frequency of characters in string
# def frequency(str):
#     dict={}
#     for ch in str:
#         if ch in dict:
            
#             dict[ch]+=1

#         else:
#             dict[ch]=1
#     return dict        

# print(frequency("apple"))

#Create a function to sort list without using sort()

# list1=[10,5,67,3,54,87,9,43,56]
# def sort(list):
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#     return list
# print(sort(list1))
    
# #Create a function to find GCD of two numbers

# def find_gcd(a,b):
#     gcd=1
#     for i in range(1,a+1):
#      if a%i==0 and b%i==0:
#         gcd=i
#     return gcd
# print(find_gcd(32,48))

# #Create a function to merge two dictionaries 
# student={
#    "name":"karan",
#    "roll_no":230280072,
#    "class":"Btech Cse"
#    }
# pending_detail={
#    "semester":"6th",
#    "cgpa":79
# }
# def merge(dict1,dict2):
#    dict1.update(dict2)
#    return dict1
# # or
# #students={
# #  **dict1,
# #   **dict2
# #}

# print(merge(student,pending_detail))


# #Create a function to find duplicate elements from list
# list1=[1,2,3,4,5,6,7,89,7,5,6,4,3,3,44,655,354,23,2,2]
# def find(list):
#    original=[]
#    duplicate=[]
#    for i in range(len(list)):
#       if i in original: 
#          duplicate.append(i)
#       else:
#          original.append(i)
#    return duplicate     
# print(find(list1))

# #Create a function to separate even and odd numbers from list
# list1=[1,2,3,4,5,6,7,89,7,5,6,4,3,3,44,655,354,23,2,2]
# def find(list):
#    odd=[]
#    even=[]
#    for i in list:
#       if i%2==0: 
#          even.append(i)
#       else:
#          odd.append(i)
      
#    return even,odd 
# print(*find(list1), sep="\n")

 #Create a function to find second largest element in list
list1=[1,2,3,4,5,6,7,89,7,5,6,4,3,3,44,655,354,23]
def second_largest(lst):
    sets=set(lst)
    lst1=list(sets)
    for i in range(len(lst1)):
        for j in range(i+1,len(lst1)):
         if lst1[j]>lst1[i]:
            lst1[i],lst1[j]=lst1[j],lst1[i]
    

    return lst1,lst1[1]
print(*second_largest(list1),sep="\n")        

