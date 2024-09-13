from random import randint
# from threading import Lock
import threading
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            _sum = randint(50, 500)
            self.balance += _sum
            print(f'Пополнение: {_sum}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            _sum = randint(50, 500)
            print(f'Запрос на {_sum}')
            if _sum <= self.balance:
                self.balance -= _sum
                print(f'Снятие: {_sum}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств!')
                self.lock.acquire()


bank = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bank,))
th2 = threading.Thread(target=Bank.take, args=(bank,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bank.balance}')