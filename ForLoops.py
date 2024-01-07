name="Aryan"
for i in name:
    print(i)
print("\n")

colors =["Red","Blue","Green"]
for color in colors:
    print(color)
    for j in color:
        print(j)
print("\n")

# range(stop)            {1st TYPE}
# range(start,stop)      {2nd TYPE}
# range(start,stop,step) {3rd TYPE}
        
for a in range(5):  # Prints 0 to 4.
 print(a)
print("\n")

for b in range(1,5): # Stop value is not printed.
 print(b)
print("\n")

for c in range(17,53,5): 
 print(c)
print("\n")