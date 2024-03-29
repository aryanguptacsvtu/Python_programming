double = lambda x: x*2
cube = lambda x: x*x*x
average = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(3))
print(average(3,5,10))


def apply(f,value):              # Passing function(f) to a function(apply).
    return 6 + f(value)

print(apply(cube,2))
print(apply(lambda x: x*x , 5))  # Here, lambda function is anonymous,as it does not have a name.



# Lambda functions are often used in situations where a small function is required for a short period of time.
# Lambda functions can also include multiple statements.
