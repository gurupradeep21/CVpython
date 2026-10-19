class A:
    a = 40
    b = 50
    def __init__(self,x,y):
        self.x = x
        self.y = y
class B(A):
    c = 100
    def __init__(self,z):
        self.z = z
        # A.__init__(self,10,20)
        super().__init__(10,20)
b = B(30)
print(b.a)
print(b.b)
print(b.c)
print(b.x)
print(b.y)
print(b.z)
