marks =[21,4,34,45,57,343,23,88]

index=0
for mark in marks:
    print(mark)                  # Without using Enumerate function.
    if (index==3):
        print("Awesome!!")
    index +=1

print("\n")


fruits =["apple","mango","orange","banana","grapes"]
for index,fruits in enumerate(fruits):
    print(fruits)
    if (index==3):                        # Enumerate function starts index at 0.
        print("Awesome!!")
   
print("\n")


months=["Jan","Feb","March","May"]              # Changing the start index.
for index,months in enumerate(months,start=1): 
    print(index,months)

