import threading
import random
import time


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            rand = random.randint(50, 500)
            with self.lock:
                self.balance += rand
                print(f'Пополнение: {rand}. Баланс: {self.balance}')
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на {rand}')
            with self.lock:
                if rand <= self.balance:
                    self.balance -= rand
                    print(f'Снятие: {rand}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
                    if not self.lock.locked():
                        self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
