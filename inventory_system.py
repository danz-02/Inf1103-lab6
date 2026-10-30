import os
import json

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


