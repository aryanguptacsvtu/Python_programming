letter="Hey my name is {1} and I am from {0}"
country="India"
name="Aryan"
print(letter.format(country,name)) # String formatting

print(f"Hey my name is {name} and I am from {country}") # Using f_string.

price=49.0999
txt=f"For only {price:.2f} dollars!"
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

print(f"We use f-strings like this:Hey my name is {{name}} and I am from {{country}}")
