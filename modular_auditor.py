inventory = 0
failed_entries = 0
tax_rate = 0.1

def calculate_tax(amount):
    return amount * tax_rate

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        elif user_input.lower() == 'quit':
            return None
        else:
            print("Invalid input. Please enter a number or 'quit' to exit.")

def process_delivery(current_total,new_total):

def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}")
    print(f"Failed Entries: {failed_entries}")

def main():
    inventory = 0
    tax_amount = 0
    exit_program = False
    while not exit_program:

        
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