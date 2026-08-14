def mul(a,b,c):
    return a*b*c
x=mul(2,3,4)
print(x)

print()

def describe_pet(animal,name):
    print("My",animal,"is named as",name)


def power(base,exponent):
    return base**exponent
print(power(2,3))
print()


def full_name(first,middle,last):
    return first+' '+middle+' '+last
print(full_name("Guru","Pradeep","Yadav"))


#    --------------------------------------------
 # create a fuc calculate bill with parameters price and quantity that returns toatal cost. add 40rs delivery if toatal is less than 200, call in a single line and print it
 # create a python application with 3 functions 1 total with three subject marks. 2nd one average which takes inputnof total marks and avg. 3rd one takes avg as input if avg is > 85 return A grade, 75 b, bet 65- 75 return c50-65 return d.


def calulate_bill(price,quantity):
    total=price*quantity
    if (total< 200):
        total+=40
        return total
print(calulate_bill(1000,2))

print(calulate_bill(1000,3))
print(calulate_bill(1000,4))