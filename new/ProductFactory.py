from ElectronicProduct import ElectronicProduct
from ClothingProduct import ClothingProduct
from GroceryProduct import GroceryProduct

class ProductFactory:
    def create_electronic_product(self, name, price, quantity, category, description):
        return ElectronicProduct(self, name, price, quantity, category, description)
    
    def create_clothing_product(self, name, price, quantity, category, description):
        return ClothingProduct(name, price, quantity, category, description)
    
    def create_grocery_product(self, name, price, quantity, category, description):
        return GroceryProduct(name, price, quantity, category, description)
