countries=("Spain","Italy","India","Germany")

# Convert firstly tuple into a list,then perform operations and convert it back to tuple.
temp=list(countries)
temp.append("Russia")       # Add item.
temp.pop(3)                 # Remove item.
temp[2]="Finland"           # Change item.
countries=tuple(temp)
print(countries)

A=("Pakistan","India","Bangladesh")
B=("Vietnam","China")
Asia=A+B                     # Concatenating two tuples.
print(Asia)

tuple1=(0,12,3,4,56,1,3,7,3,78,3)
a=tuple1.count(3)
print("The count of 3 is:",a)

b=tuple1.index(3)
print("First occurence of 3 is:",b)

c=tuple1.index(3,4,8)         #tuple.index(element,start,end)
print("Index of 3 between indexes(4:8) is:",c)

d=len(tuple1)
print("The length of tuple1 is:",d)
