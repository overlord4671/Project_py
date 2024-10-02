# Допустим, у нас есть список температур за неделю, и мы хотим найти первый день, когда температура упала ниже нуля, и напечатать все дни до этого.
# temperatures = [5, 3, 0, -1, 2, -3, 4]
# day = 0
# while day < len(temperatures):
#     print(f'День {day}: {temperatures[day]} градусов')
#     day += 1
# print(f'средняя температура за неделю: {float(sum(temperatures) / len(temperatures)):.3f} градусов')

# Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y рублей.

# in_bank = int(input('Введите изначальную сумму вклада: '))
# percentage = int(input('Введите годовой процент: '))
# out_bank = int(input('Введите желаемую сумму в банке: '))
# years = 0
#
# while not (in_bank >= out_bank):
#     in_bank += in_bank * (percentage / 100)
#     years += 1
#
# print(f'Сумма вклада в конце {in_bank:.2f}')
# print(f'количество лет: {int(years)}')

# Вывести n-ный член последовательности Фибоначи.
import sys

sys.set_int_max_str_digits(99999999)

f_1 = 0
f_2 = 1
n = int(input('Введите число n-значения последовательности Фибоначи: '))
if n <= 0:
    print('Введите положительное число!')
elif n == 1:
    print(f_1)
elif n == 2:
    print(f_2)
else:
    c = 0

    while c < n - 1:
        f_3 = f_1 + f_2
        f_1 = f_2
        f_2 = f_3
        c += 1

print(f_2)
print(len(str(f_2)))
