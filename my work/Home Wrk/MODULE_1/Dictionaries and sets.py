my_dict = {'Vadim': 28, 'Alex': 30, 'Ivan': 20}
print(my_dict)
print(my_dict['Vadim'])
print(my_dict.get('Vlad'))
my_dict.update({'Sergey': 25, 'Lisa': 35})
a = my_dict.pop('Alex')
print(a)
print(my_dict)

my_set = {2, 2, 3, 3, 3, 'hello world', False, True, 1.5, 1.5}
print(my_set)
my_set.update({(4, 5, 6), 7})
my_set.discard(1.5)
my_set.remove('hello world')  # добвил для проверки
print(my_set)
