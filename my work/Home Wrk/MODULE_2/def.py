# Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# Создайте пустой список matrix внутри функции get_matrix.
# Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# В первом цикле добавляйте пустой список в список matrix.
# Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# Во втором цикле пополняйте ранее добавленный пустой список значениями value.
# После всех циклов верните значение переменной matrix.
# Выведите на экран(консоль) результат работы функции get_matrix.

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix


print(get_matrix(5, 5, 0))

# Дополнительное задание:
# def create_matrix(n, value):
#     matrix = []
#
#     for i in range(n):
#         row = []
#         for j in range(n):
#             if i == j or i + j == n - 1:
#                 row.append(value)
#             else:
#                 row.append(0)
#         matrix.append(row)
#
#     return matrix
#
#
# matrix = create_matrix(10, '***')
# for row in matrix:
#     print(row)
