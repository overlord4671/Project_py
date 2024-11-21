first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_res = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_res))
second_res = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_res))
