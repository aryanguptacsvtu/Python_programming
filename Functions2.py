def average(a,b):
    print("The average of a and b is:",(a+b)/2)
average(21,11)  


def avg(x=9,y=1):              # DEFAULT ARGUMENTS
    print("The average of x and y is:",(x+y)/2)  
avg()
avg(1,5)  
avg(8)
avg(y=10)  
avg(y=100,x=20)                # KEYWORD ARGUMENTS(Order does not matter)


def averageIs(A,B,C=1):        # REQUIRED ARGUMENTS(A,B)
    print("The average of A,B,C is:",(A+B+C)/3)
averageIs(A=10,B=11)
averageIs(5,2)
averageIs(A=10,B=10,C=10)


def avrg(*numbers):            # VARIABLE-LENGTH ARGUMENTS(To pass more no. of arguments)
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
avrg(10,123,18,20)


def name(**names):
    print(type(names))
    print("Hello,",names["fname"],names["mname"],names["lname"])
name(mname="Hemsworth",lname="Barnes",fname="James")


def avreg(*number):           
    
    sum=0                      # RETURN statement
    for i in number:
        sum=sum+i
    return sum/len(number)
W=avreg(10,10,10)
print(W)