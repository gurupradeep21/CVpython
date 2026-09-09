class A:
    def m1(self):
        print("hi")
        print(self)
obj1=A()
obj1.m1()
print(obj1)
obj2=A()
obj2.m1()
print(obj2)


class Bank:
    def __init__(self,acc_no,pin,balance):
        self.acc_no = acc_no
        self.pin = pin
        if(balance>0):
            self.balance = balance
        else:
            print("Invalid Balance, balance should be positive")
    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
            print(self.balance)
        else:
            print("Invalid Deposit")
    def withdraw(self,amount,pin):
        if(self.pin==pin):
            if(self.balance>=amount and amount>0):
                self.balance-=amount
                print(self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
    def check_balance(self):
        print(self.balance)

b1 = Bank(125667,1234,500)
b1.deposit(200)
b1.withdraw(300,1234)
b1.check_balance()


        


