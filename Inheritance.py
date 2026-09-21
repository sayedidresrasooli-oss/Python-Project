class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()

c = Car()
print(c.start())



class Person:
    def __init__(self, name, age, classes):
        self.name = name
        self.age = age
        self.classes = classes

    def __str__(self):
        return f"{self.name} has {self.age} years old"

class Student(Person):
    def __init__(self, name, age, classes):
        super().__init__(name, age, classes)



s = Student("John", 18, 12)
print("Name  Age  Class")
print(s.name, end = "  ")
print(s.age, end = "   ")
print(s.classes, end = " ")



