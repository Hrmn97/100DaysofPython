# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword.

a=int(input("Enter any value between 5 and 9 : "))

if(a<5 or a>9):
    raise "Value must be between 5 and 9"

# In the previous tutorial, we learned about different built-
# in exceptions in Python and why it is important to handle exceptions.
# However, sometimes we may need to create our own custom exceptions that serve our purpose.

