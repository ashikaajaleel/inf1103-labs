class Inventory:
    def __init__(self):
        self.__products = [] #list to hold all product history

    def add_product(self,add_product):
        self.__products.append(add_product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty")
            return
        for product in self.__products:
            product.display_information()

    def get_all_products(self):
        return self.__products