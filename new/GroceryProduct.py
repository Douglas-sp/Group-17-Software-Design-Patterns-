from Product import Product
class GroceryProduct(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price,expiry_date)
        self.expiry_date = expiry_date
    
    def get_expiry_date(self):
        return self.expiry_date
