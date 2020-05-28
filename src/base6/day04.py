class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 相当于  java中的 toString
    def __str__(self):
        return "object"


p1 = Person("lvliao", 21, 175)
print(p1)
