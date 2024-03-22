a = input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except:
    print("Invalid Input!")

print("Some imp lines of code.\n")


try:
    num=int(input("Enter a integer:"))
    a=[6,3]                   # a[0]=6 , a[1]=3 {List}
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index error has occured.")
print("\n")


B=int(input("Enter the value of B:"))
try:
    for i in range(5):
        print(B)
except Exception as e:
    print(e)
