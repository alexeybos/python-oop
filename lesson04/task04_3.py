import random


class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def do_something_with_animal(animal: Animal):
    animal.foo()

def create500_in_list(animals: list[Animal]):
    animals.clear()
    for i in range(500):
        if random.randint(1, 10000) % 2 == 0:
            animals.append(Cat())
        else:
            animals.append(Bird())

animals_list = [Cat(), Bird()]
create500_in_list(animals_list)
for animal in animals_list:
    animal.foo()
