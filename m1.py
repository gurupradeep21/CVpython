# def cal(a,b):
#     return[a+b,a-b,a*b]
# res=cal(10,20)
# print(res)



# def say_hello(greet):
#     print(greet)
# say_hello("hi")

# def add(a,b):
#     return a+b
# print(add(1,2))

# def info(name,age,grade):
#     print(f"Name: {name}, Age:{age}, Grade:{grade}")
# info("pradeep",22,"A")

#----------------------------------------------------

# def mul(a,b,c):
#     return a*b*c
# print(mul(10,10,10))

# def pet(animal,name):
#     print(f"MY {animal} is named {name}")
# pet("cat","sheela")

# def full_name(first,middle,last):
#     return first+' '+middle+' '+last
# print(full_name("Guru","Pradeep","Yadav"))

import copy

l1 =[["Balaji","Nalgonda"],["Telangana","India"]]
dp = copy.deepcopy(l1)
print(dp)
dp[0][0]="pradeep"
print(dp)
print(l1)
sp = copy.copy(l1)
sp[0][1]="Hyderabad"
print(sp)
print(l1)