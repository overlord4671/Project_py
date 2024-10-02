class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_conf):
        self.username = username
        self.password = None
        if password == password_conf:
            errors = []

            if len(password) < 8:
                errors.append('Пароль должен содержать 8 символов или больше!')

            upper = any(char.isupper() for char in password)
            if not upper:
                errors.append('Пароль должен содержать хотя бы одну заглавную букву!')

            if errors:
                for message in errors:
                    print(message)

            else:
                self.password = password
                print('Пароль успешно создан!')


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input("Привет! Выбери действие: \n1 - Вход \n2 - Регистрация\n ")

        if choice == '1':
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}!')
                    break
                else:
                    print('Неверный пароль!')
            else:
                print('Пользователь не найден!')

        if choice == '2':
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password_conf := input("Повторите пароль: "))
            if password != password_conf:
                print(f'Пароли не совпадают!')
                continue

            database.add_user(user.username, user.password)
        print(database.data)
