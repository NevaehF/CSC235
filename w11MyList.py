# This program is a movie night watch list

print("\n\n\t *** Lets Pick Movies To Order ***\n")
print("Available Movies: ")

# Lets create our Movie List for the evening
movie_list = ["Stewart Little", "UP!", "The Goofey Movie", "Arlo The Alligator Boy", "Mean Girls"]

# print out the movies in the line up  
movie_number = 0

# Loop through the movies 
for each_movie_title in movie_list:
    print(movie_number, each_movie_title)
    # Add 1 to the movie number each time the loop runs
    movie_number = movie_number + 1

# Get the number of the item that you would like to order 
movie_pick = input("Please enter the number of the movie you would like to order: ")
    
print("\nHere is your ordered movie: " + movie_list[int(movie_pick)])