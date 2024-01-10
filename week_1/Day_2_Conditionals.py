# I. If Statements  

# 1. If Statements
# if (condition):
#     # Do something/ Do statements

manager_present = True # if the manager is present
manager_absent = False # if the manager is not present

if manager_absent:
    print("Notify John to return...")

# scenarion 2 
if (1>0):
    print("1 is greater than 0")

# if else statement
if manager_absent:
    print("Notify John to return...")
else:
    print("John is present")


# if elif else statement - where we have more than 2 conditions
# if (condition):
#     # Do something/ Do statements
# elif (condition):
#     # Do something/ Do statements
# else:
#     # Do something/ Do statements
    
# scenario 1
nationality = "Ugandan"

if nationality == "Kenyan" or nationality == "Ugandan":
    print("You are Kenyan")

elif nationality == "Ugandan":
    print("You are Ugandan")

elif nationality == "Tanzanian":
    print("You are Tanzanian")

else:
    print("You are not East African")

# Nested if statements - This is like forcing an and condition 
    
if nationality == "Kenyan":
    if manager_present:
        print("Notify John to return...")
        if (1>0):
            print("1 is greater than 0")
    else:
        print("John is present")
else:
    print("You are not Kenyan")
    
