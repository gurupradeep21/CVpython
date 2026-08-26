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

class user:
    def __init__(self,age):
        if(age>18):
            self.age=age
        else:
            print("not eligible")
obj=user(20)
print(obj.age)




