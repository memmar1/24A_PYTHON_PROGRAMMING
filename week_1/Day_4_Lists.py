import math

# lists - 
# defining a list
names = ["Mercy", "Judith", ["Emmanuel", "willy"], "kibet",  "_"]

# getting the size of  a list
print(len(names))

# accessing elements in a list
print(type(names[-3]))

# slicing a list
print(names[0:3])

# slicing a list
print(names[2][0])

# Assignment 2
names_2 = ["Mercy", "Judith", "Emmanuel", "willy", "kibet",  "_"]
"""
    How can we get 'Mercy' skip Judith and get Emmanuel, willy, kibet and _ in one line of code?
"""

list_1 = ["Mercy", "Judith"]
list_2 = ["Emmanuel", "willy", "kibet",  "_"]

combined = list_1 + list_2
print(combined)

# appending to a list
list_1.append("Judith")

list_1.append(2)
print(list_1)

# removing from a list
list_1.remove("Judith")
print(list_1)

list_1.pop(0)
print(list_1)

print("starting loop")
# Looping through a list
for name in names_2:
    print(name)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

nums_Squared = []

# looping through a list and squaring each element
for num in nums:
    num_sq = num * num
    nums_Squared.append(num_sq)

print(nums_Squared)

# list comprehension
nums_Squared_2 = [num * num for num in nums]
print(nums_Squared_2)

# lets just square even numbers in the list
nums_Squared_3 = []
for num in nums:
    if num % 2 == 0:
        num_sq_2 = num * num
        nums_Squared_3.append(num_sq_2)
    else: 
        nums_Squared_3.append(num)

print(nums_Squared_3)

# simplifying this using a list comprehension
nums_Squared_4 = [num * num if num % 2 == 0 else num for num in nums]
print(nums_Squared_4)