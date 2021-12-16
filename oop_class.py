
class Dog:
    # Атрибут класса
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.age)