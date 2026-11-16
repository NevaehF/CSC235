# This program will demo how to print a list 

print("\n\n\t *** This program will demo collections in Python ***\n")
print("Available items for online ordering.")

# Create a list with grocery items
grocery_list = ["Milk", "Bread", "Celery", "Peanut Butter"]

# print out the items in the list 
item_number = 0

# Loop through the item 
for each_grocery_item in grocery_list:
    print(item_number, each_grocery_item)
    # Add 1 to the item number each time the loop runs
    item_number = item_number + 1

# Get the number of the item that you would like to order 
item_pick = input("Please enter the number of the item you would like to order: ")
    
print("\nHere is your ordered item: " + grocery_list[int(item_pick)])

    