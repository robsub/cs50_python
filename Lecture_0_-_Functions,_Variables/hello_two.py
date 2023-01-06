# Create our own functions

#  define a function <hello> and a parameter <to>
#   hello that prints hello <name>, <name> give it a parameter of to

def hello(to):
    print("hello,", to)

name = input("What's your name? ")

# call the function
hello(name)


# you are creating your hello function. This time, however, you are 
# telling the compiler that this function takes a single parameter: a variable called to. 
# 
# Therefore, when you call hello(name) the computer passes name into the hello function as 
# to. This is how we pass values into functions. Very useful!






# We can change our code to add a default value to hello:

# Create our own function
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()
# Test out your code yourself. Notice how the first hello will behave as you might expect and the second hello, 
# which is not passed a value, will by default output hello, world.








# We don’t have to have our function at the start of our program. We can move it down, but we need to tell the compiler that we have a main function and we have a separate hello function.

def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)
# This alone, however, will create an error of sorts. If we run python hello.py nothing happens! The reason for this is that nothing in this code is actually calling the main function and bringing our program to life.

# The following very small modification will call the main function and restore our program to working order:

def main(): # convention to use main

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function 
def hello(to="world"):
    print("hello,", to)


main()





# Scope refers to a variable only existing in the context in which you defined it. So this won't work:

def main():
    name = input ("whats your name? ")
    hello()

def hello():
    print("hello,", name) # name is not within the scope of main

main()

# whats your name? roib
# Traceback (most recent call last):
#   File "/Users/rob/Learning/STARTED/cs50_python/Lecture_0_-_Functions,_Variables/./hello_two.py", line 98, in <module>
#     main()
#   File "/Users/rob/Learning/STARTED/cs50_python/Lecture_0_-_Functions,_Variables/./hello_two.py", line 93, in main
#     hello()
#   File "/Users/rob/Learning/STARTED/cs50_python/Lecture_0_-_Functions,_Variables/./hello_two.py", line 96, in hello
#     print("hello,", name)
#                     ^^^^
# NameError: name 'name' is not defined