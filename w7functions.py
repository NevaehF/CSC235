# def greet(name: str) -> str: 
#       return "Hello, " + name

# Function to add item to the shopping cart / list 
def addItem(cart, item): 
    # add the new item to the end of the list 
    cart.append(item)
    # Update user on what is happening (I wanted it to say the item that was added to further confirm)
    print(item, "was added to the cart!.")
    # return the updated list 
    return cart 

# Fuction to remove item from shopping cart / list 
def removeItem(cart, item): 
    # Delete item from the list if it exists in the list
    if item in cart:
        cart.remove(item)
        # Update user on what is happening 
        print(item, "was removed from the cart")
        # Return the updated list 
        return cart 
    else: 
        print("Item was not in cart")

# Function to view items in shopping cart / list 
def viewCart(cart): 
    if cart: 
        print("Shopping cart contents: " + ", ".join(cart))
    else:
        print("Shopping cart is empty")

# Function to checkout 
def clearCart(cart) : 
    # .clear empties the list
    cart.clear()
    print("Shopping cart is now empty")

# Function to Checkout 
def checkout(cart) : 
    print("Thank you for shopping with us.")
    # Print out items in the cart
    viewCart(cart)
    # TODO: process the order
    clearCart(cart)


def main():
    # Build the menu for our shopping cart program
    print("Hello, welcome to my shiopping program:")

    # Create a list to hold our shopping cart items
    shoppingCart = []

    while True:
        print("1. Add item to the shopping cart")
        print("2. Remove item from shopping cart")
        print("3. View shopping cart")
        print("4. Clear shopping cart")
        print("5. Checkout")

        # Ask the user which option they want to pick 
        userInput = input("Please choose an option from the menue or 'quit' to leave: ")

        if userInput.lower() == "quit" : 
            break
        elif userInput == "1" : 
            # Get user input
            itemToAdd = input("Enter an item to add to the cart: ")
            # Add item to cart
            shoppingCart = addItem(shoppingCart, itemToAdd)

        elif userInput == "2" : 
            # Get user input
            itemToRemove = input("Enter an item to remove to the cart: ")
            # Remove item from cart
            shoppingCart = removeItem(shoppingCart, itemToRemove)
            
        elif userInput == "3" : 
            # View cart
            viewCart(shoppingCart)

        elif userInput == "4" : 
            # Clear cart
            clearCart(shoppingCart)

        elif userInput == "5" : 
            # Checkout
            checkout(shoppingCart)
            # Leave the loop
            break
    

# If this script (.py file) is run directly, the value of __name__ will be__ main
if __name__ == "__main__" :
    main()