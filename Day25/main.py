# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. 
# Then perform operation on that list and convert it back to tuple.

countries = ("spain","india","dubai","japan")


print(countries)
temp = list(countries)
temp.append("Pakistan")
countries = tuple(temp)

print(countries)

# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

# However, we can directly concatenate two tuples without converting them to list.

countries2 = ("Bangladesh","aus","new","Pakistan")

all = countries+countries2
print(all)


print(all.index("Pakistan", 3, 8))
print(all.count("Pakistan"))