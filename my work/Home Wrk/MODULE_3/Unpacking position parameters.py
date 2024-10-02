def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')


# print_params(2, 'новая_строка', False)
# print_params(b='новая_строка', c=False)
# print_params()
# print_params(b=25)
# print_params(c=[1, 2, 3])

value_list = [5, True, 1.5]
value_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*value_list)
print_params(**value_dict)
value_list_2 = ([5, 10], 'новая_строка')
print_params(*value_list_2, 42)
