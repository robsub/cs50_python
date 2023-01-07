# Demonstrates addition

x = 1
y = 2

z = x + y

print(z)
# Demonstrates (unintended) concatenation of strings

# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = x + y
print(z)
# Demonstrates formatting after the decimal place

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x / y

print(f"{z:.2f}")
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
# Demonstrates conversion from str to int

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
# Demonstrates nesting of function calls

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y

print(z)
# Demonstrates conversion of str to float

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

print(z)
# Demonstrates rounding to nearest int

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)
# Demonstrates fewer variables

x = float(input("What's x? "))
y = float(input("What's y? "))

print(round(x + y))
# Demonstrates formatting with commas

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
# Demonstrates division

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)
# Demonstrates rounding after the decimal point

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)
# Demonstrates a function with a positional argument

print("hello, world")
# Demonstrates a function with a positional argument and a return value

name = input("What's your name? ")
print("hello,")
print(name)
# Demonstrates defining a function with a parameter with a default value


def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)
# Demonstrates defining a main function


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
# Demonstrates concatenation of strings

name = input("What's your name? ")
print("hello, " + name)
# Demonstrates a function with two positional arguments

name = input("What's your name? ")
print("hello,", name)
# Demonstrates a function with a positional argument and a named argument

name = input("What's your name? ")
print("hello, ", end="")
print(name)
# Demonstrates a format string

name = input("What's your name? ")
print(f"hello, {name}")
# Demonstrates str functions

name = input("What's your name? ").strip().title()
print(f"hello, {name}")
# Demonstrates str functions

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")
# Demonstrates defining a function without parameters


def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
# Demonstrates defining a function with a parameter


def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)

