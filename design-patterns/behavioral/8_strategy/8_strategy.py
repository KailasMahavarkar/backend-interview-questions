from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"

class ShoppingCart:
    def __init__(self):
        self.payment_strategy = None
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def checkout(self, amount):
        return self.payment_strategy.pay(amount)

# Usage
cart = ShoppingCart()
cart.set_payment_strategy(CreditCardPayment())
print(cart.checkout(100))

cart.set_payment_strategy(PayPalPayment())
print(cart.checkout(200))