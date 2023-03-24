from ProductCatalog import ProductCatalog
from ProductFactory import ProductFactory
# Create instances of specific products
product_factory = ProductFactory()

product_1 = product_factory.create_electronic_product("Laptop", 1000, "2 years")
product_2 = product_factory.create_clothing_product("T-Shirt", 20, "M")
product_3 = product_factory.create_grocery_product("Milk", 2, "2023-04-01")

# Add products to the catalog
product_catalog = ProductCatalog()
product_catalog.add_product(product_1)
product_catalog.add_product(product_2)
product_catalog.add_product(product_3)

# Get all products from the catalog
products = product_catalog.get_products()

for product in products:
    print(product.get_name(), product.get_price())
