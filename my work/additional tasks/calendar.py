# Тебе нужно написать преобразовать из чисел в дату: напиши функцию, которая принимает 3 числа, день, месяц, год. Вернуть эта функция должна строку.
# Пример: date_to_str(31, 12, 2000) => 31 December 2000. Сделать защиту от дурака: подумай где и как
# Если защита сработает, то вывести пустую строку.
# Усложнение 1: сделай число месяца словами: Thirty-one.
# Усложнение 2: рассчитать и вывести день недели: Thursday.

def date(day, month, year):
    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
        return ''

    if month == 2:
        if year % 4 == 0:
            if day > 29:
                return ''
        if day > 28:
            return ''

    if month in (4, 6, 9, 11):
        if day > 30:
            return ''

    dict_day = {1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth', 5: 'Fifth', 6: 'Sixth', 7: 'Seventh', 8: 'Eighth',
                9: 'Ninth', 10: 'Tenth', 11: 'Eleventh', 12: 'Twelfth', 13: 'Thirteenth', 14: 'Fourteenth',
                15: 'Fiveteenth', 16: 'Sixteenth', 17: 'Seventeenth', 18: 'Eighteenth', 19: 'Nineteenth',
                20: 'Twentieth', 21: 'Twenty-first', 22: 'Twenty-second', 23: 'Twenty-third', 24: 'Twenty-fourth',
                25: 'Twenty-fifth', 26: 'Twenty-sixth', 27: 'Twenty-seventh', 28: 'Twenty-eighth', 29: 'Twenty-ninth',
                30: 'Thirty', 31: 'Thirty-first'}

    dict_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                  9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    dict_month_code = {1: 1 - (year % 4 == 0), 2: 4 - (year % 4 == 0), 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1,
                       11: 4, 12: 6}
    year_century = year // 100
    code_century = 6 - (year_century % 4) * 2  # 0 -> 6, 1 -> 4, 2 -> 2, 3-> 0
    code_year = (code_century + year % 100 + (year % 100) // 4) % 7
    day_week = (day + dict_month_code[month] + code_year) % 7

    dict_day_name = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    return dict_day[day], dict_month[month], year, dict_day_name[day_week]


print(*date(31, 12, 2000))

print(*date(29, 2, 2000))

print(*date(31, 4, 1900))

print(*date(19, 8, 2024))
