from ProductDecorator import ProductDecorator

class GiftWrappedProduct(ProductDecorator):
    # def __init__(self, product):
    #     super().__init__(product)
    #     # self.description = "Gift wrapped " + self.product.get_description

    def get_features(self):
        return "Gift wrapped"
    def get_price(self):
        return self.product.get_price() + 1500
 