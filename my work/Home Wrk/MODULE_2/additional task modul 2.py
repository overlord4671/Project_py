# К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
#
# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
#
# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)


# import random
#
# first_num = random.randint(3, 20)
# print(f'Число из первой вставки: {first_num}')
# combinations = []
# result = ''
#
# for i in range(3, first_num + 1):
#     if first_num % i == 0:
#         for j in range(1, i + 1):
#             if i % j == 0 and j > 2:
#                 combined_number = ""
#                 pairs = []
#                 for k in range(1, j // 2 + 1):
#                     pair = (k, j - k)
#                     if k != j - k:
#                         pairs.append(f"{pair[0]}{pair[1]}")
#                 pairs.sort()
#                 combined_number = "".join(pairs)
#                 combinations.append(combined_number)
# results = list(set(combinations))
# sorted_results = sorted(results, key=len)
# print(f'Пары чисел: {results}')
# result = ''.join(sorted_results)
# print(f'Нужный пароль: {result}')

# 2-е решение:
import random

first_num = random.randint(3, 20)
print(f'Число из первой вставки: {first_num}')
result = str()

for i in range(1, first_num // 2 + 1):
    for j in range(i, first_num):
        if first_num % (i + j) == 0:
            if i == j:
                continue
            else:
                print(f'{i} и {j}')
                result = result + str(i) + str(j)

print(f'Пароль: {result}')
