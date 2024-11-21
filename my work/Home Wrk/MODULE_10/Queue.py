import queue
import threading
import time
import random


class Table:
    def __init__(self, number, guests=None):
        self.number = number
        self.guests = guests


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            table_found = False
            for table in self.tables:
                if table.guests is None:
                    table.guests = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table_found = True
                    break
            if not table_found:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guests for table in self.tables):
            for table in self.tables:
                guest = table.guests
                if guest and not guest.is_alive():
                    print(f'{guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол {table.number} свободен ')
                    table.guests = None
                if not self.queue.empty():
                    new_guest = self.queue.get()
                    table.guests = new_guest
                    print(f'{new_guest.name} вышел(-а) из очереди и сел(-а) за стол номер {table.number}')
                    new_guest.start()
            time.sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
