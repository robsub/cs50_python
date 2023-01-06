name = input ("What's your name? ")
print("hello, " + name) 



# SUPRISED BY THIS We can  (as well as '"hello, " + name') use a comma instead, to pass in multiple arguments by editing our code as follows:
#
# name = input("What's your name? ")
# print("hello,", name)

#print("hello, " + name)  - ONE ARGUMENT
#print("hello,",name)  - TWO ARGUMENTS




name = input ("What's your name? ")
print("hello,", name) 

name = input ("What's your nameee? ")
print("hello, " + name + name + " test,", name, name) 


name = input ("What's your nameee? ")
print("hello, " + name + name + " test,", name, name) 


# https://docs.python.org/3/library/functions.html?highlight=print#print
#  
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# print(argument argument argument) [what the function can take]
# AKA
# print(parameter parameter parameter) [What I choose to put into the function]

name = input ("What's your nameee? ")
print("hello, " + name + name + " test,", name, name) 


#print ("hello, ", sep="???", + name + end="" )
#print(name)
# ➜  Lecture_0_-_Functions,_Variables python3 hello.py
#  File "/Users/rob/Learning/STARTED/cs50_python/Lecture_0_-_Functions,_Variables/hello.py", line 39
#    print ("hello, ", sep="???", + name + end="" )                                ^
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
#
# ###

# Zero distinction between "" and ''

# positional parameters eg "hello" or name
# named parameters eg sep (optional)

print('hello, "friend"')
#prints hello, "friend"  #combine single and double qoutes

print("hello, \"friend\"") #escape characters 
#prints hello, "friend"



# Probably the most elegant way to use strings would be as follows:

# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
# Notice the f in print(f"hello, {name}"). This f is a special indicator to Python to treat this string a special way, 
# different than previous approaches we have illustrated in this lecture. Expect that you will be using this style of strings 
# quite frequently in this course.




# You should never expect your user will cooperate as intended. Therefore, you will need to ensure that the input of your user is corrected or checked.
# It turns out that built into strings is the ability to remove whitespace from a string.
# By utilizing the method strip on name as name = name.strip(), it will strip all the whitespaces on the left and right of the users input. You can modify your code to be:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")


# Rerunning this program, regardless of how many spaces you type before or after the name, it will strip off all the whitespace.

# Using the title method, it would title case the user’s name:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()


# Capitalize the first letter of each word
name = name.title()


# Print the output
print(f"hello, {name}")

# for more see https://docs.python.org/3/library/stdtypes.html#string-methods

name = input("tell me your name")
print()








# Notice that you can modify your code to be more efficient:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"hello, {name}")

# We could even go further!

# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()



# split users name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")

