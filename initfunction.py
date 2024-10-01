# constructor

class Student:
    name = "Rohit"

    # def __init__(self):
    #     print("hello world")         // error for constructor overloadding

    def __init__(self, name , marks):
        self.name = name
        self.marks = marks


s1 = Student("AMi",23)

print(s1.marks)
print(s1.name)