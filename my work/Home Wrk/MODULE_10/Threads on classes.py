import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали! ')
        enemy = 100
        count = 0
        while enemy > 0:
            count += 1
            enemy -= self.power
            time.sleep(0.5)
            print(f'{self.name} сражается {count} дней... осталось {enemy} воинов. ')
        print(f'{self.name} одержал победу спустя {count} дней дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f"Все битвы закончились")
