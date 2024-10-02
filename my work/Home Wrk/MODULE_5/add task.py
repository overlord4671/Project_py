import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'пользователь {self.nickname}, возраст {self.age}'

    def check_password(self, password):
        return self.password == hash(password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users=None, videos=None, current_user=None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def add_user(self, user):
        self.users.append(user)

    def add_video(self, video):
        self.videos.append(video)

    def set_current_user(self, user):
        if user in self.users:
            self.current_user = user
        else:
            raise ValueError("Пользователь не зарегистрирован.")

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                print(f'Вы вошли в аккаунт {nickname}!')
                return
        print(f'Неправильные данные входа!')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует!')
                return

        new_user = User(nickname, password, age)
        self.add_user(new_user)

        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print('Вы вышли из аккаунта!')

    def add(self, *args):
        for video in args:
            if isinstance(video, Video):
                video_exists = False
                for v in self.videos:
                    if v.title == video.title:
                        video_exists = True
                        break

                if not video_exists:
                    self.add_video(video)
                else:
                    print(f"Видео с названием '{video.title}' уже существует!")

    def get_videos(self, word):
        res = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                res.append(video.title)

        return res

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу.")
                    return

                video.time_now = 0  # Сброс текущего времени
                print(f'Начинаем просмотр: {video.title}')

                while video.time_now < video.duration:
                    print(f'Смотрим: {video.time_now} секунд')
                    time.sleep(1)
                    video.time_now += 1

                print('Конец видео!')
                return

        print(f'Видео с названием "{title}" не найдено.')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
