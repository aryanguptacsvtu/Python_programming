a= [1,3,55]      # Lists
b= [1,3,55]
print(a is b)    # Comparing exact location of object in memory.
print(a == b)    # Comparing value.
print("\n")

x = 8
y = 8
print(x is y)
print(x == y)
print("\n")

F = 'harry'
G = 'harry'
print(F is G)
print(F == G)
print("\n")

A = (1,2,3)      # Tuples
B = (1,2,3)
print(A is B)
print(A == B)
print("\n")

X = None
Y = None
print(X is Y)
print(X == Y)
print(X is None)
print("\n")

p = {'name':'aryan'}  # Dictionaries
q = {'name':'aryan'}
print(p is q)
print(p == q)
print("\n")

c = {10,88}      # Sets
d = {10,88}
print(c is d)
print(c == d)

# For Mutable objects like lists & dictionaries, 'is' & '==' can behave differently.