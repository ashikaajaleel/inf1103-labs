from products import Product


class Inventory:
    def __init__(self):
        self.__products: list[Product] = [] #list to hold all product history

    def add_product(self,add_product: Product) -> Product | None:
        self.__products.append(add_product)
        return add_product

    def search_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def remove_product(self, product_id: str):
        product = self.search_product(product_id)
        if product:
            self.__products.remove(product)
            print(f"Product {product_id} removed successfully.")
        else:
            print(f"Product {product_id} not found in inventory.")

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty")
            return
        for product in self.__products:
            product.display_information()

    def get_all_products(self):
        return self.__products