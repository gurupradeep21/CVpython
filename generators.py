# def m1(start,stop):
#     current=start
#     while current <= stop:
#
#         yield current
#         current +=1
# x=m1(1,5)
# for i in x:
#     print(i)

# def m1(start,stop):
#     while start <= stop:
#         yield start
#         start +=1
# x=m1(5,10)
# y=m1(20,30)
# for i in x:
#     print(i)
# for i in y:
#     print(i)

# def g2():
#     n=1
#     while True:
#         yield n
#         n +=1
# x=g2()
# print(next(x))
# print(next(x))
# print(next(x))

# def g2():
#     n=2
#     while True:
#         yield n
#         n +=2
# x=g2()
# print(next(x))
# print(next(x))
# print(next(x))

# def g2():
#     a,b=0,1
#     while True:
#         yield a
#         a,b = b, a+b
# x=g2()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# l=[x for x in range(1,10)]
# print(l)
# print(type(l))
# s={x for x in range(1,10)}
# print(s)
# print(type(s))
# d={x:x*x for x in range(1,5)}
# print(d)
# print(type(d))
#
# t=tuple(x for x in range(1,5))
# print(t)
# print(type(t))
# g=(x for x in range(1,5))
# for i in g:
#     print(i)
#
# g=(x for i in range(2) for x in range(1,5))
# for i in g:
#     print(i,end=" ")
#
# g2=(x for x in range(1,10) if x % 2 == 0)
# for i in g2:
#     print(i)
#
# print("-----------------")
# print(max(x for x in range(1,10) if x % 2==0))
# print(sum(x for x in range(1,10) if x % 2==0))
# print(min(x for x in range(1,10) if x % 2==0))

import sys
l = [x for x in range(100000)]
print(sys.getsizeof(l))
g=(x for x in range(100000))
print(sys.getsizeof(g))
