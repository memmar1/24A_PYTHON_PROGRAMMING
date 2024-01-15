"""
Exercise 1: Print the following pattern
Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
nums = []

round = 1

while round < 6:
    nums.append(round)
    print(nums)
    round = round +1