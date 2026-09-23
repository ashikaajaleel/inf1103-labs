
def calculate_tax(amount):
    return amount * 0.1

def get_valid_input():
    stock_quantity = input("Enter the stock quantity: ")
    if stock_quantity.isdigit():
        return int(stock_quantity)
    elif stock_quantity.lower() == 'quit':
        return "quit"
    else:
        return "invalid"

def process_delivery(current_total,new_value):
    new_total = current_total + new_value
    return new_total


def generate_report(total_units, failed_entries):
    print(f"Total Units Processed: {total_units}")
    print(f"Failed Entries: {failed_entries}")

def main():
    inventory = 0
    failed_entries = 0

    while True:
        stock_quantity = get_valid_input()
        if stock_quantity == 'quit' :
            break
        elif stock_quantity == 'invalid':
            print("Invalid input. Please enter a valid stock quantity or type 'quit' to exit.")
            failed_entries += 1
        else:
            inventory = process_delivery(inventory, stock_quantity)
            tax = calculate_tax(stock_quantity)
            print(f"Processed {stock_quantity} units. Current inventory: {inventory}. Tax on this delivery: {tax:.2f}")
            if inventory >= 500:
                print("Inventory limit reached. Stopping further processing.")
                generate_report(inventory, failed_entries)
                break
main()