

# add1=lambda x,y : x+y
# print(add1(10,20))


# def add(x,y):
#     return x+y
# print(add(10,20))
# print("--------------------------------------")
#
# square=lambda x:x**2
# print(square(5))
# print(square(6))
# print("-------------------------------------")
#
# cube=lambda x:x**3
# print(cube(3))
#
# large=lambda x,y:x if x>y else y
# print(large(10,20))
#
# even=lambda x:x%2==0
# print(even(10))
# print(even(11))
#
# l=[1,23,4,42,56,10,2]
# l.sort(key=lambda x:x)
# print(l)
# #
# l=[1,23,4,42,56,10,2]
# l.sort(key=lambda x:-x)
# print(l)
#
# t=[(1,'banana'),(2,'apple'),(3,'cherry')]
# t.sort(key=lambda x:x[1])
# print(t)
#
#
# add=lambda x,y:x+y
# multiply=lambda a,b:a*b+add(a,b)
# print(multiply(10,20))
#
#
# intrest=lambda p,t,r:(p*t*r)/100
# print(intrest(1000,1,5))


t=[(1,'banana'),(2,'apple'),(3,'mango')]
t1=sorted(t,key= lambda x:x[1])
print(t1)