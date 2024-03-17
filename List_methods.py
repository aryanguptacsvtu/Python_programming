l=[12,1,34,4,21,54,1,65]
print(l)

print(l.index(1))
print(l.count(1))

l.insert(1,899)
print(l)

l.append(70)
print(l)

l.sort()                 # Sorts in Ascending Order
print(l)
l.sort(reverse=True)     # Sorts in Descending Order
print(l)

l.reverse()
print(l)

m=l.copy()
print(m)

x=[900,1000]
l.extend(x)
print(l)         

z=[100,200]
k=l+z          # Concatenating two strings
print(k)


