# Function Arguments and return statement
# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments



# Default arguments:
# We can provide a default value while creating a function. 
# This way the function assumes a default value even if a value is not provided in the function call for that argument.

def averagem(a=9,b=1):
    print("The average is ", (a+b)/2)

averagem()


def name(fname,mname="harman",lname="Singh"):
    print("hello",fname,mname,lname)

name("chetan")


# Keyword Arguments
# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. 
# Hence, the the order in which the arguments are passed does not matter.

def names(fname, mname, lname):
    print("Hello,", fname, mname, lname)

names(mname = "Peter", lname = "Wesker", fname = "Jade")




#Required arguments
def average(a,b):
    print("The average is ", (a+b)/2)

average(4,6)


# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. 
# This can be done using variable-length arguments.

# There are two ways to achieve this:

# Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of tuple.

def main(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
        print("Average is :", sum / len(numbers))

main(5,6, 34)


# Keyword Arbitrary Arguments:
# While creating a function, pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

# return Statement
# The return statement is used to return the value of the expression back to the calling function.

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))