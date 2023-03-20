# Recursion in python
# Recursion is the process of defining something in terms of itself.

# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. 
# These types of construct are termed as recursive functions.

def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return(num * factorial(num - 1))
    
num = 10
print(num)
print(factorial(num))

#FIBONACCI SERIES
def fib(num):
    if(num == 0 ):
        return(0)
    elif(num == 1):
        return(1)
    else:
        return(fib(num-1)+ fib(num-2))
    
print(fib(10))