class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории. \n')


h1 = House('ЖК "Альбатрос"', 10)
print(f'{House.houses_history}\n')

h2 = House('ЖК "Французский бульвар"', 20)
print(f'{House.houses_history}\n')

h3 = House('ЖК "Матрёшки"', 20)
print(f'{House.houses_history}\n')

# Удаление объектов
del h2
del h3

print(f'{House.houses_history}\n')