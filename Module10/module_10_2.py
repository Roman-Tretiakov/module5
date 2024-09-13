from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        if type(name) is not str:
            raise ValueError(f'name must be string')
        if type(power) is not int:
            raise ValueError(f'power must be int')

    def run(self):
        enemy_count = 100
        battle_days = 0
        print(f'{self.name}, на нас напали!')
        while enemy_count > 0:
            enemy_count -= self.power
            battle_days += 1
            print(f'{self.name} сражается {battle_days}-й день, осталось {enemy_count} воинов.')
            sleep(1)

        print(f'{self.name} одержал победу спустя {battle_days} дней(дня)!')


knights = [Knight('Sir Lancelot', 10), Knight("Sir Galahad", 20)]
threads = []

for k in knights:
    k.start()
    threads.append(k)

for t in threads:
    t.join()

print(f'Все битвы закончились!')
