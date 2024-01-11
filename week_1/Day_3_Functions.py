# What is a function in  Python? and why does it matter?

# A function is a block of code which only runs when it is called.
def my_function():
  print("Hello from a function")


# Calling a function
my_function()

# Lets create a function that adds two input variables
def summation(num_1, num_2):
    result = num_1 + num_2
    print(num_1) # This is a local variable
    return print("The result of your function is: ", result) # This is the output of the function


# summation(7, 4)
# print(result)

# Lets look at scope of Variables while working with functions....
#  1. Local Variables - These are variables that are declared inside a function
# 2. Global Variables - These are variables that are declared outside a function
value1 = 8
value2 = 4

summation(value1, value2)
print(result)