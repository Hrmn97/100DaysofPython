#IF ELSE
'''if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:

if
if-else
if-else-elif
nested if-else-elif.
An if……else statement evaluates like this:
if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block.'''

applePrice=210
budget=200
if (applePrice < budget):
    print("We can buy it")
else:
    print("Out of budget")


'''elif Statements
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

Working of an elif statement
Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
.
.
.
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.
'''

a=int(input("enter your age: "))

print("Your age is: ",a)

if (a<18):
    print("You cannot drive")
elif (a==18):
    print("wait for one day")
elif (a>18):
    print("go ride a bike")
else:
    print("Invalid age")


#Nested if statements We can use if, if-else, elif statements inside other if statements as well.
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")