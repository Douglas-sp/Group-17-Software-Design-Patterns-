class Product:
    def __init__(self, name, price, quantity, category, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description

    def addProduct(self, name, price, quantity, category, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.description = description

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

    def getProductDetails(self):
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category}\nDescription: {self.description}"
