import math


class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__()
        self.set_color(*color)
        self.set_sides(*sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        if len(self.get_sides()) == 1:
            circumference = self.get_sides()[0]
            return circumference / (2 * math.pi)
        return 0

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__()
        self.set_color(*color)
        self.set_sides(*sides)

    def get_square(self):
        sides = self.get_sides()
        if len(sides) == 3:
            a, b, c = sides
            p = (a + b + c) / 2
            return math.sqrt(p * (p - a) * (p - b) * (p - c))
        return 0


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__()
        self.set_color(*color)
        self.set_sides(*[side_length] * 12)

    def get_volume(self):
        sides = self.get_sides()
        if sides:
            return sides[0] ** 3
        return 0


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
