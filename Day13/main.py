#String methods
# Python provides a set of built-in methods that we can use to alter and modify the strings.

#uppercase and lowercase
a = 'hrRmn'

print(len(a))

print(a.upper())      #strings are immutable that means it will not change the original string but it will save value to new one
print(a.lower())


#Stripping of character
b="hrmn!!!!!!!!!!!!!!!!!"

print(b.rstrip("!"))   # rstrip() is used to strip off the trailing character that is set in it's parameters

#Replacing of character
c="Harman is good name of Harman"
print(c.replace("Harman", "Johm"))  #replace() : The replace() method replaces all occurences of a string with another string. Example:

#split() : The split() method splits the given string at the specified instance and returns the separated strings as list items.
d = "Silver spoon"

print(d.split(" "))

#capitalize() : The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. 
# The string has no effect if the first character is already uppercase.

e ="hrmn is a good boy"
print(e.capitalize())

#center() : The center() method aligns the string to the center as per the parameters given by the user.

f = "Welcome to the Console!!!"
print(f.center(50))

print(f.center(50, "-"))

#count() :The count() method returns the number of times the given value has occurred within the given string.

g="Welcome to the console also in the console we need console of the console"
print(g.count("console"))


#endswith() :The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

h="Welcome to the Console !!!"
print(h.endswith("to", 4, 10))


#find() : The find() method searches for the first occurrence of the given value and returns the index where it is present.
#  If given value is absent from the string then return -1.

i= "He's name is Dan. He is an honest man."
print(i.find("is"))

j = "He's name is Dan. He is an honest man."
print(j.find("Daniel"))

#index() :The index() method searches for the first occurrence of the given value and returns the index where it is present. 
#If given value is absent from the string then raise an exception.

k = "He's name is Dan. Dan is an honest man."
print(k.index("Dan"))

#isalnum() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
#  If any other characters or punctuations are present, then it returns False.

l ="WelcomeToTheConsole"
print(l.isalnum())

#isalpha() : The isalnum() method returns True only if the entire string only consists of A-Z, a-z. 
# If any other characters or punctuations or numbers(0-9) are present, then it returns False.

m = 'Welcome'
print(m.isalpha())

#islower() : The islower() method returns True if all the characters in the string are lower case, else it returns False.4

n = "hello world"
print(n.islower())

# isupper() : The isupper() method returns True if all the characters in the string are upper case, else it returns False.

o ="WORL IS HEALTHY"
print(o.isupper())

#startswith() : The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
p="Python is a Interpreted Language" 
print(p.startswith("P"))

#swapcase() : The swapcase() method changes the character casing of the string. 
# Upper case are converted to lower case and lower case to upper case.

q ="Python is a Interpreted Language"
print(q.swapcase())

#title() : The title() method capitalizes each letter of the word within the string.
r="He's name is Dan. Dan is an honest man."
print(r.title())