# Dictionaries are 'Ordered' collection of data items.
# Dictionary items are key-value pairs.

info = {'name':'Aryan','age':19,'eligible':True}
print(info)
print(info['name'])
print(info.get('eligible'))

# "print(info[name2])" will raise an 'Error'as key(name2) doesn't exist.
print(info.get('name2'))    # Prints "None" if key doesn't exist.

print(info.keys())
print(info.values())

for key in info.keys():
    print(key)               # Prints the "Keys".

for key in info.keys():
    print(info[key])         # Prints the "Values".

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}.")

print('\n')
print(info.items())

for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}.")

