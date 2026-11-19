import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory
from orders import Order
from discounts import BulkDiscount, PercentageDiscount, StudentDiscount

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)

            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError("Expected 5 columns")

                    product_type, product_id, name, price, stock = [
                        item.strip() for item in row
                    ]

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price),
                        int(stock),
                        supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")

def main():
    supplier = Supplier("S001", "Office Supplies", "sales@example.com")
    inventory = Inventory()

    load_products("products.csv", inventory, supplier)

    inventory.display_all()

    lamp = inventory.search_product("P001")

    if lamp:
        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(lamp, 10)

        print("Bulk total:", order.calculate_total())

        order.set_discount(PercentageDiscount(10))
        print("Percentage total:", order.calculate_total())

        order.set_discount(StudentDiscount())
        print("Student total:", order.calculate_total())

if __name__ == "__main__":
    main()