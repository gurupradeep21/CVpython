# from abc import ABC, abstractmethod
#
# class Whatsapp(ABC):
#     @abstractmethod
#     def send(self):
#         pass
#
# class SendPhoto(Whatsapp):
#     def send(self):
#         print("Compressing the photo...")
#         print("Encrypting Photo...")
#         print("Sending the photo...")
#         print("Decrypting the photo...")
#         print("Photo sent!")
#
# class SendText(Whatsapp):
#     def send(self):
#         print("Checking character limit..")
#         print("Encrypting the message...")
#         print("Sending the message..")
#         print("Decrypting the message...")
#         print("Message sent!!")
#
# message1 = SendText()
# image1 = SendPhoto()
# message1.send()
# image1.send()

# from abc import ABC, abstractmethod
#
# class PaymentGateway(ABC):
#     @abstractmethod
#     def initiate(self, amount):
#         pass
#     @abstractmethod
#     def verify(self, transaction_id):
#         pass
#     @abstractmethod
#     def refund(self, transaction_id):
#         pass
#
# class Razorpay(PaymentGateway):
#     def initiate(self, amount):
#         print("Razorpay payment initiated:", amount)
#     def verify(self, transaction_id):
#         print("Razorpay transaction verified:", transaction_id)
#     def refund(self, transaction_id):
#         print("Razorpay refund:", transaction_id)
#
# class PayPal(PaymentGateway):
#     def initiate(self, amount):
#         print("PayPal payment initiated:", amount)
#     def verify(self, transaction_id):
#         print("PayPal transaction verified:", transaction_id)
#     def refund(self, transaction_id):
#         print("PayPal refund:", transaction_id)
#
# r = Razorpay()
# r.initiate(500)
# r.verify("R123")
# r.refund("R123")

# p = PaymentGateway()   # TypeError: Cannot instantiate abstract class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def move(self):
        pass

    def breathe(self):
        print("Animal is breathing")

class Dog(Animal):
    def speak(self):
        print("Dog says Woof")
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def speak(self):
        print("Bird says Chirp")
    def move(self):
        print("Bird is flying")

class Fish(Animal):
    def speak(self):
        print("Fish makes sounds")
    def move(self):
        print("Fish is swimming")

d = Dog()
d.speak()
d.move()
d.breathe()

# a = Animal()       # TypeError

# class Cat(Animal):
#     def move(self):
#         print("Cat is moving")
#
# c = Cat()           # TypeError because speak() is missing