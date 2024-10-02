import sys
from sys import getsizeof

sys.set_int_max_str_digits(999999999)

x = 67 ** 77 ** 3
print(x)

num_digits = len(str(x))

print(f"Количество символов в числе x: {num_digits}")

print(getsizeof(x) / (1024 ** 2))

import cProfile

cProfile.run('print(x)')
