# What are dictionaries?

# Buit in data structures in python that allows us to store data in key value pairs

# Syntax: {key: value}
my_dict = {
    "names": ["Emmanuel", "Mbugua", "MERCY", "JUDITH", "KIBET"],
    "age" : [23, [20, 5], 25, 26, 27],
    "course": ["Python", "Django", "Flask", "Javascript", "React"],
    "level": ["Intermediate", "Beginner", "Advanced", "Beginner", "Intermediate"],
    "Phone": ["+25471234567", "+25471234567", "+25471234567", "+25471234567", "+25471234567"]
}

# print(my_dict)

# Accessing values in a dictionary
# print(my_dict["age"])

# Adding a new key value pair to a dictionary
my_dict["email"] = "emanuel@gmail.com"

# print(my_dict)

# getting all the keys in a dictionary
# print(my_dict.keys())

# # getting all the values in a dictionary
# print(my_dict.values())

# updating values of a dictionary

my_dict["course"] = ["Python", "C#", "Java", "Javascript", "React", "Nodejs"]


# renaming keys to a dictionar??

# removing a key value pair from a dictionary
my_dict["course"] = my_dict.pop("course")

print(my_dict.keys())

# using the .get() method to access values in a dictionary
print(my_dict.get("age"))