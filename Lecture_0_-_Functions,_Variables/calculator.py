x = 1
y = 2

print(x + y + 55)


x = input("What's x? ") 
y = input("What's y? ")

z = int(x) + int(y) # “casting” where a value is temporarily changed from one type of variable (in this case a string) to another (here, an integer).
print(z)

# Running this program, we discover that the output is incorrect as 12. Why might this be?
# Prior, we have seen how the + sign concatenates two strings. Because your input from your 
# keyboard on your computer comes into the compiler as text, it is treated a string. We, therefore, 
# need to convert this input from a string to an integer.




# We can further improve our program as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
# This illustrates that you can run functions on functions. The most 
# inner function is run first, and then the outer one is run. First, 
# the input function is run. Then, the int function.


# Float Basics
# A floating point value is a real number that has a decimal point in it, such as 0.52.
# You can change your code to support floats as follows:

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(z)



# How can we round floating point values? First, modify your code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(z)
# When inputting 2 as x and 3 as y, the result z is 0.6666666666 seemingly going on to infinite as we might expect.

# Let’s imagine that we want to round this down, we could modify our code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round
z = round(x / y, 2)

# Print the result
print(z)
# As we might expect, this will round the result to the nearest two decimal points.

# We could also use fstring to format the output as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = round(x / y)

# Print the result
print(f"{z:.2f}")
# This cryptic fstring code displays the same as our prior rounding 
# strategy.