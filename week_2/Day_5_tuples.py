# understanding tuples
# tuples are immutable 
# defining tuples 
my_tuple = ("Emmanuel", 8, "Mercy", "Judith", "Kibet", "Judith")
my_set = {"emanual", 7}

# accessing elements in a tuple
print(my_tuple[1])
print(my_set)
# my_tuple[6] = "Emmanuel2" # this will throw an error

# Unpacking tuples
tuple = ("mercy", "judith", "kibet", "judith")

name1, name2, name3, name4 = tuple

print(name1)