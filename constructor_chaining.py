#multi level
# class A:
#     def __init__(self):
#         print("A Constructor")
# 
# class B(A):
#     def __init__(self):
#         print("B constructor")
#         super().__init__()
# 
# class C(B):
#     def __init__(self):
#         print("C constructor")
#         super().__init__()
# c=C()
# print(C.mro())
# print(B.mro())
# print(A.mro())


#heirarichel inh
# class A:
#     def __init__(self):
#         print("A Constructor")
#
# class B(A):
#     def __init__(self):
#         print("B constructor")
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print("C constructor")
#         super().__init__()
# c=C()
# b=B()

# class A:
#     def __init__(self):
#         print("A Constructor")
#
# class B(A):
#     def __init__(self):
#         print("B constructor")
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print("C constructor")
#         super().__init__()
# class D(B, C):
#     def __init__(self):
#         print("D Constructor")
#         super().__init__()
# d=D()
# print(D.mro())


#------------method chainiing
# class A:
#     def __init__(self):
#         print("A Constructor")
#         super().__init__()
#     def m1(self):
#         print("M1 -A")
#
#
# class B(A):
#     def __init__(self):
#         print("B constructor")
#         super().__init__()
#     def m1(self):
#         print("M1 -B")
#         super().m1()
#
# class C(B):
#     def __init__(self):
#         print("C constructor")
#         super().__init__()
#     def m1(self):
#         print("M1 -C")
#         super().m1()
# c=C()
# c.m1()


#create a class employee with instance variables name and salary.
#create a child class manager that has another instance variable team size

#initialize the variable while creating object of manager clAss

# A company maintains employee information using sepearte class
# 1- an employee classs stores employee_id and name
# 2- attendence class stores days present
# 3- create a manager class that inherits both employee and attendence and additionally adds team size variable
# initialize all values when creating  an manager object and dispaly all the information

# pending

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

    