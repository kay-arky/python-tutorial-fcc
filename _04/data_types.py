import math
# String data type

# literal assignment

first = "Hizkia"
last = "Arundaa"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# contructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, How are you
                                                        
I was just checking in.
                        All good?
'''
print(multiline)

# Escaping special characters
sentence = "I\'m back at work!\tHey!\n\nWhere\'s this at\\located?"
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first.capitalize())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                         "
multiline = "                          " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("H"))
print(first.endswith("i"))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
ipk = 3.75
y = float(1.14)
print(type(ipk))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(ipk))
print(abs(ipk * -1))

print(round(ipk))

print(round(ipk, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(ipk))
print(math.floor(ipk))

# Casting a string to a number
zipcode = "123123"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
