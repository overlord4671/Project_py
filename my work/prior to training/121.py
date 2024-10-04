def main():
    while True:
        # Запрашиваем у пользователя изначальное число
        initial_number = float(input("Введите изначальное число: "))

        # Запрашиваем количество повторений цикла (операций)
        num_operations = int(input("Введите количество повторений цикла: "))

        # Запрашиваем на сколько будет увеличиваться или уменьшаться число в процентах
        percentage_change = float(input("Введите величину изменения в каждом цикле (в процентах): "))

        # Преобразуем проценты в коэффициент
        percentage_change /= 100

        # Создаем пустой список для хранения чисел на каждой итерации
        numbers = []

        # Добавляем изначальное число в список
        numbers.append(initial_number)

        # Переменная для хранения суммы всех итераций
        total_sum = initial_number

        # Выполняем операции указанное количество раз
        for _ in range(num_operations):
            # Получаем последнее число в списке
            last_number = numbers[-1]

            # Вычисляем изменение числа в процентах
            change_amount = last_number * percentage_change

            # Вычисляем новое число
            new_number = round(last_number + change_amount, 3)

            # Добавляем новое число в список
            numbers.append(new_number)

            # Добавляем новое число к сумме всех итераций
            total_sum += new_number

        # Выводим финальное число
        print("Финальное число:", round(numbers[-1], 3))

        # Выводим сумму всех итераций
        print("Сумма всех итераций:", round(total_sum, 3))

        # Выводим первые 5 чисел из массива
        print("Первые значения:")
        for num in numbers[:5]:
            print(round(num, 3), end='\t')

        print("\nПоследние значения:")
        # Выводим последние 5 чисел из массива
        for num in numbers[-5:]:
            print(round(num, 3), end='\t')

        # Проверяем, хочет ли пользователь повторить программу
        repeat = input("\nХотите повторить выполнение программы? (да/нет): ")
        if repeat.lower() != 'да':
            break


if __name__ == "__main__":
    main()
