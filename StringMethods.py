#Strings are immutable
a = "!!Harry!! !!!!!! Harry!!"

print(a)
print(len(a))
print(a.upper())              # Changes the string into upper case.
print(a.lower())
print(a.rstrip("!"))          #Strips only trailing characters.
print(a.replace("Harry","John"))
print(a.split(" "))           #Splits the given string at the specified instance and returns separated strings as list items.

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 ="Welcome to the console"
print(str1.center(50))          # Aligns the string to the center as per the parameters given by user.

print(a.count("Harry"))
print(str1.endswith("!!"))      # Checks if a string ends with a given value.
print(str1.endswith("to",4,10)) # Check for a value in-between the string by providing start and end index positions.

str1 = "python language"
print(str1.startswith("python"))        # Checks if the string starts with a give value.

str1 = "His name is Dan. He is an honest man." # Variables can be over-written.
print(str1.find("name"))              # Searches for the first occurence of given value & returns the index.If given value is absent from string then return -1.
print(str1.index("is"))               # If given value is absent then raises an exception.

str1 ="WelcomeTotheConsole"
print(str1.isalnum())      # Returns TRUE if entrie string only consists of A-Z,a-z,0-9.
str1="WElcome007"
print(str1.isalpha())      # Returns TRUE if string only contains A-Z,a-z.

str1 = "hello world"
print(str1.islower())      # TRUE if all the characters in string are lower case.
print(str1.isupper())      # TRUE if all the characters in the string are upper case.

str1 = "We wish you a Merry christmas\n"
print(str1.isprintable())

str1 ="   "
print(str1.isspace())     # TRUE only if string contains white spaces.

str1 = " World Health Organisation"
print(str1.istitle())     # TRUE only if first letter of each word is capitalised.

str1 = "Python is an Interpreted language"
print(str1.swapcase())    # Changes the character casing of string.

str1 = "His name is Dan."
print(str1.title())       # Capitalises each letter of the word within the string.
 