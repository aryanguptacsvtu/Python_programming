cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
print(cities.isdisjoint(cities2))         # Returns "False" if items are present.


a = {"Tokyo","Madrid","Berlin","Delhi"}
b = {"Tokyo","Seoul","Kabul","Madrid"} 
print(a.issuperset(b))                   # Returns "True" if all the items are present.
c = {"Seoul","Kabul","Madrid"}
print(b.issuperset(c))


x = {"Tokyo","Madrid","Berlin","Delhi"}
y = {"Delhi","Madrid"}
print(y.issubset(x))                     # Returns "True" if all the items are present.            


A = {"Tokyo","Madrid","Berlin","Delhi"}
A.add("Raipur")
print(A)                                # To add a single item to the set use "add()"

X = {"Tokyo","Madrid","Berlin","Delhi"}
Y = {"Bombay","Patna","Bhilai"}
X.update(Y)                             # To add more than one item use "update()"
print(X)




