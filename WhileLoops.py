i=0
while(i<=3):
    print(i)          # Incrementing loop.
    i=i+1
print("Done with this loop.")

count=5
while(count>0):
    print(count)      # Decrementing loop.
    count=count-1
else:
    print("I am inside else, out of the loop!")

j=0
while True:
    print(j)         # Emulating the do-while loop.
    j=j+1
    if(j%10== 0):
        break
    