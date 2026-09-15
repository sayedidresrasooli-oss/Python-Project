class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.name)


class Person1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

p = Person1("Idris")
print(p)


class Person3:
    def __init__(self,  name):
        self.name = name
    def __repr__(self):
        return f"Person3('{self.name}')"

p = Person3("Jamal")
print(repr(p))


class Person4:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person4(20)
p2 = Person4(20)

print(p1 == p2)


class Person5:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)

p = Person5("Jamil")
print(len(p))



class Person6:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

p = Person6(18)
o = Person6(20)
print(p < o)