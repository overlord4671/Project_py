list_2 = ['abcm', 'abcd', '4324', 'gghjm']

list_ = ['Dima', 'Vlad', 'Kirill', 'Max']
zipped = dict(zip(list_, list_2))
print(zipped)

letter = [char for word in zipped.items() for char in word]

for value, key in zipped.items():
    print(f'{list(key)}, {list(value)}')

list_ = [1, 2, 3, 'a', 'b', 'c', True, True, False, 'привет', 'пока']
numb = []
letters = []
bools = []
words = []

for i in list_:
    if isinstance(i, int) and not isinstance(i, bool):
        numb.append(i)
    elif isinstance(i, str):
        if len(i) == 1:
            letters.append(i)
        else:
            words.append(i)
    elif isinstance(i, bool):
        bools.append(i)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def summa_(n):
    if n == 0:
        return 0
    else:
        return n + summa_(n - 1)


def another_sum(n):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += i
    return sum_


def sum_even(n):
    if n <= 1:
        return 0
    elif n % 2 != 0:
        return sum_even(n - 1)
    else:
        return n + sum_even(n - 2)


def sum_even(n):
    if n <= 1:
        return 0
    elif n % 2 != 0:
        return sum_even(n - 1)
    else:
        return n + sum_even(n - 2)


def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


def polindrome(n):
    n = n.replace(' ', '').lower()
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return polindrome(n[1:-1])
    else:
        return False
