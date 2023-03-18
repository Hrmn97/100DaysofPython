#Python while Loop
# As the name suggests, while loops execute statements while the condition is True. 
# As soon as the condition becomes False, the interpreter comes out of the while loop.

# i = 0
# while(i<5):
#     print(i)
#     i= i+1

# n=int(input("enter value less than 38 to run the loop"))
# while(n<=38):
#     n = int(input("Enter the new value: "))
#     print(n)


#Else with While Loop
# We can even use the else statement with the while loop. 
# Essentially what the else statement does is that as soon as the while loop condition becomes False,
# the interpreter comes out of the while loop and the else statement is executed.

# x=5
# while( x> 0):
#     print(x)
#     x = x - 1
# else:
#     print("it is 0")


# Else with While Loop
# We can even use the else statement with the while loop. 
# Essentially what the else statement does is that as soon as the while loop condition becomes False, 
# the interpreter comes out of the while loop and the else statement is executed.


number = int(input("Enter a positive number: "))
while True:
  
  print(number)
  if  number > 0:
    break
