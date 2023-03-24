from Product import Product

class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price,size)
        self.size = size
    
    def get_size(self):
        return self.size



