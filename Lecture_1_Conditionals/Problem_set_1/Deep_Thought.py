# Deep Thought
# “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
# “You’re really not going to like it,” observed Deep Thought.
# “Tell us!”
# “All right,” said Deep Thought. “The Answer to the Great Question…”
# “Yes…!”
# “Of Life, the Universe and Everything…” said Deep Thought.
# “Yes…!”
# “Is…” said Deep Thought, and paused.
# “Yes…!”
# “Is…”
# “Yes…!!!…?”
# “Forty-two,” said Deep Thought, with infinite majesty and calm.”

# — The Hitchhiker’s Guide to the Galaxy, Douglas Adams

# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.



# Hints
# No need to convert the user’s input to an int if you check for equality with "42", a str, rather than 42, an int!
# It’s okay if your output or the user’s wraps onto multiple lines.



# $ python deep.py                                                                                    
# What is the Answer to the Great Question of Life, the Universe, and Everything? 42                  
# Yes                                                                                                 
# $ python deep.py                                                                                    
# What is the Answer to the Great Question of Life, the Universe, and Everything? forty-two           
# Yes                                                                                                 
# $ python deep.py                                                                                    
# What is the Answer to the Great Question of Life, the Universe, and Everything? forty two           
# Yes                                                                                                 
# $              


# pseudocode

# if input is 42
# print yes
# if input is forty-two
# print yes
# if input is forty two
# print yes

# First attempt

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else: 
    print("No")



# Second attmpt (can I use a method like .strip
# )answer = input("Do you agree? ").strip() or something?


answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer == "42" or "forty two" or "forty-two":
    print("Yes")
elif: 
    print("No")

# This can be improved with .strip (remove hyphen) and somet other method?