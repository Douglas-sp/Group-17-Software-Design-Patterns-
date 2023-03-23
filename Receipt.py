from datetime import date


class Receipt:
    def __init__(self, receiptId, productList, totalAmount, paymentType, date):
        self.receiptId = receiptId
        self.productList = productList
        self.totalAmount = totalAmount
        self.paymentType = paymentType
        self.date = date

    def generateReceipt(self):
        # Perform receipt generation logic here
        print("Generating receipt...")

    def getReceiptDetails(self):
        return f"Receipt ID: {self.receiptId}\nProduct List: {self.productList}\nTotal Amount: {self.totalAmount}\nPayment Type: {self.paymentType}\nDate: {self.date}"
