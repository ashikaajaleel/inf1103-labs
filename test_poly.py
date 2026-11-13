from supplier import Supplier
from products import PhysicalProduct, DigitalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechCorp", "tech@corp.com")

inventory = Inventory()
inventory.add_product(PhysicalProduct("P001", "Guitar", 500.0, 5, 3.5, supplier))
inventory.add_product(DigitalProduct("P002", "Game", 59.9, 100, 4200, supplier))
inventory.add_product(PhysicalProduct("P003", "Piano", 3000.0, 2, 10, supplier))

for product in inventory.get_all_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print()