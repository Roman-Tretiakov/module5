class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor not in range(1, self.number_of_floors + 1):
            print('Такого этажа не существует!')
        else:
            print(*tuple(range(1, new_floor + 1)), sep='\n')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК "Альбатрос"', 8)
h2 = House('ЖК "Французский бульвар"', 5)

# h1.go_to(5)
# h2.go_to(8)
print(str(h1))
print(str(h2))

print(len(h1))
print(len(h2))