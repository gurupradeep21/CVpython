# def mul(a,b,c):
#     return a*b*c
# x=mul(2,3,4)
# print(x)


print()

# def describe_pet(animal,name):
#     print("My",animal,"is named as",name)



# def power(base,exponent):
#     return base**exponent
# print(power(2,3))
print()


# def full_name(first,middle,last):
#     return first+' '+middle+' '+last
# print(full_name("Guru","Pradeep","Yadav"))


#    -------------------------------------
 # create a fuc calculate bill with parameters price and quantity that returns toatal cost. add 40rs delivery if toatal is less than 200, call in a single line and print it
 # create a python application with 3 functions 1 total with three subject marks. 2nd one average which takes inputnof total marks and avg. 3rd one takes avg as input if avg is > 85 return A grade, 75 b, bet 65- 75 return c50-65 return d.


# def calulate_bill(price,quantity):
#     total=price*quantity
#     if (total< 200):
#         total+=40
#         return total
# print(calulate_bill(1000,2))
#
# print(calulate_bill(1000,3))
# print(calulate_bill(1000,4))

#----------------------------------
def describe_pet(animal,name):
    print(f"My {animal} is named as {name}")
x=describe_pet("cat","tom")

def power(base,exponent):
    return base**exponent
print(power(2,2))

def f_n(f,m,l):
    return f+" "+m+" "+l
print(f_n("guru","pradeep","yadav"))

def intro(name,city,hobby):
    print(f"{name} from {city} has {hobby} as hobby")
intro("pradeep","Hyd","cricket")

def sub(a,b):
    return a-b
print(sub(10,3))

def describe(color,size,shape):
    print(f" a {color} {size} {shape}")
describe(size="large",color="red",shape="circle")

def prof(name,email,age):
    print(f"Name: {name} ,Email: {email}, Age: {age}")
prof(name="pradeep",age=22,email="gurupradeepc@gmail.com")

def g(name,msg="hello"):
    print(f"{msg} {name}")
g("alice")
g("alicce","Good morning")

def create_account(username, role='student', active=True):
 print(f"User: {username}, Role: {role}, Active: {active}")
create_account("alice123")
# User: alice123, Role: student, Active: True
create_account("admin99","admin")
# User: admin99, Role: admin, Active: True

def s(base,exponent=2):
    return base**exponent
print(s(2))
print(s(2,2))

# arbitary arguments

def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(add(10,20,30,40,50))

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print(info(name="bob",age=22,city="hyd",hobby="cricket"))

def mul(*args):
    p=1
    for i in args:
        p*=i
    return p
print(mul(1,2,3))

def p(name,*hobbies):
    print(f"{name} hobbies are  {hobbies}")
p("pradeep","cricket","volleyball","singing","dancing")

def f(*args):
    print(type(args))
f(1,2,3)

def full_example(a, b, *args, option='default', **kwargs):
 print(a, b, args, option, kwargs)
full_example(1, 2, 3, 4, 5, option="custom", x=10, y=20)
