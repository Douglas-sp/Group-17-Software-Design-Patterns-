from ProductCatalog import ProductCatalog
from Product import Product
from ProductFactory import ProductFactory
# Creating instances of specific products
product_factory = ProductFactory()

product_1 = product_factory.create_electronic_product("Smartphone", 920000, 100, "Electronics", "A high-end smartphone with the latest features.")
product_2 = product_factory.create_clothing_product("T-Shirt", 34000, 50, "Clothing", "A comfortable and stylish t-shirt.")
product_3 = product_factory.create_grocery_product("Milk", 25000, 20, "Groceries", "A carton of fresh milk.")

# Adding products to the catalog
product_catalog = ProductCatalog()
product_catalog.add_product(product_1)
product_catalog.add_product(product_2)
product_catalog.add_product(product_3)

# Getting all products from the catalog
products = product_catalog.get_products()

for product in products:
    #print(product.get_name(), product.get_price(), product.get_quantity(), product.get_category, product.get_description())
    print(product.get_name())
    print(product.get_price())
    print(product.get_quantity())
    print(product.get_category)
    print(product.get_description())
    print("--------------------------------------")

