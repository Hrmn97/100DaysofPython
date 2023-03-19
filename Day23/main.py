#LIST METHODS

l=[65,57,0,17,12,1,2,4,6,1]

print(l)
l.append(7)
print(l)


l.sort(reverse= True)
print(l)

l.reverse()
print(l)


print(l.index(1))

print(l.count(1))

m=l.copy()
m[0]=0
print(l)
print(m)

color = ["voilet","green","red"]

color.insert(1,"yellow")
print(color)

rainbow=["blue","orange"]
color.extend(rainbow)
print(color)