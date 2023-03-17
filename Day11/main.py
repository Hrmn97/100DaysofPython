#What are strings?
'''
In python, anything that you enclose between single or double quotation marks is considered a string.
A string is essentially a sequence or array of textual data. 
Strings are used when working with Unicode characters.
'''

name ="Harman"
friend = 'Lovish'

print("Hello, " + name)

'''
Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. 
Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". 
We will definitely use single quotes for our convenience

'''
apple="He said, \"I want to eat an apple\"."
print(apple)

apple1 = 'He said, "I want an apple" '
print(apple1)


apple2='''He said,
Hi harman
hey i am good
"I want to eat an apple"'''

print(apple2)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Accessing Characters of a String
'''In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.'''

name1="Harman"
print(name1[0])
print(name1[3])


#Looping through the string

#We can loop through strings using a for loop like this:

str="Harman is a good boy"

for i in str:
    print(i)