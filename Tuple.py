tup=(1,13,55,342,"blue",True,434)
print(type(tup))        
print(len(tup))            # Tuples are unchangeable.
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])

print(tup[-3])             # Negative index.
print(tup[len(tup)-3])

if 342 in tup:
    print("Yess,it is present.")
    
if "Green" in tup:
    print("Yes")
else:
    print("No")

animals=("cat","dog","lion","cow","pig",31,868,12,17,8)
print(animals[3:7])
print(len(animals))
print(animals[-7:-2])
print(animals[::2])
print(animals[2:9:3])       # TupleName[start:end:jump]

tup2=(34,231,67,567,87)
print(tup2[0:])
print(tup2[:3])
print(tup2[:])
