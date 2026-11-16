# This is a Python Comment 

# create a variale on Python like so: (using camelcase)
firstName = "Nevaeh"

# snake case 
fisrt_name = "Nevaeh"

# It doesn't matter1 hwat style you go with, but be consistant 

# Print number variale
favoritePrimeNumber = 11

# Distance to nearest InNOut
distanceToInNout = .1

# Booleans are true or false 
isItLunchTime = True 
#True and False are capitalized in Pythonn 

# Python function 
def addNumbers():
    # Indentations are super dupe important
    sum = 1 + 2 

rating = int(input("How cool are variables?"))


# Let's talk about file reading and writing

# open - first argument is the file name
#      - second argument is how to open the file
#        w and a are the most common ways to open the file
#        w - (write) it will create the file if it does not exist, and overwrite the contents 
#            if the file does exist
#        a - (append) it will create the file if it does not exist, if the file does exist
#            it will append your new text to the file

# create a file, write text to it in 2 lines
with open("test.txt", "a") as file:
    file.write("This is a test.")

# open a file, reading the contents
# first argument is the filename, second is how to open the file,
# use r for read
with open("test.txt", "r") as file:
    content = file.read()
    print("File contents: ", content)


# Let's talk about if/else logic
# if/else is when you want to have various branches for the code to potentially run

# get an input from the user of the current temperature
temp = int(input("Enter the current temperature: "))

# here are some different messages to print depending on the user input
if temp > 140:
    print("It's so hot you should go somewhere else")
# the Python equivalent of else if is elif (not elf)
elif temp <= 120 and temp > 90:
    print("It is very hot.")
elif temp <= 90 or temp > 140:
    print("This doesn't feel too warm")
# This is the catch all if none of the previous statements were true, this code will run
else:
    print("The temp is either nice or really cold. ")

