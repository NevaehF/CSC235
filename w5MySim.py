''' This going to be my text-based sim for the week 5 assignment. The user will get different options based on the choices they make. 
    Assignment Requirments - 3 blocks of if/else chunks, ideally there should be nesting 3 levels deep
                        I will include lots of comments and a nice user experiance '''

# Add while loop: 
while True: 

    # My welcome messsage to the user
    print("Welcome, I hope you have a great time playing my sim!! Play many times please.\n"  )

    # This is where the sim will start. first we need context
    print("Background: You've just heard thay theres been a lot of suspitious activity going on in your neighbor hood. ")
    print("There seems to be flesh eating alians but theres no information yet regarding how people are getting infected.")
    print("Now with this knowledge you need to be extra cautious when it comes to your saftey")

    print("You just got home from school and youre exhausted. You head to your room and see your window is slightly open. do you.....\n")
    print("1. Levae the window open to let the breeze in, whats the harm?.")
    print("2. Close it ")

    # Need to gather input from the user  
    # Use an input() statement here, assign the user input to a variable 
    choice1 = input("Enter your choice (1 or 2): ")
                    
    # THIS is our FIRST block 1/3 
    if choice1 == '1' : 
        # If the user chooses option 1, then they have to think fast for their next decision 
        # Print out the next scenerio 
        print("The parasite has now entred the room and goes in your hand. What do you do next?\n ")
        print("1. Grab the nearist cord and or sting and cut off the cerculation so the parasite cant reach your brain. ")
        print("2. Scream and hope someone hears you so they can help. ")

        # Need to gather input from the user 
        # Use an input() statement here, assign the user input to a variable 
        choice2 = input("Enter your choice (1 or 2): ")

        #THIS is our SECOND block 2/3
        if choice2 == '1' : 
                # If the user chooses option 1, then tthey have to choose what happens next 
            print("Good Job the parasite couldn't reach ypur brian in time and is now stuck in your arm. Now what??\n ")
            print("1. Cut your whole arm off, and live as though nothing happened?.")
            print("2. Learn to coexist witht this parasite.\n")

    # elif choice2 == '2' : 
        # print("Welp although you were screaming no one came in time and the parasite made it to your brain. you are now dead .")
        #  print(" Try your luck again.")
            

        # Need to gather input from the user 
        # Use an input() statement here, assign the user input to a variable
            choice3 = input("Enter your choice (1): ")

            #THIS is our THIRD block 3/3 
        if choice3 == '1' : 
            print("You and the paracite learn to fite and kill off those pesky zombies and help make the work normalagain. COngradulations - you win!!\n")

        elif choice2 == '2' : 
            print("Welp although you were screaming no one came in time and the parasite made it to your brain. you are now dead .")
            print(" Try your luck again.")
            
    # They need to think carfully which they did and lived
    elif choice1 == '2' :
        # They coild play again
        print("You live to see another day and the parasite doesn't take over your body - congrats you win!!.\n")

    # Ask the user if they want to play again 
    playAgain = input("Do you want to try your luck again? (y/n)")

    # if statement to handle the user the input 
    if playAgain.lower() == "n" :
        #print a message and exit loop 
        print("Until next time")
        # Exit the loop with the break statment 
        break 
    else: 
        # If tey enter in ay other work then no, o bak to the begii of the loop 
        # In this exaple, the print statment below would not run 
        continue 

print("Play again!! restart the python program")