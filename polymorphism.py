#5
class Payment:
    def __init__(self,amount):
        self.amount=amount
    def process(self):
        print("Processing")
class CreditCard(Payment):
    def process(self):
        print("credit card payment Rs.",self.amount)
class UPI(Payment):
    def process(self):
        print("UpI payment of Rs.",self.amount)
class NetBanking(Payment):
    def process(self):
        print("Net banking payment of Rs.",self.amount)
def checkout(payment):
    payment.process()

obj1=CreditCard(1000)
obj2=UPI(2000)
obj3=NetBanking(500)

checkout(obj1)
checkout(obj2)
checkout(obj3)

#6
class PDFReport:
    def send(self):
        print("Sending PDF Report")
class ExcelSheet:
    def send(self):
        print("Sending Excel Sheet")
class EmailMessage:
    def send(self):
        print("Sending Email Message")

def dispatch(item):
    item.send()

pdf = PDFReport()
excel = ExcelSheet()
email = EmailMessage()

dispatch(pdf)
dispatch(excel)
dispatch(email)