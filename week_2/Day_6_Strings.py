# Strings - These a python data type that stores a sequence of characters or text

string1 = "hey there, Welcome to Zindua Python Programming Class B."

# getting the length of a string 
print("My String1 has a size of : ", len(string1))

# accessing elements in a string
print("The first element in my string is : ", string1[-1])

# slicing a string
print("The first 5 elements in my string are : ", string1[0:5])

# concatenating strings
string2 = "This is the second string"
string3 = string1 + " " + string2
print("Concatenated strings : ", string3)
print("length of concatenated strings : ", len(string3))

# fstring - formatting strings
combined_string = f"{string1} {string2}"
print("Combined string : ", len(combined_string))

# string methods
# 1. capitalize() - capitalizes the first letter of a string
print("Capitalized string : ", string1.capitalize())

# 1. upper()
print("Upper case string : ", string1.upper())

# 2. lower()
print("Lower case string : ", string1.lower())

# 3. count() - counts the number of times a character appears in a string
print("Count of P in string1 : ", string1.lower().count("p"))

# 4. find() - finds the index of a character in a string
print("Index of P in string1 : ", string1.lower().find("."))

string4 = "Emmanuel"
# iterating through a list
index = 0
for char in string4:
    print(f"{index}: {char}")
    index = index+1

print("---------------------")
for index, char in enumerate(string4):
    print(f"{index}: {char}")

# Finding index for a character that appears more than once
for index, char in enumerate(string1.lower()):
    if char == "p":
        print(f"{index} : {char}")

# 5. split() - splits a string into a list
print("Split string : ", string1.split(" "))
