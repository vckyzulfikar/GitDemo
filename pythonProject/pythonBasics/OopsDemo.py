# Classes are user defined blueprint or prototype
# Sum, Multiplication, Addition, Constant
# Methods, Class Variables, Instance Variables, Constructior etc
# Object for your classes
# Self keyword is mandatory for calling variable names into method
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# New keyword is not required when create object

class Calculator:
    num = 100
    # Default constructor

    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2,3) # Syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5) # Syntax to create objects in python
obj1.getData()
print(obj1.Summation())