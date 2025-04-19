# Inventory Management System
import json

# Function to load inventory from file.
def load_Inventory():
    try:
        with open("Inventory.json", "r")as file:
            print("Loading Inventory......")
            return json.load(file)
        # Load inventory from file.

    except FileNotFoundError:
        return {}  #If file doesn't exist, return empty dictionary
    
def save_Inventory():
    with open("Inventory.json","w")as file:
        print("Saving Inventory......")
        json.dump(Inventory, file)
    # save inventory to a file.

# Load inventory when program starts
Inventory = load_Inventory()

def AddProduct(name, quantity):
    if name in Inventory:
        print(f"{name} already exists in Inventory.")
    else: 
        Inventory[name] = quantity
        save_Inventory()
        print(f"{name} added with {quantity} items.")


# Function to update stock of an existing product.
def UpdateStock(name, quantity):
    if name in Inventory:
        Inventory[name] += quantity
        save_Inventory()
        print(f"{quantity} items added to {name}. Total Stock now: {Inventory[name]}")
    else:
        print(f"{name} not found in inventory.")

# Functions to view all products and their roots.
def ViewInventory():
    if not Inventory:
        print("Inventory is empty")
    else:
        for name, quantity in Inventory.items():
            print(f"Product: {name}, Stock: {quantity}")

# Function to delete a product
def DeleteProduct(name):
    if name in Inventory:
        del Inventory[name]
        save_Inventory()
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} not found in Inventory.")


while True:
    print("\nChoose an option.")
    print("1. Add Product")
    print("2. Update Product")
    print("3. View Inventory")
    print("4. Delete Product")
    print("5. Exit")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        P_name = input("Product Name: ")
        P_Quan = int(input("Product Quantity: "))
        AddProduct(P_name,P_Quan)

    elif choice == 2:
        P_name = input("Product Name: ")
        P_Quan = int(input("Product Quantity: "))
        UpdateStock(P_name,P_Quan)

    elif choice == 3:
        ViewInventory()

    elif choice == 4:
        P_name = input("Product Name: ")
        DeleteProduct(P_name)
    
    elif choice == 5:
        break
    else:
        print("Invalid Input")