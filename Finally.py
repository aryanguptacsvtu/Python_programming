def fun():
    try:
        l=[1,23,5,67]
        i=int(input("Enter the index:"))
        print("The value from list:",l[i])
        return 1
    except:
        print("Some error occured.")
        return 0
    finally:
        print("I am always executed.")


x = fun()
print("The value of x:",x)
