# These functions are known as "higher-order functions",as they take other functions as arguments.

def cube(x):
    return x*x*x

l=[1,2,4,6,3]

newl=[]
for item in l:
    newl.append(cube(item))
print(newl)

Newl=list(map(cube,l))               # "Syntax":- map(function,iterable)
print(Newl)


def filter_function(a):
    return a>2

NEWl=list(filter(filter_function,l)) # "Syntax":- filter(predictable,iterable)
print(NEWl)


from functools import reduce
numbers=(1,2,3,4,5)
sum=reduce(lambda x,y:x+y,numbers)   # "Syntax":- reduce(function,iterable)
print(sum)


# "map" function applies a function to each element in a sequence & returns a new sequence containing the transformed elements.

# "filter" function filters a sequence of elements based on a given predictable(a func. that returns a boolean value) & returns a new sequence containing only elements that meet the predictable.

# "reduce" function applies a function to a sequence & returns a single value.It is a part of 'functools' module.
