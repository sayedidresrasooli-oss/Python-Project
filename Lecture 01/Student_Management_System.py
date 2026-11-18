from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.email}"


class Student(Person):
    def role_info(self):
        return f"Student: {self.name}"


class Lecturer(Person):
    def role_info(self):
        return f"Lecturer: {self.name}"


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.name}"


# Objects
s1 = Student("Ali", "ali@gmail.com")
s2 = Student("Ahmad", "ahmad@gmail.com")
l1 = Lecturer("Rahimi", "rahimi@gmail.com")

# Composition
course = Course("Python")
course.add_student(s1)
course.add_student(s2)

# Polymorphism
people = [s1, s2, l1]

for person in people:
    print(person.role_info())

print(course)

for student in course.students:
    print(student)
