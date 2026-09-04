# #create a class zomato with attributes
# class attributes: discount,coupon_code and list of all rest_names
# instance attributes: rest_name,dictionary of items,rest_id
# now, calculate rest_id based on another class variable resturent number.
# create a function variable rest_number.
# create a function order which takes an item number as input and checks wheatjer the user entered a valid id and
# prints the final bill if they entered copuncode correctly with discount
class Zomato:
    restaurant_names=[]
    restaurant_no=0
    coupon_code="PY20"
    discount=0.2
    def __init__(self,restaurant_name, restaurant_menu):
        self.restaurent_name=restaurant_name
        Zomato.restaurant_no+=1
        self.restaurent_id=Zomato.restaurant_no
        self.restaurent_menu=restaurant_menu
        Zomato.restaurant_names.append(restaurant_name)
Paradise=Zomato("Paradise",
                {"chicken Biriyani":200,
                 "mutton biriyani": 300,
                 "coke":40})

Pista_House=Zomato("Pista House",
                   {"mutton biriyani":300,
                    "prawns biriyani":350,
                    "fish fry":200})

KFC=Zomato("KFC",
           {
               "chicken biriyani":250,
               "fries":70,
               "burger": 60
           })
c=0
for i in Zomato.restaurant_names:
    c+=1
    print(c,":",i)
choice=int(input("Enter the Restaurant "))
