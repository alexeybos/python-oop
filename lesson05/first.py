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

def create500_in_list(array_size: int) -> list[Animal]:
    animals = []
    for i in range(array_size):
        if random.randint(1, 10000) % 2 == 0:
            animals.append(Cat())
        else:
            animals.append(Bird())

    return animals

size = input("Введите размер массива animals: ")

animals_list = create500_in_list(int(size))
for animal in animals_list:
    animal.foo()
