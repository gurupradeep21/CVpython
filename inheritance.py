# 1. Bank Management System Create a Bank class with:
# • balance variable
# • deposit()
# • withdraw()
# • check_balance()
# Create a User class that inherits Bank and displays the user's name.
# Perform deposit, withdrawal, and balance check.
# class Bank:
#     balance=1000
#     def deposit(self,amt):
#         self.balance=self.balance+amt
#         print("Deposited :", amt)
#     def withdraw(self,amt):
#         self.balance=self.balance-amt
#         print("Withdraw amount is:",amt)
#     def check_balance(self):
#         print("Balance :",self.balance)
# class user(Bank):
#     def __init__(self,name):
#         self.name=name
#         print("User name is :",name)
# obj=user("pradeep")
# obj.deposit(1000)
# obj.withdraw(100)
# obj.check_balance()
# obj.deposit(1000)
# obj.check_balance()


# 2. Employee Salary System Create an Employee class with:
# • emp_name
# • salary
# • display_details()
# Create a Manager class that inherits Employee and adds a bonus().
# Display the total salary.

class Employee:
    def __init__(self,emp_name,salary):
        self.emp_name=emp_name
        self.salary=salary
    def display(self):
        print("Employee Name : ", self.emp_name)
        print("Salary :", self.salary)
class manager(Employee):
    def bonus(self):
        self.final_salary=self.salary+50
        print("employee salary after bonus :",self.final_salary)
obj=manager("pradeep",1000)
obj.display()
obj.bonus()


# 3. Student Result System Create a Student class with:
# • Name
# • marks
# • display_marks()
# Create a Result class that inherits Student and calculates whether the student has passed or failed.




# 4. Food Ordering System Using Multilevel Inheritance
# Class 1: Restaurant
# • Create a method menu(item) that returns the price of the selected food item.
# Class 2: FoodCourt (inherits Restaurant) Create the following methods:
# • display_menu() – Display the available food items.
# • order() – Accept the food item from the user and allow multiple orders.
# • billing() – Display the total bill and add a packing charge of ₹20.
# Class 3: Customer (inherits FoodCourt)
# • Create an object of the Customer class.
# • Call the order() method.