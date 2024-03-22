for i in range(6):
    print (i)
else:
    print("Sorry no i.")


for i in []:
    print(i)
else:
    print("Noo i.")


for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Sorry!!")
print("\n")


j=0
while(j<7):
    print(j)
    j=j+1
else:
    print("Sorry no j.")
print("\n")


for x in range(5):
    print("Iteration no.{} in for loop".format(x+1))
else:
    print("Out of loop.")

