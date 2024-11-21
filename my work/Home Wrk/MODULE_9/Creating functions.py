# -*- coding: windows-1251 -*-
import sys
import io
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='windows-1251')

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for item in data_set:
                file.write(str(item) + "\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words, **kwargs):
        self.words = words
        self.kwargs = kwargs

    def __str__(self):
        return f'MysticBall'

    def __call__(self):
        random_word = random.choice(self.words)
        return random_word


first_ball = MysticBall('Да', 'Нет', 'Наверное', "Semperconvallis", "Curaeluctus", "FelipeXue", a=6)
print(first_ball())
print(first_ball())
print(first_ball())
