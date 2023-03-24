from Product import Product
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price, warranty_period)
        self.warranty_period = warranty_period
    def get_warranty_period(self):
        return self.warranty_period

