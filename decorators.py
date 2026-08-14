# def greet():
#     print("Hello")
# say_hello=greet
# say_hello()


# def outer():
#     message='I am the outer function'
#     def inner():
#         print(message)
#     inner()
# outer()


# def make_greeter():
#     def say_hi():
#         print("Hi there")
#     return say_hi
# my_func=make_greeter()
# my_func()

# def intro():
#     print("This is Py-20")
#
# def decorator1(func):
#     def wrapper1():
#         print("HI..!")
#         func()
#     return wrapper1
# intro=decorator1(intro)
# intro()

#1
# def place_order(item):
#     print(f"order placed for {item}")
# def dec(func):
#     def wrapper(*args):
#         print("Function started")
#         func(*args)
#         print("Function ended")
#     return wrapper
# place_order = dec(place_order)
# place_order("Laptop")

#2
# def greet():
#     print("Balaji",end=" ")
# def de2(func):
#     def wr2():
#         print("Hello..!",end=" ")
#         func()
#         print("Have a nice day!")
#     return wr2
# greet = de2(greet)
# greet()

#4
# def start_system():
#     print("Starting System")
# def dec2(func):
#     def wrapp1():
#         func()
#         print("System Started successfully")
#     return wrapp1
# start_system = dec2(start_system)
# start_system()

#5
# def show_msg():
#     print("welcome")
# def dec2(func):
#     def wra3():
#         func()
#         print("Good bye")
#     return wra3
# show_msg = dec2(show_msg)
# show_msg()

#6
# def make_payment():
#     print("Payment initiated")
# def de1(func):
#     def wr2():
#         func()
#         print("Payment Successful")
#     return wr2
# make_payment = de1(make_payment)
# make_payment()

#5  with parameter
# def add(a,b):
#     print(a + b)
# def dec1(func):
#     def wrap1(*args,**kwargs):
#         print("before calling")
#         func(*args,**kwargs)
#         print("After calling")
#     return wrap1
# x=dec1(add)
# x(10,20)

# import functools
# def dec1(func):
#     @functools.wraps(func)
#     def wrapper1(*args,**kwargs):
#         func(*args,**kwargs)
#         print("discount applied")
#     return wrapper1
#
# @dec1
# def apply_discount(price):
#     discount=50
#     price=price-discount
#     print(price)
#
# apply_discount(2500)
# print(apply_discount.__name__)

def verify_user(func):
    def wrapper1(*args,**kwargs):
        func(*args,**kwargs)
        print("User verified")
        
    return wrapper1

def log_transaction(func):
    def wrapper2(*args,**kwargs):
        func(*args,**kwargs)
        print("Transaction logged")
    return wrapper2
