file = open('test.txt')
# Read all the contents of file
# Read n number of character by passing parameter
# print(file.read(5))

# Read one single line at a time readLine()
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

#file.close()

# Print line by line using readLine method
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()

# values = [a, b, "cat", 4, "elephant"]
for line in file.readline():
    print(line)

file.close()