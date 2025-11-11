from datetime import datetime, date, time

class Territory:
    def __init__(self, height, width, owner):
        self.height = height  # meters
        self.width = width  # meters
        self.owner = owner
        self.plants = []

    def is_occupied(self):
        return self.owner is not None and self.owner != ''

    def show_plants(self):
        for plant in self.plants:
            print(plant.name)


class Garden(Territory):
    def __init__(self, height, width, owner):
        super().__init__(height, width, owner)
        self.tree_count = 0

    def plant_tree(self, tree):
        self.tree_count += 1
        self.plants.append(tree)

    def cut_down_tree(self, tree_name):
        for tree in self.plants:
            if tree.name == tree_name:
                self.plants.remove(tree)
                self.tree_count -= 1
                return

        print(f"Дерево {tree_name} не найдено")

class Field(Territory):
    def __init__(self, height, width, owner):
        super().__init__(height, width, owner)
        self.ripening_date = None
        self.productivity = 0  # урожайность (кг с м**2)
        self.is_planted = False

    def seed(self, productivity, ripening_date, plants):
        self.productivity = productivity  # урожайность (кг с м**2)
        self.ripening_date = ripening_date
        self.is_planted = True
        self.plants = plants

    def harvest(self, harvest_date):
        if self.is_planted and harvest_date >= self.ripening_date:
            return self.width * self.height * self.productivity

        self.plants = []
        return 0


class Plant:
    def __init__(self, name, growth_per_day):
        self.name = name
        self.growth_per_day = growth_per_day  # см в день
        self.height = 0
        self.water_level = 50

    def water(self, amount):
        self.water_level = min(100, self.water_level + amount)
        print(f"Полили {self.name}. Уровень воды: {self.water_level}%")

    def grow(self):
        if self.water_level > 30:
            self.height += self.growth_per_day
            print(f"{self.name} вырос на {self.growth_per_day}. Теперь {self.height} см")
        else:
            print(f"{self.name} нуждается в поливе!")

    def get_info(self):
        return f"{self.name}, высота: {self.height} см"


class Tree(Plant):
    def __init__(self, name, growth_per_day, circumference_per_day):
        super().__init__(name, growth_per_day)
        self.circumference_per_day = circumference_per_day
        self.circumference = 0
        self.crown_diameter = 0

    def grow(self):
        if self.water_level > 30:
            self.height += self.growth_per_day
            self.circumference += self.circumference_per_day
            self.crown_diameter += self.circumference_per_day * 2.5
            print(f"{self.name} выросло. Теперь {self.height} см и в обхвате {self.circumference} см")
        else:
            print(f"{self.name} нуждается в поливе!")

    def provide_shade(self, area_size):
        shade_coverage = min(100, (self.crown_diameter / area_size) * 100)
        print(f"{self.name} создает тень на {shade_coverage:.1f}% площади")
        return shade_coverage


class Potato(Plant):
    def __init__(self, name, growth_per_day, tubers_per_height):
        super().__init__(name, growth_per_day)
        self.tubers_per_height = tubers_per_height
        self.pest_count = 0
        self.is_exterminated = False

    def get_tubers_count(self):
        return self.tubers_per_height * self.height / 10

    def check_pests(self):
        if self.is_exterminated:
            self.is_exterminated = False
        else:
            self.pest_count = 2 * self.height / 10

        return self.pest_count

    def extermination(self):
        self.pest_count = 0
        self.is_exterminated = True

tree1 = Tree("Береза", 0.05, 0.01)
tree2 = Tree("Дуб", 0.1, 0.02)
tree3 = Tree("Дуб", 0.1, 0.02)

potato1 = Potato("Богатырь", 0.02, 1)
potato2 = Potato("Белорусский", 0.01, 0.5)

garden = Garden(100, 100, "Иванов")
field = Field(1000, 200, "Петров")

garden.plant_tree(tree1)
garden.plant_tree(tree2)
garden.plant_tree(tree3)

field.seed(10, date(2026,5, 2), [potato1, potato2])

print('В саду растут:')
garden.show_plants()
print('На поле посажены сорта:')
field.show_plants()