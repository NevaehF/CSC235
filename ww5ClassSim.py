# This is going to be a text-based sim for the week 5 assignment. The user will get different options based on the choices they make. 

# Requirments - 3 blocks of if/else chunks, ideally there should be nesting 3 levels deep

# Include lots of comments and a nice user experiance 

# Welcome the user to your program 
print("welcome to my text-based sim. Please play multiple times ")
print("You find yourself at a crossroads. Which path will you take? ")
print("1. Follow the path through the forest.")
print("2. Take a bridge over the river. ")

# Need to gather input from the user for what path they want to take 
# Use an input() statement here, assign the user input to a variable 
choice1 = input("Enter your choice (1 or 2): ")
                
# THIS is our FIRST block 1/3 
if choice1 == '1' : 
    # If the user chooses option 1, then they go down some path 
    # Print out the next scenerio 
    print("You enter the dense forest. Which path will you take? ")
    print("1. Investigate a strange noise. ")
    print("2. Ignore the noise and walk the other way. ")

    # Need to gather input from the user for what path they want to take 
    # Use an input() statement here, assign the user input to a variable 
    choice2 = input("Enter your choice (1 or 2): ")

     #THIS is our SECOND block 2/3
    if choice2 == '1' : 
            # If the user chooses option 1, then they go down some path 
        print("You enter a clearing. The noise is louder and is in front of you. ")
        print("1. Walk towards the nose.")
        print("2. Ignore the noise and run the other way.")

    elif choice2 == '2' : 
        print("You took a bridge over the river. you see a boat waiting in the distance.")
        print("1. Get on the boat")
        print("2. Keep walking")
        

    # Need to gather input from the user for what path they want to take 
    # Use an input() statement here, assign the user input to a variable
        choice3 = input("Enter your choice (1 or 2): ")

        #THIS is our THIRD block 3/3 
        if choice3 == '1' : 
        # IF user has picked choice '1' 3 times they win!
         print("You discover some people digging up a tresure chest. They give you 1/2 of the tressutr. COngradulations - you win!!")

        elif choice3 == '2' : 
         print("You discover a brief case full go gold - you win")
        else: 
         print("Please enter only 1 or 2. ")

#If the user chooses option 2, go down a different path 
elif choice1 == '2' :
    # This could be another set of nested if/else statements or it could be a dead end 
    print("You have reached a dead end. Please play again.")
else: 
    print("Choose 1 or 2")


#TODO: set up a loop so the program will automatically run again 
    print("Thank you for playing. Please play again by running the Pythin code again") 