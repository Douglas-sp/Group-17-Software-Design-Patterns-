import Product


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period
    
    def get_warranty_period(self):
        return self.warranty_period
        


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    
    def get_size(self):
        return self.size


class GroceryProduct(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self.expiry_date = expiry_date
    
    def get_expiry_date(self):
        return self.expiry_date
