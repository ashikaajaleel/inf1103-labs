import json
INVENTORY_FILE = "inventory.json"

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

#manage a collection of products
class Inventory:
    def __init__(self):
        self.__products = [] #list to hold all product history

    def add_product(self,add_product):
        self.__products.append(add_product)

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

    def get_all_products(self):
        return self.__products


#file handling functions
def save_inventory(inventory):
    data = []

    for product in inventory.get_all_products():
        data.append({
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open(INVENTORY_FILE, "w") as f:
        json.dump(data,f,indent=4)
    print("Inventory saved successfully!")

def load_inventory(inventory):
    try:
     with open(INVENTORY_FILE, "r") as f:
        data = json.load(f)
    except FileNotFoundError:
        print("Inventory file not found.")
        return

        for item in data:
            product = Product(item["product_id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)


#main function to run the program
def main():
    inventory = Inventory()
    load_inventory(inventory)


    while True:
        print("\n========================================\nINVENTORY MANAGEMENT SYSTEM\n========================================")
        print("1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter ID: ")
            name = input("Name:  ")
            price = float(input("Price:  "))
            stock = int(input("Stock:  "))
            inventory.add_product(Product(product_id, name, price, stock))
            print("Product added, yay!")

        elif choice == "3":
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                updated_stock = int(input("Enter New Stock: "))
                product.update_stock(updated_stock)
                print("Stock updated.")

        elif choice == "4":
            search_product = input("Enter Product ID:  ")
            product = inventory.search_product(search_product)
            if product is None:
                print("Product is not found.")
            else:
                product.display_information()

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("Goodbye, have a nice day!")
            break
        else:
            print("Invalid Option, enter a valid option.")

main()