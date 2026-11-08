import json
INVENTORY_FILE = "inventory_lab7.json"

from products import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory

#file handling functions
def save_inventory(inventory):
    data = []

    for product in inventory.get_all_products():
        item = {
            "type": product.get_type(),
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }

        if product.get_type() == "physical":
            item["weight"] = product.get_weight()
        elif product.get_type() == "digital":
            item["download_size"] = product.get_download_size()
        data.append(item)

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
        if item["type"] == "physical":
            product = PhysicalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["weight"])
        elif item["type"] == "digital":
            product = DigitalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["download_size"])
        else:
            continue 
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
            option  = input(f"Select which type of product you would like to add:\n1. Physical Product\n2. Digital Product\n")
            if option == "1":
                weight = float(input("Weight:  "))
                inventory.add_product(PhysicalProduct(product_id, name, price, stock, weight))
            elif option == "2":
                download_size = int(input("Download Size:  "))
                inventory.add_product(DigitalProduct(product_id, name, price, stock, download_size))
            else:
                print("Invalid option.")
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

if __name__ == "__main__":
    main()