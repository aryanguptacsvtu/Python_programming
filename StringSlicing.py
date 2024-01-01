fruit ="Mango"
len1 = len(fruit)       #To know the length of word
print("Mango is a",len1,"letter word") 

print(fruit[0:4])       #including 0 but not 4
print(fruit[:4])        #python assumes 0 itself 

print(fruit[1:4])       #including 1 but not 4
print(fruit[:5]) 
print(fruit[:])         #python assumes 5 itself here


print(fruit[0:-3])      #NEGATIVE SLICING
print(fruit[:len(fruit)-3])

print(fruit[-3:-1])     #python assumes len(fruit) itself like [len(fruit)-3 : len(fruit)-1]
  