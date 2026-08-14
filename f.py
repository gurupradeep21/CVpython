import copy
org_msgs = [['hi'],['hoe are you'],['where are you']]
print(org_msgs)
print(id(org_msgs[0]))
print(id(org_msgs[1]))

shal_cpy = copy.copy(org_msgs)
shal_cpy[0] = ['hey']
print(shal_cpy)
print(id(shal_cpy[0]))
print(id(shal_cpy[1]))
# shallow copy
#outer objects are copied, but inner objects are shared
#deep copy
#create apy program where shopping cart contqins list of products and each product has a list of features, create duplicate card using shalo copy and modify the feature of one product in the copy card check if the org card change and use the deep copy and explain the difference



#
# import copy
#
# l1 =[["Balaji","Nalgonda"],["Telangana","India"]]
# dp = copy.deepcopy(l1)
# print(dp)
# dp[0][0]="pradeep"
# print(dp)
# print(l1)
# sp = copy.copy(l1)
# sp[0][1]="Hyderabad"
# print(sp)
# print(l1)

# og=[['hi'],['hello how are you '],['bye']]
# print(og)
#
# og[0]=['mama']
# print(id(og[0]))
# print(id(og[1]))
# import copy
# shal_copy=copy.copy(og)
# shal_copy[0]=['hey']
# print(shal_copy)
# print(id(shal_copy[0]))
# print(id(shal_copy[1]))

# import copy
#
# # Original Shopping Cart
# org_cart = [
#     ["Laptop", ["8GB RAM", "512GB SSD"]],
#     ["Mobile", ["128GB Storage", "5000mAh Battery"]]
# ]
#
# print("Original Cart:")
# print(org_cart)
#
# print(id(org_cart[0]))
# print(id(org_cart[1]))
#
# # Shallow Copy
# shal_cpy = copy.copy(org_cart)
#
# # Modify feature of Laptop in copied cart
# shal_cpy[0][1][0] = "16GB RAM"
#
# print("\nShallow Copy:")
# print(shal_cpy)
#
# print(id(shal_cpy[0]))
# print(id(shal_cpy[1]))
#
# print("\nOriginal Cart After Shallow Copy Change:")
# print(org_cart)
#
# # Deep Copy
# deep_cpy = copy.deepcopy(org_cart)
#
# # Modify feature of Mobile in deep copied cart
# deep_cpy[1][1][0] = "256GB Storage"
#
# print("\nDeep Copy:")
# print(deep_cpy)
#
# print("\nOriginal Cart After Deep Copy Change:")
# print(org_cart)