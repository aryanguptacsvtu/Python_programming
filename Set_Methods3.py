cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
print(cities)               # If we try to delete an item which is not present in set, "remove()" raises an error. 
cities.discard("Berlin")
print(cities)


a = {"Tokyo","Madrid","Berlin","Delhi"}
item = a.pop()
print(a)                   # We don't know which item gets popped.
print(item)


x = {"Tokyo","Madrid","Berlin","Delhi"}
del x                      # "del" is a Keyword, which deletes the set entirely.
# print(x) raises an error.


A = {"Tokyo","Madrid","Berlin","Delhi"}
A.clear()
print(A)                   # Clears all items in the set and prints an empty set.


info={"Boy",12,False,14.22,88}
if "Boy" in info:
    print("Yess!")
else:
    print("Noo!")

