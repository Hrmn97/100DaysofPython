# Python Sets
# Sets are unordered collection of data items. They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}. 
# Sets are unchangeable, meaning you cannot change items of the set once created. 
# Sets do not contain duplicate items.


s={2,4,2,6}
print(s)

info={"carla",19,False,5.9,19}
print(info)

# Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers.
# Also sets do not allow duplicate values.

# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set

x=set()
print(type(x))

for value in info:
    print(value)

