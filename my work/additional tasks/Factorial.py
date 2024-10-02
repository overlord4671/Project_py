import sys
from sys import getsizeof

sys.set_int_max_str_digits(999999999)


#
# def Factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * Factorial(n - 1)


def Factorial_1(n):
    C = 1
    while n > 1:
        C = C * n
        n = n - 1
    return C


n = int(input('Введите число: '))
print('Значение: ', Factorial_1(n))
num_digits = len(str(Factorial_1(n)))
print(f"Количество символов в факториале:", num_digits)
print(getsizeof(Factorial_1(n)) / (1024 ** 2))

# def FCTRL(n):
#     if n == 1:
#         return 1
#     else:
#         return n * FCTRL(n - 1)
#
#
# print(FCTRL(10))
