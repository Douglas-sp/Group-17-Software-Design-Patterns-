from ProductDecorator import ProductDecorator


class ExpressShippingProduct(ProductDecorator):
    def get_features(self):
        return "Express shipping"

    def get_price(self):
        return self.product.get_price() + 15000
