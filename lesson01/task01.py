# 1.1
# 1) TickTick - приложение для управления задачами и планирования.
# Думаю есть классы
# "Категория" (категория задачи) - "Наименование категории", "Цвет категории", "Значок категории"
# "Задача" с полями "Название", "Комментарий", "Время работы над задачей", "Приоритет", "Категория"
# 2) Три в ряд. Классы:
# GameItem (собираемые элементы) - поля Координаты (Х и Y), Тип
# GameField (игровое поле) - поля Длина, Ширина, Набор (список) элементов

# 1.2
class Dwarf:
    name = 'Alex' # имя
    age = 18 # возраст
    profession = 'Soldier' # профессия
    health = 100 # % здоровья
    hair_color = 'Black' # цвет волос

class Weapon:
    name = 'Bow' # наименование
    lethal_distance = 25 # дистанция применения (метры)
    material = 'Wood' # материал
    cost = 100 # стоимость (золотых)
    wear = 0 # износ (%)

class Animal:
    name = 'Cow' # наименование
    speed = 1 # скорость м/с
    type = 'mammal' # вид животного (млекопитающее, пресмыкающееся и т.п.)
    is_dangerous = False # опасное или нет
    health = 100  # % здоровья

dwarf1 = Dwarf()
dwarf2 = Dwarf()
dwarf2.name = 'Bob'
weapon1 = Weapon()
weapon1.name = 'Sword'
weapon1.material = 'Metal'
weapon2 = Weapon()
animal1 = Animal()
animal2 = Animal()
animal2.name = 'Tiger'
animal2.is_dangerous = True
print(f'dwarf1 name is {dwarf1.name}')
print(f'dwarf2 name is {dwarf2.name}')
print(f'{animal1.name} is {'dangerous' if animal1.is_dangerous else 'not dangerous'}')
print(f'{animal2.name} is {'dangerous' if animal2.is_dangerous else 'not dangerous'}')
print(f'{weapon1.name} is from {weapon1.material}')
print(f'{weapon2.name} is from {weapon2.material}')

# 1.3

dwarf1 = dwarf2
print('dwarf1 = dwarf2')
print(f'dwarf1 name is {dwarf1.name}')
print(f'dwarf2 name is {dwarf2.name}')

dwarf1.name = 'New name'
print('dwarf1.name = "New name"')
print(f'dwarf1 name is {dwarf1.name}')
print(f'dwarf2 name is {dwarf2.name}')

dwarf2.name = 'Robert'
print('dwarf2.name = "Robert"')
print(f'dwarf1 name is {dwarf1.name}')
print(f'dwarf2 name is {dwarf2.name}')