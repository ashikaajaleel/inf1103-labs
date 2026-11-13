import json
INVENTORY_FILE = "inventory_lab8.json"
from products import PhysicalProduct, DigitalProduct
from inventory import Inventory
from supplier import Supplier

#retrieve supplier from the suppliers dictionary or create a new one if it doesn't exist
def get_supplier(suppliers: dict[str, Supplier], supplier_id: str,
                 name: str, email: str) -> Supplier:
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, name, email)
    return suppliers[supplier_id]

#file handling functions
def save_inventory(inventory) -> None:
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

def load_inventory(inventory, suppliers: dict[str, Supplier]) -> None:
    try:
     with open(INVENTORY_FILE, "r") as f:
        data = json.load(f)
    except FileNotFoundError:
        print("Inventory file not found.")
        return

    for item in data:
        supplier = get_supplier(suppliers, item["supplier_id"], item.get("supplier_name", ""), item.get("supplier_email", ""))
        if item["type"] == "physical":
            product = PhysicalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["weight"], supplier=supplier)
        elif item["type"] == "digital":
            product = DigitalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["download_size"], supplier=supplier)
        else:
            continue 
        inventory.add_product(product)


#main function to run the program
def main() -> None:
    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}
    load_inventory(inventory,suppliers)


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
            supplier_id = input("Supplier ID:  ")
            supplier_name = input("Supplier Name:  ")
            supplier_email = input("Supplier Email:  ")
            supplier = get_supplier(suppliers,supplier_id, supplier_name, supplier_email)
            option  = input(f"Select which type of product you would like to add:\n1. Physical Product\n2. Digital Product\n")
            if option == "1":
                weight = float(input("Weight:  "))
                inventory.add_product(PhysicalProduct(product_id, name, price, stock, weight,supplier))
            elif option == "2":
                download_size = int(input("Download Size:  "))
                inventory.add_product(DigitalProduct(product_id, name, price, stock, download_size, supplier))
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