# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(2 * 2 + 2)
print(2 * (2 + 2))
print(2 * 2 + 2 == 2 * (2 + 2))

# 4th program
# Преобразуйте строку в дробное число
number = float('123.456')
# Умножьте на 10, чтобы сместить 4 в целую часть
number *= 10
# Используйте команду int() и остаточное деление на 10
first_digit_after_decimal = int(number) % 10
print(first_digit_after_decimal)
