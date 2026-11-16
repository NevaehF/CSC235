# import the Python random library
import random
# 4 basics of programming are:

# variables
usersName = "Nevaeh"

# functions
# when you create a function in Python use the word def 
# the function name should usually be some sort of action
# make sure to include () and the :
# if you want to have the function use variable(s) from other part of the code, put the variables between the ()
def calcScore(hits, misses):
    # all this function needs to do is some arbitrary math
    # that arbitrary result is passed back to the code that called the function
    return (hits * 10) - (misses * 5)

# let's create a fundtion to randomly high five
def highFiveEnemy():
    # we want to randomly high five the enemy
    return random.choice([True, False])

# let's code a high five game
def playGame():
    # set up our game play variables
    hits = 0 # hit tracker, default to 0
    misses = 0 # misses tracker, default to 0
    totalRounds = 10 # how many round you want the game to last

    # welcome message
    print("Welcome to my game. Have fun high-fiving your opponent.")

    # set up a for loop to run the rounds
    for _ in range(totalRounds):
        print("Press Enter to try to high five the enemy...")
        input()

        # call the random high five generator, if high five was susccessful, print such
        if highFiveEnemy():
            print("Enemy was High Fived")
            hits += 1
        # bummer, high five missed
        else:
            print("Enemy was not High Fived")
            misses += 1

    score = calcScore(hits, misses)
    print("Game over")
    print(f"You score: {score}")
    print("Thanks for playing")

    
# loops
# in Python we have 2 types of loops:
# for loop - generally use a for loop when you know (or Python knows) how many times you want the loop to run
# while loop - generally use a while loop when you do not know how many times the loop will run

# easy way to set up a while loop; this loop will run forever
# remember that True and False in Python have capital T and capital F
while True:
    # call the play game function
    playGame()

    # let's ask the user if they want to play our game again - make sure to offer guidance for how you want the user to answer
    response = input("Do you want to play again? (yes/no): ")

    # check the user's answer, if they respond with anything other than "yes", they leave the program
    if response != "yes":
        # say goodbye
        print("Thanks for playing")
        # the break statement will get us out of our infinite while loop
        break

# decision logic (if/else statements)