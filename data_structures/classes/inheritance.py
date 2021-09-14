class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 50

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


dog = Mammal()
dog.eat()
dog.walk()

print(isinstance(dog, Mammal))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object))  # True
print(issubclass(Mammal, Animal))  # True

o = object()
print(isinstance(o, object))  # True


# Declaring a constructor in Mammal subclass will completely override the
# constructor in the parent class, use super to inherit the properties
print(dog.age)
print(dog.weight)
