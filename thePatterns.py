from typing import List

# Product class represents a generic product


class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str, description: str):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.category}, {self.price}, {self.quantity}, {self.description}"

# ProductFactory class uses the Factory Method pattern to create different types of products


class ProductFactory:
    def create_product(self, product_type: str, name: str, price: float, quantity: int, description: str) -> Product:
        if product_type == "electronics":
            category = "Electronics"
        elif product_type == "clothing":
            category = "Clothing"
        elif product_type == "groceries":
            category = "Groceries"
        else:
            raise ValueError("Invalid product type")

        return Product(name, price, quantity, category, description)

# ProductCatalogSingleton class uses the Singleton pattern to ensure only one instance of the product catalog is created and accessed throughout the POS system


class ProductCatalogSingleton:
    __instance = None

    def __init__(self):
        if ProductCatalogSingleton.__instance != None:
            raise Exception(
                "You cannot create more than one instance of ProductCatalogSingleton")
        else:
            ProductCatalogSingleton.__instance = self
            self.products = []

    @staticmethod
    def get_instance() -> 'ProductCatalogSingleton':
        if ProductCatalogSingleton.__instance == None:
            ProductCatalogSingleton()
        return ProductCatalogSingleton.__instance

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def get_products(self, category: str = None) -> List[Product]:
        if category:
            return [product for product in self.products if product.category == category]
        else:
            return self.products

# Unit tests for the Factory Method pattern and Singleton
