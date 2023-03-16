# Data types and Variables


#variable -> It is like a container that holds data. Creating a variable is like creating a placeholder in memory and assigning it to some value

a = 1
print(a)
b = "Harman"
print(b)


# Data types -> There are 4 variable of different data types
'''
data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error
'''

# use type function to check data type
c = 1
print(type(c))
d = "ABCD"
print(type(d))


# 1. Numeric data type: int, float, complex
#   -> int: 3, -8, 0
#   -> float: 7.349, -9.0, 0.00002388712

# 2. Text data: str
#   str -> "Hello world"

# 3. Boolean data:
#    Boolean data consist of values True or False

# 4. Sequenced data type: list, tuple
#   list:It is an ordered collection of data with elements separated by a comma and enclosed with in square brackets. List are mutable and can be modifies after creation
list1 = [8,2.3, [-4,5], ["apple","orange"]]
print(list1)

# tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within paranthesis. Tuples are immutable and can not be modified after createion
tuple1 = (("parrot","sparrow","more"), ("lion","tiger"))
print(tuple1)

# 5. Mapped data : dict
# dict : A dictionary is an ordered collection of data containing a key: value pair. The key:value pair are enclosed within curly brackets
dict1 = {"name": "Harman", "age": 25, "canVote": True}
print(dict1)