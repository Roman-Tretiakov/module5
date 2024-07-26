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

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        print(f'{type(self).__name__} and {type(other).__name__} can\'t be compared.')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        print(f'{type(self).__name__} and {type(other).__name__} can\'t be compared.')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        print(f'{type(self).__name__} and {type(other).__name__} can\'t be compared.')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        print(f'{type(self).__name__} and {type(other).__name__} can\'t be compared.')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        print(f'{type(self).__name__} and {type(other).__name__} can\'t be compared.')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        print(f'{type(self).__name__} and {type(other).__name__} can\'t be compared.')

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        print(f'{type(value).__name__} is not int type.')

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК "Альбатрос"', 10)
h2 = House('ЖК "Французский бульвар"', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
