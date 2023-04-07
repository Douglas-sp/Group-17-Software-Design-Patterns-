
class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)