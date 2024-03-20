cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities.update(cities2)
print(cities)                  # "update()" adds item into existing set from another set.


c1 = {"Tokyo","Madrid","Berlin","Delhi"}
c2 = {"Tokyo","Seoul","Kabul","Madrid"}
c3 = c1.intersection(c2)
print(c3)
c1.intersection_update(c2)
print(c1)                      # "intersection_update()" updates the existing set from another set.


a = {"Tokyo","Madrid","Berlin","Delhi"}
b = {"Tokyo","Seoul","Kabul","Madrid"}
c = a.symmetric_difference(b)
print(c)                        # Prints only items that are not similar to both sets.
a.symmetric_difference_update(b)
print(a)


x = {"Tokyo","Madrid","Berlin","Delhi"}
y = {"Seoul","Kabul","Madrid"}
print(x.difference(y))          # Return the difference of two or more sets as a new set.
x.difference_update(y)
print(x)

