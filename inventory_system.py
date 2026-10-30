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



