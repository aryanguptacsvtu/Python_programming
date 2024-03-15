def calculateGmean(a,b):     # a,b are arguments
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(x,y):          # x,y are arguments
    if(x>y): 
        print("First number is greater.")
    else:
        print("Second number is greater.")

def isLesser(a,b):
    pass              # Only defining the function(I will write the body of function later)

a=9;b=3
isGreater(a,b)               # Calling the function 
calculateGmean(a,b)

c=10;d=12
isGreater(c,d)               # USER-DEFINED Functions.
calculateGmean(c,d)

