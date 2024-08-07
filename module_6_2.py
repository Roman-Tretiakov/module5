class Vehicle:
    __COLOR_VARIANTS = ['Silver', 'Black', 'Red', 'White']

    def __init__(self, owner_name, model, engine_power, color):
        self.owner = owner_name
        self.__model = model
        self.__engine_power = int(engine_power)
        self.__color = color

    def get_model(self):
        return f'Model: {self.__model}'

    def get_horsepower(self):
        return f'Engine power: {self.__engine_power}'

    def get_color(self):
        return f'Color: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nOwner is: {self.owner}')

    def set_color(self, new_color):
        if str(new_color).lower() in [c.lower() for c in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f'Impossible to change current color to {new_color}. ')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['Silver', 'Black', 'Red', 'White']
vehicle1 = Sedan('Masha', 'Toyota Corolla', 150, 'black')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
