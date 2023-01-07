import re
# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. 
# Otherwise, output $100. Ignore any leading whitespace in 
# the user’s greeting, and treat the user’s greeting case-insensitively.


# pseudocode
# If greeting start with "hello" print "$0"
# If greeting start with "h" but not hello, print "$20"
# Elif pint "$100"



response = input("Greeting: ")

if response.startswith("hello"):
    print("$0")



# https://github.com/haleyelder/cs50

# https://rivea0.github.io/blog/solving-the-problem-sets-of-cs50s-introduction-to-programming-with-python-problem-set-1/



    

# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.