from Product import Product

class ProductDecorator:
    def __init__(self, product):
        self.product = product

    def get_name(self):
        return self.product.get_name()

    def get_price(self):
        return self.product.get_price()

    def get_quantity(self):
        return self.product.get_quantity()

    def get_category(self):
        return self.product.get_category()

    def get_description(self):
        return self.product.get_description()

    def get_features(self):
        return ""

