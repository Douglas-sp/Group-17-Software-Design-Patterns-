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


def test_factory_method():
    factory = ProductFactory()

    # Create an electronics product
    electronics_product = factory.create_product(
        "electronics", "Smartphone", 500.0, 10, "A high-end smartphone")
    assert electronics_product.category == "Electronics"
    assert electronics_product.price == 500.0

    # Create a clothing product
    clothing_product = factory.create_product(
        "clothing", "T-Shirt", 20.0, 50, "A basic cotton t-shirt")
    assert clothing_product.category == "Clothing"
    assert clothing_product.quantity == 50

    # Create a groceries product
    groceries_product = factory.create_product(
        "groceries", "Bananas", 2.0, 100, "A bunch of ripe bananas")
    assert groceries_product.category == "Groceries"
    assert groceries_product.description == "A bunch of ripe bananas"


def test_singleton():
    catalog1 = ProductCatalogSingleton.get_instance()
    catalog2 = ProductCatalogSingleton.get_instance()

    # Make sure there is only one instance of the product catalog
    assert catalog1 is catalog2

    # Add a product to the catalog
    product = Product("Headphones", 50.0, 20, "Electronics",
                      "A pair of noise-cancelling headphones")
    catalog1.add_product(product)

    # Make sure the product is in the catalog
    products = catalog2.get_products("Electronics")
    assert len(products) == 1
    assert products[0].name == "Headphones"
    assert products[0].price == 50.0
