# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
#     def __str__(self):
#         return f"{self.name} has gotten {self.marks} marks."
#
#     def __repr__(self):
#         return f"Student ({self.name},{self.age},{self.marks})"
#
#
# obj = Student("alice", 23, 90)
# # print(obj)
# # print(str(obj))
# print(repr(obj))

class Student:
    def __init__(self, name, age, marks, subjects):
        self.name = name
        self.age= age
        self.marks = marks
        self.subjects = subjects
    def __str__(self):
        # return f"{self.name} has gotten {self.marks} marks."
        return f"Hey! This is {self.name}!!"
    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.marks})"
    def __len__(self):
        # return len(self.subjects)
        return len(self.name)
    def __contains__(self, item):
        return item in self.subjects
    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.marks - other.marks
    def __mul__(self, other):
        return self.age * other.age
    def __truediv__(self, other):
        return len(self.subjects)/len(other.subjects)
    def __floordiv__(self, other):
        return len(self.subjects)//len(other.subjects)
    def __lt__(self, other):
        return self.marks < other.marks
    def __gt__(self, other):
        return self.marks > other.marks
    def __le__(self, other):
        return self.marks <= other.marks
    def __ge__(self, other):
        return self.marks >= other.marks
    def __eq__(self, other):
        return self.marks == other.marks
    def __ne__(self, other):
        return self.marks != other.marks
    def __hash__(self):
        return self.age
obj1 = Student("Alice", 27, 78, ['Maths', 'Science'])
obj2 = Student("Reene", 22, 79, ['Maths', 'Science', 'Geography', 'Civics'])
obj3 = Student("Meg", 25, 72, ['Maths'])
obj4 = Student("Candice", 24, 98, ['Maths', 'Civics', 'Science'])
obj5 = Student("Max", 23, 88, ['English', 'Python'])
# print(obj1)
# print(obj2)
# print(obj4)
#
# print(repr(obj1))
# print(len(obj1))
# print('English' in obj1)
# print('Maths' in obj1)
# print(obj1 + obj2)
# print(obj3 - obj4)
# print(obj2 * obj3)
# print(obj1 / obj2)
# print(type(obj1 // obj2))
# print(obj1 < obj2)
# print(obj2 > obj1)
# print(obj2 >= obj1)
# print(obj5 <= obj3)
# print(obj3 == obj2)
# print(obj4 != obj5)
print(hash(obj1))
class Number:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return f"{self.n}"
    def __add__(self, other):
           return  Number(self.n * other.n)
    def __sub__(self, other):
            return Number(self.n - other.n)
    def __truediv__(self, other):
        return Number(self.n / other.n)
    def __floordiv__(self, other):
        return Number(self.n // other.n)
    def __mul__(self, other):
        return Number(self.n * other.n)
    def __pow__(self, power, modulo=None):
        return Number(self.n ** power)
# n1 = Number(10)
# n2 = Number(20)
# print(type(n1 + n2))
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 // n2)
# print(n1 / n2)
# print(n1 ** 3)