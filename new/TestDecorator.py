from Product import Product
from ProductDecorator import ProductDecorator
from GiftWrappedProduct import GiftWrappedProduct
from ExpressShippingProduct import ExpressShippingProduct


product = Product("Shirt", 29000, 10, "Clothing", "A blue shirt")
gift_wrapped_product = GiftWrappedProduct(product)
express_shipping_product = ExpressShippingProduct(gift_wrapped_product)

print(express_shipping_product.get_name())  # "Shirt"
print(express_shipping_product.get_price())  # 29000
print(express_shipping_product.get_quantity())  # 10
print(express_shipping_product.get_category())  # "Clothing"
print(express_shipping_product.get_description())  # "A blue shirt"
# "Gift wrapped, Express shipping"
print(express_shipping_product.get_features())
