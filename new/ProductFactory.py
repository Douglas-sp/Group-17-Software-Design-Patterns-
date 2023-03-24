from ElectronicProduct import ElectronicProduct
from ClothingProduct import ClothingProduct
from GroceryProduct import GroceryProduct

class ProductFactory:
    def create_electronic_product(self, name, price, warranty_period):
        return ElectronicProduct(name, price, warranty_period)
    
    def create_clothing_product(self, name, price, size):
        return ClothingProduct(name, price, size)
    
    def create_grocery_product(self, name, price, expiry_date):
        return GroceryProduct(name, price, expiry_date)
