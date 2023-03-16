# Python comments
# A comment is part of the coding file that the programmer does not want to execute, rather than programmer uses it to 
# explain a block of code or to avoid the execution of a specific part of code while testing.


'''
This also got commented to be used as a multiline comments
The lines here written are not taken as code and ignored 
'''




# Escape sequence character -> 
'''
To insert character that cannot be directly used in a string, we use an escape sequence character.
An escape sequence character is a backslash / followed by the character you want to insert
'''


print("Hey! I m a good boy \n and this is python repos") 

print ("Hey this is to \"test\"\n and it is working as per need")


#More about print statement
print ( "hey", 6, 7, sep="~", end = "\n")

print("Harman")

# 1. object(s): Any object and as many as you like will be converted to string before printed
# 2. sep = "separator" -> specify how to separate the object if there is more than one. Default is  ''
# 3. end = "end" -> Specify what to print at the end. Default is "\n" (line feed)
# 4. file: An object with a write method. Default is sys.stdout