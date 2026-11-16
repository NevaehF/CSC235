# import the tkinter built-in Python HUI library
import tkinter as tk
# import the message box and file dialog features of tkinter 
from tkinter import messagebox, filedialog

# Event handler/function for clearing the note/text box 
def clearNote():
    # Delete everything in the textbox from for 1, colum 0 to the end of the textbox
    text.delete("1.0", "end")

# Event handler / function to save the note
def  saveNote():
    # Create a variable to hold the text that the user has entered into textbox
    note = text.get("1.0", "end-1c")

     #ask the user where they want to 
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

     # If a file path was selected by the user 
    if filePath:
         # Open the file for writing
         with open(filePath, "w") as file:
            file.write(note)

         # Show a message box
            messagebox.showinfo("Note Saved", "Your note has been saved.")

# Create the event handler / function to open note and replace the text in the text box 
def openNote():
    # Ask the user for a file to open 
    filePath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    # If the user selected a file
    if filePath:
        # Open the file in read mode
        with open(filePath, "r") as file:
            # Get the contents of the file and set them to variable 
            note = file.read()

            # Clear out the textbox 
            text.delete("1.0", "end")

            # Add the text from the file to the textbox
            text.insert("1.0", note)


# Create a main window
root = tk.Tk()
# Set the title for the window 
root.title("Simple Note Taking App")

# Create a text box, with word wrapping 
text = tk.Text(root, wrap=tk.WORD)

# Pack the text box, tell it to fill the window
text.pack(fill="both", expand=True)

# Create a button to save the note 
saveButton = tk.Button(root, text="Save Note", command=saveNote)

# Pack the button so it will show up in the window 
saveButton.pack(side=tk.LEFT)

# Create a button to open the note 
openButton = tk.Button(root, text="Open Note", command=openNote)

# Pack the button so it will show up in the window 
openButton.pack(side=tk.LEFT)

# Create a button to clear the text area/note 
clearButton = tk.Button(root, text="Clear Note", command=clearNote)

# Pack the button so it will show up in the window 
clearButton.pack(side=tk.LEFT)


# Start the main event loop to run the GUI
root.mainloop()
