#Typecasting
'''The cnversion of one data type to other data type is known as typecasting in python or type converison'''
# Pyhton supports a wide variety of functions or methods: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() for type casting in python

# Two types of typecasting in python:
# 1. Explicit conversion
# 2. Implicit conversion

# Explicit typecasting:
'''The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement
is known as explicit type conversion'''

# It can be achieved with the help of python's built-in type conversion function such as int(), float(), hex(), oct(), str() etc
string = "15"
number =7
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The sum of both the numbers is :", sum)


# Implicit typecasting:
'''Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. 
Some of the data types have higher-order, and some have lower order. 
While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type.
 According to the level, one data type is converted into other by the Python interpreter itself (automatically). 
 This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.'''

c =1.9
d=8
print(c+d)