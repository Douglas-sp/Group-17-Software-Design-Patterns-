
class ProductCatalog:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.products = []
        return cls._instance
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product):
        self.products.remove(product)
    
    def get_products(self):
        return self.products
