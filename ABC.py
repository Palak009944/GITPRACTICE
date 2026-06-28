#Payment Gateway

from abc import ABC, abstractmethod 

class Payment(ABC):
    @abstractmethod    #decorator
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

    def refund(self):
        print("Refund to UPI")

class Credit_Card(Payment):
    def pay(self):
        print("Paid using Credit Card")
    
    def refund(self):
        print("Refund to Credit Card")

U=UPI()
C=Credit_Card()
U.pay()
U.refund()

C.pay()
C.refund()


