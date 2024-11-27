import sys
from sys import getsizeof
import time

sys.set_int_max_str_digits(999999999)

time_start = time.time()
x = 2 ** 93999

num_digits = len(str(x))

print(f"Количество символов в числе x: {num_digits}")

print(f"Размер числа x: {getsizeof(x) / (1024 ** 2):.2f} мегабайт")
time_end = time.time()
print(f"Время выполнения программы: {time_end - time_start:.2f} секунд")
