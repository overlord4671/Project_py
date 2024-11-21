# -*- coding: windows-1251 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='windows-1251')


def apply_all_func(int_list, *functions):
    if not all(isinstance(i, (int, float)) for i in int_list):
        return f'Неверные вводные данные'
    results = {}
    for func in functions:
        result = func(int_list)
        results[func.__name__] = result
        print(func.__name__, end=' ')
    print()
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([30, 10, 20, 40], sorted, sum))
print(apply_all_func([1, 2, 3, 4, 5], max, min, sum, len))
