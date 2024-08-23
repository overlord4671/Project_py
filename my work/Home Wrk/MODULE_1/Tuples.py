immutable_var = (1, 'привет', 1.5, True)
print(immutable_var)
# immutable_var[0] = 2  # Нельзя изменять этот тип файлов
print(immutable_var)

mutable_list = ([1, 2, 3], 490, 172.03, 'hello world')
mutable_list[0][2] = 5  # Можно изменять элементы внутри
print(mutable_list)
