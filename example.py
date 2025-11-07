class Cat:
    def __init__(self, cat_name, cat_age, cat_weight, cat_speed, cat_fq):
        self.name = cat_name # прозвище
        self.age = cat_age # возраст, полных лет
        self.weight = cat_weight # масса, кг
        self.speed = cat_speed # скорость, км/ч
        self.fq = cat_fq # частота текущего мурлыканья, Гц

    def Run(self, new_speed):
        self.speed = new_speed

    def Stop(self):
        self.speed = 0

    def Eat(self, food):
        self.weight += food

    def purr(self, freq):
        self.fq = freq

    def sleep(self):
        self.speed = 0
        self.fq = 0
        self.weight -= 0.1