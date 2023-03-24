from Product import Product

class ClothingProduct(Product):
    def __init__(self, name, price, quantity, category, description):
        super().__init__(name, price, quantity, category, description)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description
    
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_category(self):
        return self.category

    def get_description(self):
        return self.description



