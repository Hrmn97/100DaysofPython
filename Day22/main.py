# Python Lists
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.

lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)


# List Index
# Each item/element in a list has its own unique index. 
# This index can be used to access any particular item from the list. 
# The first item has index [0], second item has index [1], third item has index [2] and so on.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]

# Accessing list items
# We can access list items by using its index with the square bracket syntax []. 
# For example colors[0] will give "Red", colors[1] will give "Green" and so on...

print(colors[2])
print(colors[4])
print(colors[0])

# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. 
# The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

print(colors[-1])
print(colors[-3])
print(colors[-5])


# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


# Range of Index:
# You can print a range of list items by specifying where you want to start, 
# where do you want to end and if you want to skip elements in between the range.
# listName[start : end : jumpIndex]

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

print(animals[1:8:3])

print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes


# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, 
# and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

namesWith_i = [item for item in names if (len(item) > 4)]
print(namesWith_i)