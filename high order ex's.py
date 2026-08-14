# def my_map(func,list):
#     result=[]
#     for i in list:
#         x=func(i)
#         result.append(x)
#     return result
# def square(x):
#     return x**2
# l=[10,20,30]
# print(list(my_map(square,l)))
# print(list(filter(lambda x:x>500,my_map(square,l))))

# def my_map(func,list):
#     result=[]
#     for i in list:
#         x=func(i)
#         result.append(x)
#     return result
# l=[10,20,30]
# def square(x):
#     return x**2
# print(list(my_map(square,l)))

# t=[("guru",90),("balaji",95),("pradeep",100)]
# sorted_marks=sorted(t,key=lambda x:x[1],reverse=True)
# sorted_name=sorted(t,key=lambda x:x[0])
# print(sorted_marks)
# print(sorted_name)

# t=[("guru",90),("balaji",95),("chinnu",85)]
# s_m=sorted(t, key=lambda x:x[1])
# s_n=sorted(t, key=lambda x:x[0])
# print(s_m)
# print(s_n)


# string=["hi","bye","hello"]
# len_str=sorted(string,key=lambda x:len(x))
# alpha=sorted(string,key=lambda x:x)
# print(len_str)
# print(alpha)

# from functools import reduce
# l=[2,3,5,10,20,15]
# l1=list(filter(lambda x:x if x%2==0 and x%5==0 else None,l))
# print(l1)
# l2=list(map(lambda x:x+5,l1))
# print(l2)
# l3=reduce(lambda x,y:x*y,l2)
# print(l3)
from functools import reduce
l=[2,3,4,5,6,6,7,10,20]
l1=list(filter(lambda x:x if x%2==0 and x%5==0 else None,l))
print(l1)
l2=list(map(lambda x:x+5,l1))
print(l2)
l3=reduce(lambda x,y:x*y,l2)
print(l3)

# from functools import reduce
# l=[1,2,3,4,5,5,6,7,8,9,10]
# div=list(filter(lambda x:x if x%2==0 and x%4!=0 else None,l))
# print(div)
# add=list(map(lambda x:x+3,div))
# print(add)
# prod=reduce(lambda x,y:x*y,add)
# print(prod)

# def apply_op(a,b,op):
#     return op(a,b)
# print(apply_op(10,20, lambda x,y:x-y))
#
#
# def make_greeting(name,prefix="hello",formatter=lambda x:x):
#     s=prefix +' '+name
#     return formatter(s)
# print(make_greeting("alice",prefix="hi",formatter=lambda x:x.upper()))

# def make_greeting(name,prefix="hello",formatter=lambda x:x):
#     s=prefix+" "+name
#     return formatter(s)
# print(make_greeting("alice",prefix="hi",formatter=lambda x:x.upper()))
# # from functools import reduce
# l=[1,17,23,56,7,4,6]
# print(reduce(lambda x,y:x if x>y else y,l))
#
# l1=["hi","hello","bye"]
# print(reduce(lambda x,y:x+'-'+y,l1))

from functools import reduce
l=["HELLO","MADAM","OPPO",'MALAYALAM',"RABBIT","HI"]
print(list(filter(lambda x:x[0]==x[-1],l)))
print(list(map(lambda x:x.lower(),l)))
print(sorted(l, key= lambda x:x, reverse=True))
print(sorted(l,key=lambda x:len(x)))
print(reduce(lambda x,y:x+""+y,l))

# from functools import reduce
# t=[{"type":"credit","amount":1000},
#    {"type":"debit","amount":500},
#    {"type":"credit","amount":2000}
#    ]
# credit=list(filter(lambda x:x["type"]=="credit",t))
# print(credit)
# bonus=list(map(lambda x:{"type":x["type"],"amount":x["amount"]*1.05},credit))
# print(bonus)
# des=sorted(bonus,key=lambda x:x["amount"], reverse=True)
# print(des)
# total=reduce(lambda x,y:x+y["amount"],bonus,0)
# print(total)


# def mystery(*args, **kwargs):
#     print(sum(args), list(kwargs.values()))
# mystery(1, 2, 3, a=4, b=5)
#
# from functools import reduce
# data = [2, 3, 4]
# result = reduce(lambda a, b: a * b, list(map(lambda x: x + 1, data)))
# print(result)
#
# def f(n):
#  if n == 0: return 0
#  return n + f(n - 1)
# print(f(4))

#7,
# def f(n):
#     if n==0:return 0
#     return n+ f(n-1)
# print(f(4))