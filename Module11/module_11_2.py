from pprint import pprint


def introspection_info(obj):
    dictionary = {
        'Type': type(obj).__name__,
        'Attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'Methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'Module': getattr(obj, '__module__', None)
    }
    return dictionary


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 50
        self.fullness -= 10


man = Man("Volodya")

member_info = introspection_info(42)
member_info_2 = introspection_info(man)
pprint(member_info, sort_dicts=False)
pprint(member_info_2, sort_dicts=False)