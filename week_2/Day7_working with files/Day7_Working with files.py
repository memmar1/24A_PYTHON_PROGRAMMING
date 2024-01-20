# opening a file

f = open("week_2\Day7_working with files\sample.txt", "r")

# print(f.read())

# print(f.readline())
# print(f.readline())
# secon

# print(first_line)

# for x in f:
#     print(x)

f.close()

# print(f.readline()) # This will through an error since the file has already been closed
# Writing files

f2 = open("week_2\Day7_working with files\sample2.txt", "r")

f2.write("Hi there this is zindua")
print(f2.readline())

f2.close()
f2_r = open("week_2\Day7_working with files\sample2.txt", "r")
print("line 26:", f2_r.readline())

# f2 = open("week_2\Day7_working with files\sample.txt", "a+")

# f2.write("Hi there this is zindua")
# print("line 31:", f2.readline())


