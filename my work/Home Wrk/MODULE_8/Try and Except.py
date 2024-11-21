# def add_everything_up(a, b):
#     try:
#         if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#             return f'{a + b:.3f}'
#         elif isinstance(a, str) and isinstance(b, str):
#             return a + b
#         else:
#             return str(a) + str(b)
#     except Exception as e:
#         return f"Произошла ошибка: {e}"
#
#
# print(add_everything_up(123.456, 'строка'))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))


# Напиши функцию safe_divide(a, b), которая принимает два числа и выполняет их деление. Функция должна обрабатывать различные исключения:
#
# Если происходит деление на ноль (ZeroDivisionError), функция должна выводить сообщение: "Деление на ноль невозможно!".
# Если в функцию переданы нечисловые значения (TypeError), вывести сообщение: "Неверный тип данных!".
# Если деление прошло успешно, вывести результат в блоке else.
# Независимо от результата или наличия ошибок, в блоке finally вывести сообщение: "Операция завершена".


def safe_divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print(f"Деление на ноль невозможно!")
        return a, b
    except TypeError:
        print(f"Неверный тип данных!")
        return a, b
    else:
        print(f'Результат {res}')
        return res
    finally:
        print(f"Операция завершена")


print(safe_divide(10, 2))  # Ожидаемый вывод: Результат деления: 5.0
# Операция завершена

print(safe_divide(10, 0))  # Ожидаемый вывод: Деление на ноль невозможно!
# Операция завершена

print(safe_divide(10, 'a'))  # Ожидаемый вывод: Неверный тип данных!
# Операция завершена
