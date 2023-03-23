from datetime import date


class Order:
    def __init__(self, orderId, productList, date):
        self.orderId = orderId
        self.productList = productList
        self.totalAmount = 0.0
        self.date = date

    def addProduct(self, product):
        self.productList.append(product)
        self.totalAmount += product.price

    def removeProduct(self, product):
        if product in self.productList:
            self.productList.remove(product)
            self.totalAmount -= product.price

    def getTotalAmount(self):
        return self.totalAmount

    def getProductsList(self):
        return self.productList

    def getDate(self):
        return self.date
