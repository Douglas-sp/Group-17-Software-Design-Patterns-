from PaymentStrategy import PaymentStrategy

class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} dollars in cash.")
