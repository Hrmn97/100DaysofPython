#Introduction to Loops
'''

Sometimes a programmer wants to execute a group of statements a certain number of times.
 This can be done using loops. Based on this loops are further classified into following main types;

for loop
while loop
The for Loop
for loops can iterate over a sequence of iterable objects in python. 
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

'''

name = "Harman"
for i in name:
    print(i , end=", ")
    if( i == "a"):
        print("This is special")


colors = ["Red","Green","Blue","Yello"]
for color in colors:
    print(color) 
    

#range():
#What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?
#Here, we can use the range() function.

for k in range(5):
    print(k - 5)

for k in range(4,9):
    print(k)