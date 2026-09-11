inventory = 0
failed_entries = 0

while True:
    stock_quantity = input("Enter the stock quantity: ")
    if stock_quantity.isdigit():
        stock_quantity = int(stock_quantity)
        inventory += stock_quantity
        print(f"current inventory: {inventory}")
        if inventory >= 500:
            print("Inventory limit reached. Stopping input.")
            break
    elif stock_quantity.lower() == 'quit':
        break
    else:
        failed_entries += 1
        print("Invalid input. Please enter a number or 'quit' to exit.")

print(f"Total Units Processed: {inventory}")
print(f"Failed Entries: {failed_entries}")