from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def update_stock(self, quantity) -> None:
        if quantity < 0:
            print("There are no stocks here, no changes are made.")
            return
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"{self.__product_id} | {self.__name} | ${self.__price:.2f} | {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def get_supplier(self) -> Supplier:
        return self.__supplier

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)  #parent class product
        self.__weight: float = weight                            #child class physical product

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5  # Example shipping cost calculation based on weight

    def get_weight(self) -> float:
        return self.__weight

    def get_type(self) -> str:
        return "physical"

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)  #parent class product
        self.__download_size: float = download_size       #child class digital product

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally."

    def get_download_size(self) -> float:
        return self.__download_size

    def get_type(self) -> str:
        return "digital"