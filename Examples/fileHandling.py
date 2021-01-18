import os

# Read data from the file
file = os.path.join(os.path.dirname(__file__), '..', 'data', 'file.txt')
obj = open(file, 'r')

#  Read all data from the file
print(obj.read())

#  Read one line from the file
# print(obj.readline())
# print(obj.readline())

#  Read only few characters from the file
# print(obj.read(10))

# Read all characters from file and display 1 by 1
# for i in obj.read():
#     print(i)

# Read all data from file line by line
# line = obj.readline()
# while line:
#     print(line)
#     line = obj.readline()

# Write data from the file & replace existing content in file
# wobj = open(file, 'w')
# wobj.write('This is a new line')
# wobj.close()

# Append data from the file
# wobj = open(file, 'a')
# wobj.write('\nThis is a new line')
# wobj.close()

# tell(): find out your current cursor position
# seek(): take your cursor position to a specific character
