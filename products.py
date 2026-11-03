from abc import ABC, abstractmethod

class Product(ABC):
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

    @abstractmethod
    def get_fulfilment_info(self):
        pass

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)  #parent class product
        self.__weight = weight                            #child class physical product

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5  # Example shipping cost calculation based on weight

    def get_weight(self):
        return self.__weight

    def get_type(self):
        return "physical"

class DigitalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)  #parent class product
        self.__download_size = download_size       #child class digital product

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."

    def get_download_size(self):
        return self.__download_size

    def get_type(self):
        return "digital"