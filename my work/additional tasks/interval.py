import random


def interval(left, right, candidates):
    if left > right:
        print('Invalid interval.')
    print(f'{a} {b} {c}')
    if candidates >= left and candidates <= right:
        return print(True)
    else:
        return print(False)


a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
interval(a, b, c)
