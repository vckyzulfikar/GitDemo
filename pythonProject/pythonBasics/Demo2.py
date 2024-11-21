values = [1, 2, "vicky", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0]) #1 since array is start from 0, 1, 2, ...

print(values[3]) #4
print(values[-1]) #5
print(values[1:3]) #[2, 'vicky']
values.insert(3, "shetty") #[1, 2, 'vicky', 'shetty', 4, 5]
print(values)
values.append("End") #[1, 2, 'vicky', 'shetty', 4, 5, 'End']
print(values)

values[2] = "VICKY" #Updating value

del values[0] #Deleting value

print(values) #[2, 'VICKY', 'shetty', 4, 5, 'End'] 1 (0 in array) is gone because deleting value

# Tuple - Same as LIST Data type but immutable
val = [1, 2, "rahul", 4.5] #need to used [ ] since it's array

print(val[1])

val[2] = "RAHUL"

print(val)

# Dictionary
dic = {"a": 2, 4:"bcd", "c": "Hello World"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "Rahul"
dict["lastname"] = "shetty"
dict["gender"] = "Male"

print(dict)

name = ['vicky','zulfikar']
print(name[1])