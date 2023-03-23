import Product
import Payment
import Receipt
import ShopAttendant
import Order

# create some products
product1 = Product("Shirt", 20.0, 10, "Clothing", "A nice shirt")
product2 = Product("Pants", 30.0, 15, "Clothing", "Some nice pants")
product3 = Product("Shoes", 50.0, 5, "Footwear", "Some nice shoes")

# create an order
order1 = Order(1, [product1, product2], "2023-03-23")

# create a payment
payment1 = Payment(1, "credit card", order1.getTotalAmount(), "2023-03-23")

# create a receipt
receipt1 = Receipt(1, order1.getProductList(), payment1.amountPaid,
                   payment1.paymentType, payment1.paymentDate)

# create a shop attendant
attendant1 = ShopAttendant("John", 1, "john@example.com", "123-456-7890")

# add a product to the inventory
attendant1.addProduct(product3)

# remove a product from the inventory
attendant1.removeProduct(product2)

# update a product in the inventory
attendant1.updateProduct(product1, 25.0, 5)

# process an order
attendant1.processOrder(order1)

# generate a receipt
attendant1.generateReceipt(receipt1)
