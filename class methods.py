# class PasswordUtils:
#     @staticmethod
#     def is_strong(password):
#         if len(password)>=8:
#             return True
#     def generate_hint(self):

class Student:
    count=0
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        Student.count+=1

    def display(self):
        print("Student Name:",self.name)
        print("Student Roll No:",self.rollno)
        print("Student Marks:",self.marks)
        print("Student result:",Student.check(self.marks))

    def calculate_percentage(self):
        per = (sum(self.marks) // len(self.marks))*100
        print(self.name,"has secured",per,"%")

    @classmethod
    def total(cls):
        print("Total Students enrolled :",cls.count)

    @staticmethod
    def check(marks):
        if sum(marks) >= 40:
            print("Pass")
        else:
            print("Fail")

s1=Student("A",1,[60,70,80])
s2=Student("A",1,[60,70,80])
s3=Student("A",1,[60,70,80])
s1.display(),