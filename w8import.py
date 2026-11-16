# Import adds the functionality of whatever module/package/library you would like to use
import os 
#import the math-y library numpy with the nickname np
import numpy as np

# Get the current working directory from the os library/module/package
currentDirectory = os.getcwd()

# Print out the current directory
print("Current working directory:", currentDirectory)

# Create a new directoy
newDirectory = "awesome_dir"
#os.makedirs(newDirectory)

# print out a new directory name 
#print("New directoy created:,", newDirectory)

# Delete my awesome directory :(
#os.rmdir(newDirectory)

# Print out new statement indicating the directory has been removed
#print("New Directory removed,")

# List the files in a directory 
files = os.listdir(currentDirectory)

print("Here are the files in the current directory: ")

# Loop through the files and print out each file name 
for eachFile in files : 
    print(eachFile)

# Create a 1 demensional array, numpy handles complex math/array stuff better than a built in python 
arr1d = np.array([1,2,3,4,5,6])

print("1 d array contents", arr1d)

# Create a 2d array 
arr2d = np.array([1,2,3,4,5,6,], [1,2,3,4,5,6], [1,2,3,4,5,6])

print("2 d array contents", arr1d)




