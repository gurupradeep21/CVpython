# 2,4,6,8,10,12,14,16,18,20,22,24
# 2,6,12,20
# n=int(input())
# c=0
# for i in range(1,n+1):
#     if(i%2==0):
#         c=c+1
#
#
#         print(i,end=" ")


# n=int(input())
# s=n*n
# d=1
# t=n
# while(t>10):
#     d=d*10
#     t=t//10
# if(s % (d*10)==n):
#     print("automophic")
# else:
#     print("No automophic")

# n=int(input())
# s=n*n
# t=n
# d=1
# while(t>10):
#     d=d*10
#     t=t//10
# if(s % (d*10)==n):
#     print("automophic")
# else:
#     print("not automophic")

# n=int(input())
# t=n
# rev=0
# while(n>0):
#     r=t%10
#     rev=rev*10+r
#     t=t//10
# if(rev==t):
#     print(t)
# n=n+1

# n = int(input())
#
# while True:
#     temp = n
#     rev = 0
#
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp = temp // 10
#
#     if rev == n:
#         print(n)
#         break
#
#     n = n + 1  #145-->151
#
# n = int(input())
#
# while True:
#     temp = n
#     rev = 0
#
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp = temp // 10
#
#     if rev == n:
#         print(n)
#         break
#
#     n = n - 1  #145-->141

#------------------------------------------------------


# n=4
# if(n%2==0):
#     print("even")
# else:
#     print("odd")

# n=int(input())
# if(int(n*0.5)*2==n):
#     print("even")
# else:
#     print("odd")

# n=int(input())
# while(n>1):
#     n=n-2
# if(n==0):
#     print("even")
# else:
#     print("odd")

n=int(input())
x=0
while(x<n):
    x=x+2
if(x==n):
    print("even")
else:
    print("odd")


























