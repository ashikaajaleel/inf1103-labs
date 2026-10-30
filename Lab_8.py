import json
INVENTORY_FILE = "inventory.json"

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

class Inventory:
    def __init__(self):
        self.__product = [] #list to hold all product history

    def add_product(self,add_product):
        self.__product.append(add_product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty")
            return
        for product in self.__products:
            product.display_information()

    def get_all_product(self):
        return self.__products


def save_inventory(inventory, transaction_history):
    data = []

    for product in inventory.get_all_products():
        data.append({
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open("inventory.txt", "w") as f:
        json.dump(data,f,indent=4)
    print("Inventory saved successfully!")

def load_inventory():
    inventory = []
    try:
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)

    for item in data:
        product = Product(item["product_id"], item["name"], item["price"], item["stock"])
        inventory.add_product(product)

def main():
    inventory = Inventory()
    ID = 1000
    load_inventory(Inventory)


    while True:
        print("\n========================================\nINVENTORY MANAGEMENT SYSTEM\n========================================")
        print("1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == 1, 
            




main()