from supplier import Supplier
from products import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "TechCorp", "tech@corp.com")
guitar = PhysicalProduct("P001", "Guitar", 500.0, 5, 3.5, supplier)
game = DigitalProduct("P002", "Game", 59.9, 100, 4200, supplier)

print("--- Test 1: one function, both types ---")
show_product_details(guitar)
show_product_details(game)

print("\n--- Test 2: both types in one inventory ---")
inventory = Inventory()
inventory.add_product(guitar)
inventory.add_product(game)
inventory.display_all()

print("\n--- Test 3: normal Product operations on both ---")
inventory.search_product("P001").update_stock(10)
inventory.search_product("P002").update_stock(50)
inventory.display_all()

print("\n--- Test 4: same rule for bad input ---")
guitar.update_stock(-5)
game.update_stock(-5)
print(guitar.get_stock(), game.get_stock())

print("\n--- Test 5: remove ---")
inventory.remove_product("P002")
inventory.display_all()