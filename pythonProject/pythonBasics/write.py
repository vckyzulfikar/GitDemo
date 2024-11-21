# Read the file and store all the lines in list
# Reverse the list
# Write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readline() #[a,b,cat,4,elephant]
    reversed(content) #[elephant, 4, cat, b, a]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)



























            