# # Take numbers from user and store only unique values
# sets=set()
# number=int(input("enter how many elements in set: "))
# for num in range(number):
#     element=int(input("enter element:"))
#     sets.add(element)
# print(sets)
# # Remove duplicate elements from a list using set
# list=[10,20,.30,40,50,60,70,80,90,10,2,3,4,0,50,24,0,54,0,8,406,0]
# sets=set(list)
# print(sets)
# # Find common elements between two sets
# set1={10,20,3,89,7,6,5,445}
# set2={1,2,3,23,34,35,456,45}
# common_set=set1.intersection(set2)
# print(common_set)

# # Find union between two sets
# set1={10,20,3,89,7,6,5,445}
# set2={1,2,3,23,34,35,456,45}
# union_set=set1.union(set2)
# print(union_set)

 # find diff between sets 
# set1={10,20,3,89,7,6,5,445}
# set2={1,2,3,23,34,35,456,45}
# diff_set=set2-set1
# print(diff_set)

#Check whether two sets are equal or not
# set1=set()
# number=int(input("enter how many elements in set: "))
# for num in range(number):
#     element=int(input("enter element:"))
#     set1.add(element)
# print(set1)
# set2=set()
# number=int(input("enter how many elements in set: "))
# for num in range(number):
#     element=int(input("enter element:"))
#     set2.add(element)
# print(set2)
# if set1==set2:
#     print("equal set")
# else:
#     print("not equal")

# symmetric diffrence (a-b)u(b-a)
# set1={10,20,3,89,7,6,5,445}
# set2={1,2,3,23,34,35,456,45}
# diff_set1=set1-set2
# print(diff_set1)
# diff_set2=set2-set1
# print(diff_set2)
# symmetric_set=diff_set1.union(diff_set2)
# print(symmetric_set)

# #inbuilt method
# print("using built-in")
# symmetric=set1^set2
# print(symmetric)
# sy=set1.symmetric_difference(set2)
# print(sy)

# Find duplicate elements from a list using set logic
# count vowel in string using set
# sets=set()
# stringg="education"
# for ch in stringg.lower():
#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#       sets.add(ch)
# print(len(sets))      

# #other way
# str1=str(input("enter a string:"))
# count_vowel=set()
# normal_set=set()
# vowels={"a","i","o","u","e"}
# for character in str1:
#    if character in vowels:
#       count_vowel.add(character)
#    else:
#       normal_set.add(character)
# print(count_vowel)
# print("count of vowel=",len(count_vowel))
# print("collection of not a vowel=",normal_set)
#Find duplicate elements from a list using set logic

list1=[1,2,3,4,5,65,423,734,734,83,84,87,34,634,6,336,3]
duplicate_set=set()
non_duplicate_set=set()
for element in list1:
    if element in non_duplicate_set:
        duplicate_set.add(element)
    else:
      non_duplicate_set.add(element)  
print("duplicate=",duplicate_set)       
print("non-duplicate=",non_duplicate_set)