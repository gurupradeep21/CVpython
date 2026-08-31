# class A:
#     pass
# obj1=A()
# print(type(obj1))
# obj2=A()
# print(id(obj1))
# print(id(obj2))

# class A:
#     a=20
# obj=A()
# print(A.a)

# class Phone:
#     software = 'Android'
#     count=0
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#         Phone.count+=1
# phone1=Phone('Samsung','1000000')
# phone2=Phone('pixel','60000')
# print(phone1.price)
# print(phone1.brand)
# print(phone2.price)
# print(phone2.brand)
# print(Phone.count)

# class A:
#     x=40
#     def __init__(self,y):
#         self.y=y
# obj=A(40) #instance variable #legb
# print(obj.y)

# def outer():
#     x=20
#     def inner():
#         x=40
#         print(x)

# class A:
#     x=40
#     def __init__(self,y):
#         """hello py-20"""
#         self.y=y
# obj1=A("hey") #instance variable #legb
#
# #print(obj.y)
# print(A.__dict__)
# print(obj1.__dict__)

# class A:
#     x=40
#     def __init__(self,y):
#         self.y=y
# obj1=A("hey")
# obj2=A("hi")
# obj3=A("hello")
# obj1.x=100
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
#
# obj2.__dict__['z']=40 ----
# print(obj2.__dict__)

# class computer:
#     def __init__(self,cpu,ram):
#             self.cpu=cpu
#             self.ram=ram
#             print(self.cpu,self.ram)
#
#     def config(self):
#         print("i5")
#
# obj=computer("i5","8gb")
# obj.config()

# class Phone:
#     software = 'Android'
#     count=0
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#         Phone.count+=1
# phone1=Phone('Samsung','1000000')
# phone2=Phone('pixel','60000')
# print(phone1.price)
# print(phone1.brand)
# print(phone2.price)
# print(phone2.brand)
# print(Phone.count)

# class student:
#     count=0
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#         student.count+=1
# obj=student("pradeep",22,10)
# obj1=student("balaji",22,1)
# obj3=student("pavan",22,3)
# # print(obj.name)
# # print(obj.age)
# # print(obj.rollno)
# print(student.count)

# class user:
#     def __init__(self,age):
#         if(age>18):
#             self.age=age
#         else:
#             print("not eligible")
# obj=user(20)
# print(obj.age)

class BankAccount():
    bank_name="ABC Bank"
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        if(balance<0):
            self.balance=0
        else:
            self.balance=balance
    def display(self):
        print("Bank Name: ",BankAccount.bank_name)
        print("Account Holder: ",self.account_holder)
        print("account number: ",self.account_number)
        print("Balance: ",self.balance)

acc1=BankAccount("pradeep",12351647,100000)
acc2=BankAccount("balaji",9786747,-4000)
acc1.display()
acc2.display()


# def display(obj):
#     print(obj.__dict__)

#2

# class Student():
#     college="ABC College"
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         if(marks >=0 and marks <=100):
#             self.mraks=marks
#         else:
#             self.marks=0
# s1=Student("Alice",123,34)
# s2=Student("Bob",124,-94)
# s3=Student("Alice",125,10)
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)

#3
# class Product():
#     products=[]
#     store_name = "ABC Store"
#     def __init__(self,name,price,quantity):
#         self.name=name
#         if(price > 0 and quantity>0):
#             self.price=price
#             self.quantity=quantity
#         else:
#             print("Invalid price or quantity")
#         Product.products.append(name)
# p1=Product("Laptop",10000,2)
# p2=Product("Mouse",100,-2)
# p3=Product("Ps5",10000,2)
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
# print(Product.products)



#1
#A company wants to generate basic salary information when employee objects are created.
# Create a class Employee with class variables company = "TechCorp" and employee_count = 0.
# The constructor should accept name, department, salary, and experience.
# Validate that salary and experience are not negative.
# Based on experience, calculate a bonus inside the constructor: employees with more than 5 years receive 15%,
# employees with 3–5 years receive 10%, and employees with less than 3 years receive 5%.
# Create an instance dictionary pay_details containing the employee’s name, salary, experience, bonus, and final salary.
# Generate an employee ID using employee_count. Create three employee objects and display their _dict_.

class Employee():
    company="TechCorp"
    employee_count=0
    def __init__(self,name,department,salary,experience):
        self.name=name
        self.department=department

        if(salary>0 and experience>0):
            self.salary = salary
            self.experience = experience
            if (experience > 5):
                bonus = (salary * 0.15)
            elif (experience >= 3 and experience <= 5):
                bonus = (salary * 0.1)
            else:
                bonus = (salary * 0.05)
            final_salary = salary + bonus
            Employee.employee_count += 1
            self.employee_id = self.employee_count

            self.pay_details = {
                "employee;s name": name,
                "salary": salary,
                "experience": experience,
                "bonus": bonus,
                "final_salary": final_salary
            }
        else:
            print("Invalid salary or experience")

emp1=Employee("pradeep","Developer",1000000,6)
emp2=Employee("pavan","Testing",70000,2)
emp3=Employee("balaji","sales",60000,4)
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(emp3.__dict__)
print(emp1.pay_details)
print(emp2.pay_details)
print(emp3.pay_details)

#2
#A mobile store creates a purchase object whenever a customer buys a phone.
# Create a class MobilePurchase with a class variable store_name = "Smart Mobiles" and purchase_count = 0.
# The constructor should accept customer, brand, price, storage, and quantity.
# Validate that price and quantity are positive and that storage is either 64, 128, 256, or 512 GB.
# Calculate the total price inside the constructor.
# If the total exceeds ₹50,000, apply a 10% discount; otherwise, apply a 5% discount.
# Store the complete purchase information in a dictionary called purchase_details.
# Increment purchase_count for every valid purchase. Create three objects and display their _dict_.

class MobilePurchase():
    store_name = "Smart Mobiles"
    purchase_count=0
    def __init__(self,customer, brand,price, storage,quantity):
        self.customer=customer
        self.brand=brand
        if(price>0 and quantity>0 and (storage==64 or storage==128 or storage==256 or storage==512)):
            self.price=price
            self.quantity=quantity
            self.storage=storage
            if(price>50000):
                discount=price*0.1
            else:
                discount=price*0.05
            final_price=price-discount
            MobilePurchase.purchase_count+=1

            self.purchase_details={"customer":customer,
                                   "Brand":brand,
                                   "Price":price,
                                   "Storage":storage,
                                   "Quantity":quantity,
                                   "Discount":discount,
                                   "Final Price":quantity * final_price
                          }
        else:
            print("Invalid price or quantity or storage")
p1=MobilePurchase("pradeep","poco",14000,100,1)
p2=MobilePurchase("balaji","moto",60000,256,1)
p3=MobilePurchase("pavan","samsung",24000,128,1)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

#3
#Create a class Product with a class variable store = "ShopEasy".
#The constructor should accept name, price, and quantity and
# create an instance dictionary product_details containing the product name, price, quantity, and the calculated total price.
# Create two Product objects. After creating the objects, change the price of the first product using its instance variable.
# Then change the price stored inside the product_details dictionary of the first product.
# Display the __dict__ of the first product and explain why the two price values can be different.

class Product:
    store = "ShopEasy"

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.product_details = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total_price": price * quantity
        }


p1 = Product("Laptop", 50000, 2)
p2 = Product("Mouse", 1000, 3)

p1.price = 55000
p1.product_details["price"] = 60000
print(p1.__dict__)