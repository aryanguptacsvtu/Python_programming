def factorial(n):
    if (n==0 or n==1):
        return 1
    else:                               # Using Recursive function.
        return n*factorial(n-1)
    
n=int(input("Enter the no. whose factorial you want:"))

print("Factorial of",n,"is:",factorial(n))


