1# For this assignment, you need to wite a file and read from a file 

# Function that reads from a file 
def readFromFile(fileNameToRead):
    # Open the file in read mode
    with open(fileNameToRead, 'r') as file: 
        # read the contents of the file was just opened 
        data = file.read()
        # Return the contents of the file to the code that called the function 
        return data
    
    # Function that writes to a file 
def writeToFile(fileNameToWrite, fileData):
        # Open the file in write mode 
        # a - append - add your new info to the end of the file 
        # w - write - overwrite existing data with your new info 
        with open(fileNameToWrite, 'a') as file: 
            # Write the text that we passed into the function in the FileData argument to the file 
            file.write(fileData)

    # Main program, the user can choose to add an entry to their journal 
    # Or they can read the entries 
            
while True: 
     # This is the name of our file
    theFileName = "journal.txt"
     
     # Print out menu options for the user 
    print("1. Create a new Journal Entry")
    print("2. View past Journal Entries")
    print("3. Exit")

     # ask the user which option they want, store that in a variable 
    choice = input("Enter your choice (1/2/3):")

     # Check the entry; if they entered 1, then let them create a journal entry 
    if choice == "1" : 
          # Get the entry from the user 
      journalEnrty = input("Enter your journal entry: ")
         # add entry to file
      writeToFile(theFileName, journalEnrty + "/n")
      print("Journal Entry Created")
    elif choice == "2" : 
         # Read the file 
        print(readFromFile(theFileName))
    elif choice == "3" : 
        print("Thank you for using my time machine journal")
        #break out of the while loop, so this is not an infinate loop 
        break 
     #catch all for anything other than 1,2, or 3
    else: 
        print("Invalid choice. Please enter 1, 2, or 3")