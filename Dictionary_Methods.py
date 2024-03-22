emp1 = {122:43, 123:65, 567:87, 125:67}
emp2 = {553:65, 589:23}

emp1.update(emp2)
emp1.update({'Name':'Ankit'})
print(emp1)

empty ={}             # Creating Empty Dictionary.
print(empty) 
emp1.clear()          # "clear()" removes all the items from dictionary.
print(emp1)     


info = {'name':'Aryan','age':19,'class':10,'eligible':True}
info.pop('age')
print(info)

info.popitem()
print(info)           # "popitem()" removes the last key-value pair from dictionary.


Dict = {434:54, 234:78,"name":"Harry"}
del Dict[234]
print(Dict)

del Dict             # If 'Key' is not provided, then "del" will delete the entire dictionary. 
# print(Dict) will raise an Error.
