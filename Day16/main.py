#Match case

'''
Match Case Statements
To implement switch-case like characteristics very similar to if-else functionality, 
we use a match case in python. 
If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements.
If this is your first language, dont worry as I will tell you everything you need to know about 
match case statements in this video!

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. 
The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

The match keyword
One or more case clauses
Expression for each case
The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches,
 and a set of statements to be executed if the pattern matches.'''


x=int(input("Enter the value for x: "))
#x is variable to match

match x:
    #if x is 0
    case 0:
        print("x is zero")
    case 4:
        print('x % 2 == 0 and case is 4')
    case _ if x < 10:
        print("x is  < 10")
    case _:
        print(x)