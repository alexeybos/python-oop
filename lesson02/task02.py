class Dwarf:
    def __init__(self, name, age, profession, health, hair_color):
        self.name = name # имя
        self.age = age # возраст
        self.profession = profession # профессия
        self.health = health # HP
        self.hair_color = hair_color # цвет волос

    def happy_birthday(self):
        self.age += 1

    def hit_by_weapon(self, damage: int):
        self.health -= damage

class Weapon:
    def __init__(self, name, lethal_distance, material, cost, damage):
        self.name = name # наименование
        self.lethal_distance = lethal_distance # дистанция применения (метры)
        self.material = material # материал
        self.cost = cost # стоимость (золотых)
        self.damage = damage # причиняемый вред (в HP)

class Animal:
    def __init__(self, name, speed, category, is_dangerous, health):
        self.name = name # наименование
        self.speed = speed # скорость км/ч
        self.category = category # вид животного (млекопитающее, пресмыкающееся и т.п.)
        self.is_dangerous = is_dangerous # опасное или нет
        self.health = health  # % здоровья

    def kick(self):
        self.speed += 0.1

    def feed(self, cal):
        self.health += cal * 0.2


dwarf = Dwarf('Gimly', 110, 'Warrior', 150, 'Black')
animal = Animal('Hedgehog', 5.4, 'predator', False, 100)

dwarf.happy_birthday()
print(f'{dwarf.name} age is {dwarf.age}')
dwarf.hit_by_weapon(10)
dwarf.hit_by_weapon(10)
dwarf.hit_by_weapon(10)
print(f'{dwarf.name} health is {dwarf.health}')

animal.kick()
print(f'{animal.name} speed is {animal.speed}')
animal.feed(1000)
print(f'{animal.name} health is {animal.health}')
