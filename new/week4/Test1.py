from Cart import Cart
from BarcodeScanner import BarcodeScanner

# create a cart and a barcode scanner
cart = Cart()
scanner = BarcodeScanner(cart)

# register the cart as an observer of the barcode scanner
scanner.subject.register_observer(cart)

# scan some barcodes
scanner.scan("A12B9")
scanner.scan("67DF2")

# get the items in the cart
print(cart.get_items())
