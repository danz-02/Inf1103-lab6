import os
import json

def display_all():

    print("--------MENU--------")
    
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

    print("--------------------")


class Product:

    def __init__(self, id: str, name: str, price: float, stock_quantity: int):

        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    def get_id(self):
        return (self.__id)


    def get_name(self):
        return (self.__name)

    def get_price(self):
        return (self.__price)

    def get_stock(self):
        return (self.__stock_quantity)

    def update_stock(self, stock_update):
        self.__stock_quantity = stock_update


    def display_product(self):

        print("------------------")
        print("ID Number: ", self.__id)
        print("Name: ", self.__name)
        print("Price: ", self.__price)
        print("Stock Quantity: ", self.__stock_quantity)
        print("------------------")


class Inventory: 
    
    def __init__(self): 
        self.__product=[]

    def get_products(self):
        return self.__product

    def add_product(self, product):
        product = self.__product.append(product)

    def search_product(self, id):
        for product in self.__product:
            ##'OOP' search product by 'id'
            if product.get_id() == id:
                return product 

    def display(self):
        print("\nCurrent Inventory\n" "--------------------------------------------")
        for product in self.__product:
            print(f"ID: {product.get_id()}, Name: {product.get_name()}, Price: {product.get_price()}, Stock Quantity: {product.get_stock()} ")
        print("--------------------------------------------\n") ##Display 


def load_inventory():
    ##Load previous transaction history
    orders = []
    inventory = Inventory()
    if os.path.exists("inventory.json"):
        try:
            with open("inventory.json", "r") as file:
                orders = json.load(file)
        except json.JSONDecodeError:
            orders=[]
        print("inventory.json found.\n Inventory loaded successfully. ")

    else:
        ##No previous records, will automatically create a new file 
        order=[]
        f=open("inventory.json", "w")
        f.close()

    for item in orders:
        product = Product(item["id"], item["name"], item["price"], item["stock_quantity"])
        inventory.add_product(product)
    return inventory

def save_inventory(inventory):
    ##Append new transactions to "orders.json", using "a" mode
    orders = []

    for product in inventory.get_products():
        orders.append({
            "id": product.get_id(), 
            "name": product.get_name(),
            "price": product.get_price(),
            "stock_quantity": product.get_stock()

        }) 
    
    with open("inventory.json", "w") as file: 
        json.dump(orders, file, indent=4)
    print("Saving file..")

def add_product(inventory):

    print("--------Add product-----------")
    id = str(input("Enter an ID: "))
    name= str(input("Enter a product: "))
    ##Reusing code to prompt user for stock quantity
    price = input("Enter the price: ")
    stock_quantity = int(input("Enter a stock quantity: "))

    inventory.add_product(Product(id, name, price, stock_quantity))

    print("Product added successfully! ")


def update_stock(inventory):

    print("-------Update Stock-----------")
    search_id = input("Enter Product ID: ")

    ##Search for product id then update stock
    product = inventory.search_product(search_id)

    if product is None:
            
        print("Product not Found! ")
        return
 
    print("Product Found! ")
    print("Name: ", product.get_name())
    print("Current Stock: ",product.get_stock())
    new_stock = input("New Stock Quantity: ")
    product.update_stock(int(new_stock))
    ##Update stock

    print("Stock updated successfully! ")
  

def search_product(inventory):

    print("----------Search Product------------")
    search_id = input("Enter Product ID: ")
    ##Search for product id then search for list of stock

    product = inventory.search_product(search_id)

    if product is None:
        print("Product not found")

    else: 
        print("Product Found:")
        product.display_product()

inventory = load_inventory()

while True:

    display_all()
    menu_option = input("Enter your choice: ")

    if menu_option == "1":
        print("Current Inventory: ")
        inventory.display()

    elif menu_option == "2":
        print("Add Product/n")
        add_product(inventory)

    elif menu_option == "3":
        print("Update Product/n")
        update_stock(inventory)

    elif menu_option == "4":
        print("Search Product/n")
        search_product(inventory)

    elif menu_option == "5":
        print("Save Inventory")
        save_inventory(inventory)

    elif menu_option == "6":
        print("Saving inventory before exit...")
        print("Thank you for using Inventory Management System.")
        break
    else:
        print("Invalid choice.. Please try again")
