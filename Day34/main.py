# Dictionary Methods
# Dictionary uses several built-in methods for manipulation.They are listed below

# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary,
# else it creates a new key-value pair.

ep ={122: 45, 123: 89, 567: 69, 670:69}
ep2 ={222: 67, 566: 90}

# ep.update(ep2)
# print(ep)

# Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.

# clear():
# The clear() method removes all the items from the list.

ep.clear()
print(ep)

# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('age')
print(info)


# popitem():
# The popitem() method removes the last key-value pair from the dictionary.

info.popitem()
print(info)


# del:
# we can also use the del keyword to remove a dictionary item.

info2 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info2['age']
print(info2)