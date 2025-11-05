from abc import abstractmethod,ABC

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass


class CreditCardPayment(Payment):
    def pay(self,amount):
        print("this is class Credit Card Payment ")


class PayPalPayment(Payment):
     def pay(self,amount):
        print("this is class PayPal Payment")


class CryptoPayment(Payment):
    def pay(self,amount):
        print("this is class Crypto Payment")

