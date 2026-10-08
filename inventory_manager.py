import json

INVENTORY_FILE = "inventory.txt"

def load_inventory():
    inventory = 0
    transaction_history = []
    try:
        with open(INVENTORY_FILE, "r") as f:
            first_line = f.readline().strip()
            if first_line:
                inventory = int(first_line)
            for line in f:
                line = line.strip()
                if line:
                    order_number, order_name, stock_quantity = line.split("  ")
                    transaction_history.append(
                        (int(order_number), order_name, int(stock_quantity))
                    )
    except FileNotFoundError:
        print("\nInventory file not found. Starting with empty inventory.")
    return inventory, transaction_history
    
def calculate_tax(amount):
    return amount * 0.1

def add_product():
    order_name = input("\nEnter the order name: ")
    if order_name.lower() == 'quit':
        return 'quit', 'quit'
    else:
        stock_quantity = input("\nEnter the stock quantity: ")
        if stock_quantity.isdigit():
            return order_name, int(stock_quantity)
        else:
            return 'nill', 'invalid'

def update_stock(inventory):
    product_id = input("\nEnter the order name to update: ")
    for product in inventory:
        if product["id"] == product_id:
            print(f'\nProduct Found\n Name:{product['name']}\n Current Stock:{product['stock']}')
            new_stock = input("Enter the new stock quantity: ")
            if new_stock.isdigit():
                return product_id, int(new_stock)
            else:
                print("Invalid stock quantity.")
                return
        product['stock'] = new_stock
    else:
        print("Product not found.")
        return

def display_all(inventory):
    print("\nCurrent Inventory:")
    for product in inventory:
        print(f'ID: {product["id"]} | Name: {product["name"]} | Price: ${product["price"]:.2f} | Stock: {product["stock"]}')

def search_product(inventory):
    product_id = input("\nEnter product ID to search:")
    for product in inventory:
        if product["id"] == product_id:
            print(f'\nProduct Found\n ID: {product["id"]}\n Name: {product["name"]}\n Price: ${product["price"]:.2f}\n Stock: {product["stock"]}')
            return
    else:
        print("Product not found.")


def process_delivery(current_total,new_value):
    new_total = current_total + new_value
    return new_total

def generate_report(total_units, failed_entries):
    print(f"Total Units Processed: {total_units}")
    print(f"Failed Entries: {failed_entries}")

def save_inventory(inventory, transaction_history):
    with open("inventory.txt", "w") as f:
        f.write(str(inventory) + "\n")
        for order in transaction_history:
            f.write(f"{order[0]}  {order[1]}  {order[2]}\n")

def main():
    inventory = 0
    failed_entries = 0
    transaction_history = []
    order_number = 1000

    #load inventory and transaction history from file
    inventory, transaction_history = load_inventory()
    if transaction_history:
        order_number = transaction_history[-1][0]

    while True:
        #get order name and stock quantity from user input
        order_name, stock_quantity = add_product()
        if order_name == 'quit' :
            save_inventory(inventory, transaction_history)
            print("Order successfully saved to inventory.txt")
            break
        elif stock_quantity == 'invalid':
            print("Invalid input. Please enter a valid stock quantity or type 'quit' to exit.")
            failed_entries += 1
        else:
            #save the order to transaction history and update inventory
            inventory = process_delivery(inventory, stock_quantity)
            tax = calculate_tax(stock_quantity)
            order_number += 1
            transaction_history.append((order_number, order_name, stock_quantity))    
            print("Current Orders:")

            #print the current orders in transaction history
            for order in transaction_history:
                print(f"{order[0]}  {order[1]}  {order[2]}")

        if inventory >= 500:
            print("Inventory limit reached. Stopping further processing.")
            generate_report(inventory, failed_entries)
            save_inventory(inventory, transaction_history)
            print("Order successfully saved to inventory.txt")
            break
main()