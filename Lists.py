marks = [3,5,6,"Harry",True,12,54,32,43,65]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3])          # Negative index
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if "6" in marks:
    print("Yes")
else:
    print("No")

if 6 in marks:
    print("Yess")
else:
    print("Noo")

if "Ha" in "Harry":
    print("Yes!!")
else:
    print("No!!")

print(marks[:])             # Automatically starts with 0 index and prints till end.
print(marks[1:])
print(marks[1:-1])
print(marks[1:8])
print(marks[1:8:2])         # listName[start:end:jump]

animals=["cat","dog","bat","horse","mouse","lion","cow","goat","tiger"]
print(animals[::2])               # Printing alternate elements
print(animals[-8:-1:2])    


list=[i*i for i in range(10)]     # LIST COMPREHENSION
print(list)
list=[i*i for i in range(10) if i%2==0]
print(list)

names=["Milo","Sarah","Bruno","Anna","Rose"]
namesWith_o=[item for item in names if "o" in item]
print(namesWith_o)

names=["Milo","Sarah","Bruno","Anna","Rose"]
namesWith_o=[item for item in names if (len(item)>4)]
print(namesWith_o)


