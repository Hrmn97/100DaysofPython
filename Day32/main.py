# Joining Sets
# Sets in python more or less work in the same way as sets in mathematics. 
# We can perform operations like union and intersection on the sets just like in mathematics.

# I. union() and update():
# The union() and update() methods prints all items that are present in the two sets. 
# The union() method returns a new set whereas update() method adds item into the existing set from another set.


s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))
s1.update(s2)
print(s1, s2)

# II. intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. 
# The intersection() method returns a new set whereas intersection_update() method updates into the existing
# set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that 
# are not similar to both the sets. The symmetric_difference() method returns a new set whereas 
# symmetric_difference_update() method updates into the existing set from another set.


cities5 = cities.symmetric_difference(cities2)
print(cities5)

cities.symmetric_difference_update(cities2)
print(cities)



# IV. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set
# and not in both the sets. The difference() method returns a new set whereas difference_update() method updates 
# into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities7 = cities.difference(cities2)
print(cities7)


# Set Methods
# There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. 
# This method returns False if items are present, else it returns True.


print(cities.isdisjoint(cities2))

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set.
# It returns True if all the items are present, else it returns False.

print(cities.issuperset(cities2))
cities8 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities8))


# # issubset():
# The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items are present, else it returns False.

cities12 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities21 = {"Delhi", "Madrid"}
print(cities21.issubset(cities12))


# add()
# If you want to add a single item to the set use the add() method.

cities.add("Helsinki")
print(cities)

# update()
# If you want to add more than one item, simply create another set or any 
# other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

cities.update(cities2)
print(cities)

# remove()/discard()
# We can use remove() and discard() methods to remove items form list.

cities.remove("Tokyo")
print(cities)

# pop()
# This method removes the last item of the set but the catch is that we don’t 
# know which item gets popped as sets are unordered. However, you can access the popped item
# if you assign the pop() method to a variable.

item = cities.pop()
print(cities)
print(item)


# del
# del is not a method, rather it is a keyword which deletes the set entirely.
cities66 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities66
# print(cities66)

# clear():
# This method clears all items in the set and prints an empty set.


cities66.clear()
print(cities66)


# Check if item exists
# You can also check if an item exists in the set or not.

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")