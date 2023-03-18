#FUNCTIONS

# Python Functions
# A function is a block of code that performs a specific task whenever it is called.
#  In bigger programs, where we have large amounts of code, 
# it is advisable to create or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# Built-in functions
# User-defined functions
# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.



def calculateGmean (a,b):
    mean = (a*b)/(a+b)
    print(mean)


def greater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    else:
        print(b,"is greater than", a)
a=8
b=9
c=8
d=7
calculateGmean(a,b)
greater(a,b)
calculateGmean(c,d)
greater(c,d)