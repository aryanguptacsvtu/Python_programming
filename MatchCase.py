x =int(input("Enter the value of x:"))

match x: 

    case 0:
        print("x is zero.")
    case 5:
        print("x is 5.")

    case _ if x!=80:           # Case with if-condition.
        print(x,"is not 80.")
    case _ if x!=90:
        print(x,"is not 90.")  # No need to use "break" statements in Python.

    case _:                    # case_ is the default condition.
        print(x)