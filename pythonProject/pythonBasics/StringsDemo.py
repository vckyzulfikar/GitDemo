str = "RahulSheetyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulSheety"

print(str[1]) #a

print(str[0:5]) # If you want substring in python

print(str+str1) # Concatenation

print(str3 in str) # Substring check

var = str.split(".") # Split "." from str
print(var)
print(var[0]) # Check array 0 from var = ['RahulSheetyAcademy', 'com']

str4 = " great "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())