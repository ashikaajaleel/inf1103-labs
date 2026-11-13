from products import Product

class OrderLine: 
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines = list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total

    def display_order_details(self) -> None:
        print(f"Order ID: {self.__order_id}")
        for order_line in self.__order_lines:
            product = order_line.get_product()
            quantity = order_line.get_quantity()
            subtotal = order_line.calculate_subtotal()
            print(f"Product: {product.get_name()} | Quantity: {quantity} | Subtotal: ${subtotal:.2f}")
        print(f"Total Amount: ${self.calculate_total():.2f}")