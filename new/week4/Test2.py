from Cart import Cart
from BarcodeScanner import BarcodeScanner

# creating a cart and a barcode scanner
cart = Cart()
scanner = BarcodeScanner(cart)

# registering the cart as an observer of the barcode scanner
scanner.subject.register_observer(cart)


