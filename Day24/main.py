#Tuples


# Python Tuples
# Tuples are ordered collection of data items. They store multiple items in a single variable
# . Tuple items are separated by commas and enclosed within round brackets (). 
# Tuples are unchangeable meaning we can not alter them after creation.

tuple = (1,2,3,4,5,6)
tup = ("red","blue","green")

print(type(tuple),tup)
print(tup)


# Tuple Indexes
# Each item/element in a tuple has its own unique index.
# This index can be used to access any particular item from the tuple. 
# The first item has index [0], second item has index [1], third item has index [2] and so on.

print(tup[0])
print(tup[1])


print(tup[-2])


# III. Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword.

if "yellow" in tup:
    print("yes it is")
else:
    print('no')

#range of index

tup2 = tup[1:4]
print(tup2)