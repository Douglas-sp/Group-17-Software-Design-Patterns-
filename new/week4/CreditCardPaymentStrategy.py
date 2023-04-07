from PaymentStrategy import PaymentStrategy

class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paid {amount} dollars using credit card {self.card_number}.")

