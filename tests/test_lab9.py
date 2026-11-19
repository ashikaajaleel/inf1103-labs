import unittest
from unittest.mock import patch
from io import StringIO
from supplier import Supplier
from inventory import Inventory
from product_factory import ProductFactory
from products import PhysicalProduct, DigitalProduct
from orders import Order
from discounts import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from lab_9 import get_positive_float, load_products

class Lab9Tests(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S", "Supplier", "s@example.com")
        self.product = ProductFactory.create(
            "physical", "P", "Desk", 25, 10, self.supplier
        )

    def test_factory(self):
        self.assertIsInstance(self.product, PhysicalProduct)

        digital = ProductFactory.create(
            "digital", "D", "App", 20, 3, self.supplier
        )
        self.assertIsInstance(digital, DigitalProduct)

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "X", "Service", 10, 2, self.supplier
            )

    def test_validation(self):
        for price, stock in [(0, 1), (-1, 1), (2, -1)]:
            with self.assertRaises(ValueError):
                ProductFactory.create(
                    "physical", "P", "Desk",
                    price, stock, self.supplier
                )

        order = Order("O")

        with self.assertRaises(ValueError):
            order.add_order_line(self.product, 0)

        with self.assertRaises(ValueError):
            self.product.update_stock(-1)

    def test_discounts(self):
        order = Order("O", BulkDiscount(200, 20))
        order.add_order_line(self.product, 10)

        self.assertAlmostEqual(order.calculate_total(), 230)

        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

        order.set_discount(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)

        order.set_discount(NoDiscount())
        self.assertAlmostEqual(order.calculate_total(), 250)

    def test_input_retry(self):
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            with patch("sys.stdout", new_callable=StringIO) as output:
                result = get_positive_float("Price: ")

        self.assertEqual(result, 12.5)
        self.assertIn("valid number", output.getvalue())
        self.assertIn("greater than zero", output.getvalue())

    def test_csv(self):
        inventory = Inventory()

        with patch("sys.stdout", new_callable=StringIO) as output:
            load_products("products.csv", inventory, self.supplier)

        self.assertEqual(len(inventory.get_all_products()), 3)
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Skipping row 4", output.getvalue())
        self.assertIn("Skipping row 5", output.getvalue())

        with patch("sys.stdout", new_callable=StringIO) as output:
            load_products("missing.csv", inventory, self.supplier)

        self.assertIn("Products file not found", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())

if __name__ == "__main__":
    unittest.main()