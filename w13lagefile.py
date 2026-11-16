# import the tkinter library so we can make a GUI
import tkinter as tk
# import the messagebox library so we can show messageboxes
from tkinter import messagebox
# import random number generating library
import random

# function to write numbers to a file
def writeToFile(fileName):
    # create a list to hold a bunch of random numbers
    largeList = []

# Number of data points to cretae
    numDataPoints = 10000

    # create a loop to generate random numbers
    for _ in range(numDataPoints):
        aRandomNumber = random.randint(1, numDataPoints)
        # add the random number to the list
        largeList.append(aRandomNumber) 

    # loop through the list and write the contents to a file
    try:
        # open the file in write mode
        with open(fileName, 'w') as file:
            # write the numbers to the fil
            for dataPoint in largeList:
                file.write(str(dataPoint) + ",")
    except Exception as e: # Handle any generic exception that may happen
        messagebox("Error", f"An error occurred with the file writing: {str(e)}") # TODO: make the error message more generic

# read from the file
def readFromFile(fileName):
    data = ""
    try:
        with open(fileName, 'r') as file:
            # read the file contents into the data variable
            data = file.read()
            return data
    except FileNotFoundError as e: # handle the specific file not found error
        messagebox("Error", "The file was not found")
    except Exception as e: # Handle any generic exception that may happen
        messagebox("Error", f"An error occurred with reading from the file: {str(e)}") # TODO: make the error message more generic
    
def generateData():
    writeToFile("exampledata.txt")
    messagebox.showinfo("Success", "Large data file generated!")

# create a function to make sure that a number is a number
def isNumber(theSuspectedNumber):
    try:
        # Lets's se if our number can succesfully be casted as a float
        float(theSuspectedNumber)
        return True
    # If this canot be casted as a float, then it is 99% likley to be a value error
    except ValueError:
        return False

# the button calls this function to put the data from our file into the textarea
def displayData():
    # get the data from the file
    dataRead = readFromFile("exampledata.txt")
    
    # check to make sure that there was data in the file
    if dataRead is not None:
        # list to hold our formatted data
        formattedData = []

        # loop through the data
        for amount in dataRead.split(','):
             formattedData.append(f"${int(amount):,.2f}") # format our number in currency format $##.##

        #Convert the list data to a string where the currancy values are each on a new line
        dataToShow = "\n".join(formattedData)

        #If thee is data to show, add it op the text area.   
        if dataToShow:
            # First, enable the text area so we cn change the contents
            data_text.config(state=tk.NORMAL)
            data_text.delete("1.0", tk.END) #Delete anything in the text area
            data_text.insert("1.0", dataToShow)
            data_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("No data", "There is no data to display")

fileName = "exampledata.txt"
#writeToFile(fileName)

#print(readFromFile(fileName))

# create the GUI main application window
root = tk.Tk()
# set the title of our window
root.title("Large File Generator")

# Create a button for generating the data
generate_button = tk.Button(root, text="Generate Data", command=generateData)
generate_button.grid(pady=10) # add some padding so the buttons are separated a bit

# Create a button for displaying the data
display_button = tk.Button(root, text="Display Data", command=displayData)
display_button.grid(pady=10) # add some padding so the buttons are separated a bit

# create a frame to hold the text that will display the data
data_frame = tk.Frame(root)
data_frame.grid(row=4, column=0, pady=10, sticky="nsew")
root.grid_rowconfigure(4, weight=1) # allow row 4 to expand
root.grid_columnconfigure(0, weight=1) # allow column 0 to expand
data_frame.grid_rowconfigure(0, weight=1) # allow the data_frame row to expand
data_frame.grid_columnconfigure(0, weight=1) # allow the data_fram column to expand

# create the textbox to actually hold the data from the file
data_text = tk.Text(data_frame, wrap="word") # allow the words to wrap
data_text.grid(row=0, column=0, sticky="nsew") # place the text area in the data frame
scrollbar = tk.Scrollbar(data_frame, orient="vertical", command=data_text.yview) # create a scrollbar so we can vertically scroll
scrollbar.grid(row=0, column=1, sticky="ns")
data_text.config(yscrollcommand=scrollbar.set) # tell the scrollbar what to do 


# start the tkinter window
root.mainloop()