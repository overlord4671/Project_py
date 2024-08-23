my_string = input()
length = len(str(my_string))
print('\n' + str(length))
print('в верхнем регистре:',
      my_string.upper())
print('в нижнем регистре:',
      my_string.lower())
print('без пробелов:',
      my_string.replace(' ', ''))
print('1-й элемент:',
      my_string[0])
print('последний элемент:',
      my_string[-1])
