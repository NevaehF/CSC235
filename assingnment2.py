""" Nevaeh Fernandez
     Jan.18.2024 """

# For assignment 2 we need user input and output and 2 variables. 

# Welcome message for the user 
print("Welcome to my tutorial about the print function in Python")

# ask the user for their name using the input function. 
userName = input("Please enter your name:  ")

# print out the name of the user 
print("I hope you enjoy the tutorial", userName)

# explain some different ways to print in Python
print("One way to print out text in Python is like so: ")
print("print('The weather in Pheonix is great', 75)\n")
print("You can seperate different things to print with a comma. A space will be added with each instance of each comma.")
print("print('The weather in Peonix is great' , 75, 'is todays ig temp')\n")

#lets sow aoter way to use te prit statement
print("another way to print out text in Python is like so:")
print("print('The weather in Pheonix is great ' +75)\n")

# lets ask the user how they would rate my tutorial
ratingStr = input("Please let me know how you rate my tutorial so far ( 1-10, 10 being the highest)")
ratingInt = 0

# Check to see if user entered a number
if ratingStr.isnumeric():
    # This code is indented, so it belongs to the if statment. 
    # We can cast the user iput to an int because we kow the user etered a number
    ratingInt = int(ratingStr)
    print("Nice job following directions")
else: 
        # The user did not eter input correctly 
    print("Please pay better attetion next time")


# let's talk about "f" string formatting
    # make sure to include the "f" in the begining of the line or else it will print a funky result 
print(f"Here is the information you have entered so far: your name: {userName} and your rating of my awsome tutorial: {ratingStr}")

# aanother way to print is using the "f" string (formatting)
print("A third way to print out text in python is like so: ")
print("This is an easy way to print out the values of your variables.")
print("print(f'Here is the information you have entered so far: your name: {userName} and your rating of my awsome tutorial: {ratingStr}')\n")

print("Have a nice day!")