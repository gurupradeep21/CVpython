# --------------- 06-07-26-----------------------



'''def calculate_bill(price,quantity):
    total = price * quantity
    if total < 200:
        print("adding 40rs small cart fee...")
        return total + 40
    return total
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = calculate_bill(price,quantity)
print(total)
'''
#-----------------------------------------------------------------------------------------

'''def total(subject1, subject2, subject3):
    return subject1 + subject2 + subject3
def avg(total):
    return total // 3
def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 65:
        return "C"
    elif avg >= 50:
        return "D"
    return "Fail"
total=total(70,50,80)
average=avg(total)
print(grade(average))
'''
#---------------------------------------------------------------

'''def deposit(amount, current_balance):
    if amount > 0:
        return current_balance + amount
    return "Please enter a valid amount"
def withdraw(amount, current_balance):
    if amount > current_balance:
        return "Insufficient funds"
    return current_balance - amount
balance =int(input("Enter your balance: "))
final_balance = deposit(1000,balance)
print(withdraw(20000,balance))      # incommplete
'''

#--------------------------------------------------------------

#positional arguements
'''def learn(name, skill):
    print(name," is learning", skill)
#learn(goutham,"sql")
#learn("sql","goutham")

#key word argumennts
learn(skill="sql", name="goutham")
'''
#  --------------------------------------------------------------
'''def objective(name,strength1,strength2,strength3):
    print("My name is",name,"My strength1 is",strength1,"My strength2 is",strength2,"My strength3 is ",strength3)
objective(strength2="hardworking",strength1="problem solving",strength3="team player",name="pradeep")

'''
#---------------------------------------------------------------------------------------
'''' write a py prog to build a simple uber application that has a function called trip details with parameters
     like driver name,pickup location, drop location, total price . call this function using positional arguments 
     onece and next use keyword arguments
'''


'''
def uber(driver_name,pickup_location,drop_location,total_price):
    print(driver_name,pickup_location,drop_location,total_price)
print(uber("Pradeep","Kphb","Nexus",30))

'''
#-------------------------------------------------------------------------------------------------
             #practice q's--Sec 3: Positional Arguments
#1.
'''
def intro(name, city, hobby):
    print(name,city,hobby)
intro("Pradeep","Kukatpally","Playing_cricket")
intro("Kukatpally","Playing_cricket","Pradeep")

#Pradeep Kukatpally Playing_cricket
#Kukatpally Playing_cricket Pradeep
'''

#2.
'''
def subtract(a,b):
    return a-b
print(subtract(10,3))
print(subtract(3,10))

# 7
#-7
'''

#3. Positional in positional arguments means we need to pass arguments
#    as same order as paramters are defined.py matches them based on their position

#4.
'''
def bio(first_name,last_name,age):
    print(first_name,last_name,age)
bio("Guru","Pradeep",22)

#Guru Pradeep 22
'''

#5.
'''
def bio(first_name,last_name,age):
    print(first_name,last_name,age)
bio("Guru","Pradeep",22,"India")
#TypeError: bio() takes 3 positional arguments but 4 were given
'''
#------------------------------------------------------------------
           #pq's-Sec 4: Keyword Arguments
#q1.
'''
def send_email(to, subject, body):
    print(to,subject,body)
send_email(to=" Balaji",body="balaji how are u!",subject="req")
'''
#2.
'''
def create_profile(username,email,age):
    print(username,email,age)
create_profile(username="Guru_Pradeep",email="gurupradeepc@gmail.com",age=22)
'''

#3.
'''
def create_profile(username,email,age):
    print(username,email,age)
create_profile(username="Guru_Pradeep",email="gurupradeepc@gmail.com",22)

# O/P: SyntaxError: positional argument follows keyword argument
'''

#4.

#5. keyword arguments are more readable why because we pass values to the parameters
#   names. making easy to know which value is assinged for which parameter
'''
def create_profile(username,email,age):
    print(username,email,age)
create_profile(age=22,username="Guru_Pradeep",email="gurupradeepc@gmail.com")
'''
'''
def trip_details(driver_name,pickup_location,drop_location,total_price):
    print("Your driver's name is ",driver_name)
    print("From ",pickup_location)
    print("To ",drop_location)
    print("Fare", total_price)
trip_details("Pradeep","kphb","Hi tech city", 120)
trip_details("150","kphb","Hi tech city", "pradeep")
trip_details(total_price=150,drop_location="Hi tech city",pickup_location="kphb",driver_name="pradeep")
'''
#----------------------------------------------------------------------
                            #SEC 5: Default Arguments
#1.
'''
def power(base,exponent=2):
    return base**exponent     
print(power(2))
print(power(3,3))                   

O/P: 4
     27
'''

#2.
'''
def connect(host,port=3306,protocal='TCP'):
    print(host,port,protocal)
connect("localhost")
connect("localhost",5000,"udp")

O/P: localhost 3306 TCP
     localhost 5000 udp

'''

#3.
'''
def func(name='Guest', age):
    print(name,age)
func(name,age)

# SyntaxError: parameter without a default follows parameter with a default
'''

'''
def func(age,name='Guest'):
    print(name,age)
func(22)

#O/P:   Guest 22
'''

#4.
'''
def discount_price(price, discount=10):
    discounted_price = price*(discount/100)
    final_price = price - discounted_price
    return final_price
print(discount_price(1000,50))
print(discount_price(1000))
 
 O/P: 500.0
      900.0

'''

#5. A default parameter is used because it provides a default value
#   while still allowing the caller to change that value when needed.

#----------------------------------------------------------------------------------------------
                           #    Arbitary arguments

# def add(*args):
#     print(args)
# add(10,20,30)


# def add(*l):
#     sum=0
#     for i in l:
#         sum+=i
#     print(sum)
# add(10,20,30)
# add(10,20,30,40,50)

#---------------------------------------------

# def multiply(*args):
#     prod=1
#     for i in args:
#         prod=prod*i
#     print(prod)
# multiply(1,2,3)

#---------------------------------------------

def emp_details(**kwargs):
    print(kwargs)
emp_details(emp_name="jude",
            emp_id=2210,
            emp_salary=1000000)
emp_details(emp_id=20302,
            emp_salary=1000000,
            emp_name="Alice",
            emp_designation="HR Excwl",
            emp_department="Software Engineer")


#Q. Create a python application to develop a simple hospital billing system, design functions like calculate bill with positional args of variable or arbitrary type
# another function Insurance with keyword args of variable or arbitrary type and create function add_taxes with kwargs of var or arbitrary type The program should accept multiple charges like consultation ,test, etc .Apply insurance reduction and add tax
'''
def calculate_bill(*bill):
    total_bill=0
    for i in bill:
        total_bill+=i
    return total_bill
def apply_insurance(amount,**insurance):
    total_claim=0
    for key,value in insurance.items():
        print(key,":",value)
        total_claim+=value
    return amount-total_claim
def calculate_taxes(amount,**tax):
    total_tax=0
    for key,value in tax:
        print(key,":",value)
    return amount-total_tax
total_bill=calculate_bill(1500,2000,20000)
total_bill=apply_insurance(total_bill, "LIC=1000","star"==4500)
print(calculate_taxes(total_bill,"SGST"=100,"GST"=200))
'''


# Create a python application to design a funstion for a food delivery application where the customer name taken as positional arguments the order type is default arg default value is regular, the function should accept multiple food items orderd by the customer using postional args and additional details such as address, payment mode ,delivery instructions, using keyword arguments the function should display complete details using customer details,list of items orderd, total no of items and all additional info
#positional,def, *positional, **kwargs
# def swiggy(customer_name, order_type= "regular", *items, **customer_details):
#     print("Hi", customer_name)
#     print("Your order type is:",order_type)
#     print("Your cart:")
#     total_bill=0
#     for item in items:
#         print(item[0], ":", item[1])
#         total_bill+=item[1]
#     print("Total items in cart:", len(items))
#     print("Your total bill: Rs.", total_bill)
#     print("Additional details:")
#     for detail, description in customer_details.items():
#         print(detail, ":",  description)
# swiggy("balaji", "swiggy one",["burger", 250],["fries", 60],["coke",40],
#        payment_mode="UPI",
#        delivery_instructions="Don't Ring the bell",
#        cultery=" yes, provide cultery")