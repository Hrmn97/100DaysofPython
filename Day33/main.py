# Python Dictionaries
# Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accessing Dictionary items:
# I. Accessing single values:
# Values in a dictionary can be accessed using keys. 
# We can access dictionary values by mentioning keys either in square brackets or by using get method.

print(info['name'])
print(info.get('eligible'))

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

print(info.values())

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.

print(info.keys())

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.

print(info.items())