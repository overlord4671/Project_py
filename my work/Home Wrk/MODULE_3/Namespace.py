# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

calls = 0


def count_calls():
    global calls
    calls += 1
    print(f'Current calls: {calls}')
    return calls


def string_info(string):
    conclusion = (len(string), string.upper(), string.lower())
    print(f'Length: {conclusion[0]}, Uppercase: {conclusion[1]}, Lowercase: {conclusion[2]}')
    count_calls()
    return calls, conclusion


def is_contains(string, list_to_search):
    print(f'String: {string}, List: {list_to_search}')

    if string.upper() in [item.upper() for item in list_to_search]:
        print(True)
        count_calls()
        return True
    else:
        print(False)
        count_calls()
        return False
    return calls


string_info('Hello')
is_contains('hello', ['Hello', 'WORLD', 'Python'])
string_info('gfbjnuifgbdunkijmfgbnujmi')
is_contains('UrbAN', ['URBAN', 'urban', 'urbAN'])
