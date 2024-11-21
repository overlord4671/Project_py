import random

random_dict = {i: random.randint(2, 25) for i in range(10)}

print(random_dict)

# Сортировка по возрастанию
sorted_dict_asc = dict(sorted(random_dict.items(), key=lambda item: item[1]))
print("Сортировка по возрастанию:", sorted_dict_asc)

# Сортировка по убыванию
sorted_dict_desc = dict(sorted(random_dict.items(), key=lambda item: item[1], reverse=True))
print("Сортировка по убыванию:", sorted_dict_desc)
