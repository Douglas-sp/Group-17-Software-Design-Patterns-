from datetime import date


class Payment:
    def __init__(self, paymentId, paymentType, amountPaid, paymentDate):
        self.paymentId = paymentId
        self.paymentType = paymentType
        self.amountPaid = amountPaid
        self.paymentDate = paymentDate

    def processPayment(self):
        # Perform payment processing logic here
        print("Processing payment...")

    def getPaymentDetails(self):
        return f"Payment ID: {self.paymentId}\nPayment Type: {self.paymentType}\nAmount Paid: {self.amountPaid}\nPayment Date: {self.paymentDate}"

