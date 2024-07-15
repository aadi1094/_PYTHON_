#SetMethods

#union and update.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
cities.update(cities2)
print(cities,cities2)

#Intersection and update:
s1={1,2,5,6}
s2={5,6,7,3}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1,s2)

#Symmetric_difference and update:
s1={1,2,5,6}
s2={5,6,7,3}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1,s2)

#difference
s1={1,2,5,6}
s2={5,6,7,3}
print(s1.difference(s2))
