
# l=[1,2,3,4]
# p=list(map(lambda x:x**2,l))
# print(p)
#
#
#
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=list(map(lambda x,y:x+y ,l1,l2))
# print(l3)
#
# l=[10,23,30,40]
# l2=list(map(lambda x:x/2 ,l))
# print(l2)
#
#
#
# def isEven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l=[1,2,3,4,5,6]
# l2=list(filter(isEven,l))
# print(l2)
#
# print(list(filter(lambda x:x%2==0,p)))
# print(list(filter(lambda x:x%2==0,list(map(lambda x:x**2,l)))))
#

#
# #---------------------------------------------------------

# l=[100,200,300,400]
# l2=list(map(lambda x:x+(x*0.1),l))
# print(l2)
#
# l=["ram","balaji","pandu","charan"]
# l2=list(map(lambda x:x.title(),l))  #capitalize
# print(l2)
#
# l=[100,200,500,600,2000,4000,5345,66345]
# l2=list(filter(lambda x:x>500,l))
# print(l2)
#
# l=[1,2,3,4,5]
# l2=list(map(lambda x:x*5,l))
# print(l2)
#
# l=["hi","hello","python"]
# l2=list(map(lambda x:len(x),l))
# print(l2)
#
# l=[10,20,60,34,67,85,876,890]
# l2=list(filter(lambda x:x>50,l))
# print(l2)
#
# l=[4,5,6,7,8,9,10,11,12]
# l1=list(filter(lambda x:x%4==0,l))
# print(l1)
#
#
# l=[10,20,3,4,7,9]
# #l1=list(map(lambda x:x**2,l))
# l2=list(filter(lambda x:x%4==0,list(map(lambda x:x**2,l))))
# print(l2)
#
# l=[100,300,600,700,1000]
# l2=list(map(lambda x:x*0.1,list(filter(lambda x:x>500,l))))
# print(l2)
#
# l=[1,2,3,4,5,6]
# l2=list(map(lambda x:x*3,list(filter(lambda x:x%2==0,l))))
# print(l2)
#
# l=[10,20,30,40,50]
# l2=list(map(lambda x:x**2,list(filter(lambda x:x>20,l))))
# print(l2)
#
#
# l=["balaji","pradeep","chinna","sai"]
# l1=list(filter(lambda x:len(x)>4,l))
# l2=list(map(lambda x:x.upper(),l1))
# print(l2)
#
# from functools import reduce
# l=[1,2,3,4,7,9,14]
# print(reduce(lambda x,y:x+y,l))

#
# #-----------------------------------------------------------
#
# c=[20,30,40]
# f=list(map(lambda x:x*(9/5)+32,c))
# print(f)
# print()

#Q2. Use filter() to extract all words from a list that start with a capital letter.
# l=["Krishna","Balu","Pandu","guru","pradeep"]
# l2=list(filter(lambda x:x[0].isupper(),l))
# print(l2)
# print()
#
# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x*y,l))
# print()
#
# from functools import reduce
# l1=["Krishna","Balu","Pandu","guru","pradeep"]
# l2=reduce(lambda x,y:x if len(x)>len(y) else y,l1)
# print(l2)
#
# # --------------------------------------------------------------------------
# #Given a list of product prices, write a program to filter prices above ₹500,
# # then apply a 10% discount using map(), and compute the final total bill using reduce().
#
# l=[500,600,700,300,1000]
# l1=list(filter(lambda x:x>500,l))
# l2=list(map(lambda x:x+x*0.1,l1))
# from functools import reduce
# l3=reduce(lambda x,y:x+y,l2)
# print(l3)
#
#
# l=[1,-1,-2,-4,1,3,5]
# l1=list(filter(lambda x:x<0,l))
# l2=list(map(lambda x:abs(x),l1)) #*-1
# l3=reduce(lambda x,y:x+y,l2)
# print(l3)
#
#
# from functools import reduce
# l=[20,30,40,50,60,70,80]
# l1=list(filter(lambda x:x<50,l))
# l2=list(map(lambda x:x*3,l1))
# l3=reduce(lambda x,y:x if x>y else y,l2)
# print(l3)
#
#
# from functools import reduce
# l=["krishna","bye","hi","guru","pradeep"]
# l1=list(filter(lambda x:len(x)>3,l))
# l2=list(map(lambda x:x.upper(),l1))
# l3=reduce(lambda x,y:x+""+y,l2)
# print(l3)
#
# l=[30000,40000,50000]
# l1=list(filter(lambda x:x>30000,l))
# l2=list(map(lambda x:x*1.15,l1))
# l3=reduce(lambda x,y:x+y,l2)
# print(l3)
#
# l=[1,2,3,4,5,6]
# l1=list(filter(lambda x:x%2==1,l))
# l2=list(map(lambda x:x**2,l1))
# l3=reduce(lambda x,y:x+y,l2)
# print(l3)
#
#
# l=[600, 800, 1000, 550]
# l1=list(filter(lambda x:x>500,l))
# l2=list(map(lambda x:x-x*0.1,l1))
# l3=reduce(lambda x,y:x+y,l2)
# print(l3)
#
# l=[-100,-20,100,200,300]
# l1=list(filter(lambda x:x>0,l))
# l2=list(map(lambda x:x+10,l1))
# l3=reduce(lambda x,y:x+y,l2)
# print(l3)

words = ['banana', 'fig', 'apple', 'kiwi']
print(sorted(words, key=len))