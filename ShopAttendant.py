import Product

class ShopAttendant:
    def __init__(self, name, id, email, phone):
        self.name = name
        self.id = id
        self.email = email
        self.phone = phone


    def addProduct(name, price, quantity, category, description):
        name = name
        price = price
        quantity = quantity
        category = category
        description = description
        return name

    def removeProduct(self):
        self.name = None
        self.price = None
        self.quantity = None
        self.category = None
        self.description = None
        

    def updateProduct(self, name, price, quantity, category, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description

    def processOrder(self, order):
        # process the order
        order.processOrder()
        print("Order processed successfully.")

    def generateReceipt(self, receipt):
        # generate the receipt
        receipt.generateReceipt()
        print("Receipt generated successfully.")

    # print(addProduct("Henry", 12, "EMIAL@GMAIL", "0784344343", "CLOSS"))
    removeProduct()
    # print(addProduct("Henry", 12, "EMIAL@GMAIL", "0784344343", "CLOSS"))
  


    # def addProduct(self, product):
    #     # add product to inventory
    #     print(f"Product {product.name} added to inventory.")

    # def removeProduct(self, product):
    #     # remove product from inventory
    #     print(f"Product {product.name} removed from inventory.")

    # def updateProduct(self, product, newPrice, newQuantity):
    #     # update product price and quantity in inventory
    #     product.price = newPrice
    #     product.quantity = newQuantity
    #     print(f"Product {product.name} updated in inventory.")

   