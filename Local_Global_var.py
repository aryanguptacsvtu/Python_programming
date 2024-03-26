x= 10            # Global Variable

def func():
    global x
    x=634
    
    y=50         # Local Variable
    print(y) 

func()
print(x)

# "print(y)" will cause an error because it is not accessible outside the function.

# The 'global' Keyword is used to declare that a variable is a 'global variable' & it should be accessed with 'global scope'.
