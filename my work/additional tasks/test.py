def test(n):
    digits = [int(digit) for digit in str(n)]
    return sum(digits)


n = int(input('Введите число: '))
print('Сумма цифр:', test(n))


def test(n):
    if n < 10:
        return n
    else:
        return n % 10 + test(n // 10)


n = int(input('Введите число: '))
print('Сумма цифр:', test(n))
