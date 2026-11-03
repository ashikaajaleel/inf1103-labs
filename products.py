#manage 1 product information
class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("There are no stocks here, no changes are made.")
            return
        self.__stock = quantity

    def display_information(self):
        print(f"{self.__product_id} | {self.__name} | ${self.__price:.2f} | {self.__stock}")


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)  #parent class product
        self.__weight = weight                            #child class physical product

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)  #parent class product
        self.__file_size = file_size                      #child class digital product

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.__file_size} MB")