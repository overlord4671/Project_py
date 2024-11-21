# создать класс для квадратного уравнения, который принимает в конструкторе ИЛИ 3 числа a b d ИЛИ самой строки этого квадратного уравнения.
# так же необходимо написать функцию для рассчета корней X_1 X_2 ИЛИ написать что решения нет.
# a * x ** 2 + b * x + c
# необходимо реализовать консольный ввод квадратного уравнения в виде строки и передавать в функцию и выводить ответ
# разобраться с 2x 2*x, пробелами, перестановкой, тем что нет коеф.

import re
import math


class Solution:
    def __init__(self, a: float, b: float, c: float = 0):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        D = self.b ** 2 - 4 * self.a * self.c  # дискриминант

        if D < 0:
            return 'No real solutions'  # если дискриминант отрицательный

        X_1 = (-self.b + math.sqrt(D)) / (2 * self.a)
        X_2 = (-self.b - math.sqrt(D)) / (2 * self.a)

        return X_1, X_2


def clean_equation(equation: str):
    # Убираем пробелы и лишние символы
    equation = equation.replace(' ', '').replace('=', '')

    # Шаблон для поиска переменной (латиница или кириллица)
    match_var = re.search(r'[a-zA-Zа-яА-Я]', equation)

    if match_var:
        variable = match_var.group(0)  # Переменная найдена
        # Заменяем переменную на стандартную 'x'
        equation = re.sub(variable, 'x', equation)

    # Шаблон для замены случаев вида "2x2" на "2*x**2"
    equation = re.sub(r'(\d)(x)', r'\1*\2', equation)
    equation = re.sub(r'(x)(\d)', r'\1**\2', equation)
    return equation


def parse_string(equation: str):
    # Очищаем и исправляем строку
    equation = clean_equation(equation)

    # Шаблон для поиска коэффициентов
    pattern = r'([+-]?\d*)\*?x\*\*2([+-]?\d*)\*?x([+-]?\d+)'

    match = re.match(pattern, equation)

    if match:
        a_str, b_str, c_str = match.groups()

        # Если коэффициент не указан, то подразумеваем 1
        a = float(a_str) if a_str not in ('', '+', '-') else float(a_str + '1')
        b = float(b_str) if b_str not in ('', '+', '-') else float(b_str + '1')
        c = float(c_str)

        # Форматируем уравнение для вывода пользователю
        formatted_equation = f"{a}*x**2 {'+' if b >= 0 else ''}{b}*x {'+' if c >= 0 else ''}{c} = 0"
        print(f"Ваше уравнение: {formatted_equation}")

        return Solution(a, b, c)
    else:
        raise ValueError("Invalid quadratic equation format. Please check your input.")


if __name__ == "__main__":
    while True:
        try:
            eq_input = input("Введите квадратное уравнение: ")
            equation = parse_string(eq_input)
            roots = equation.solve()
            print("Корни уравнения:", roots)
            break
        except ValueError as ve:
            print(ve)
            print("Попробуйте ввести уравнение ещё раз.")
