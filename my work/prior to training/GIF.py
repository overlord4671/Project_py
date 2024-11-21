import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageFilter
import random


class AnimatedGif:
    def __init__(self, root, width=1000, height=800):
        # Инициализация основных параметров
        self.root = root
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()
        self.bg_color = "black"
        self.square_info = []
        self.square_images = []  # Список для хранения изображений квадратов
        self.animation_running = True  # Переменная для отслеживания состояния анимации
        self.switch_bg()

        # Привязываем обработчики событий для мыши
        self.canvas.bind("<ButtonPress-1>", self.stop_animation)
        self.canvas.bind("<ButtonRelease-1>", self.start_animation)

    def switch_bg(self):
        # Переключение цвета фона между черным и белым
        if self.animation_running:
            self.bg_color = "white" if self.bg_color == "black" else "black"
            self.canvas.configure(bg=self.bg_color)
            self.update_squares()
        self.root.after(110, self.switch_bg)  # Менять цвет каждые 120 миллисекунд

    def update_squares(self):
        # Обновление квадратов на холсте
        self.canvas.delete("square")  # Удаление старых квадратов
        self.square_info = []  # Сброс информации о квадратах
        self.square_images = []  # Сброс списка изображений квадратов
        num_squares = random.randint(5, 9)  # Случайное количество квадратов
        for _ in range(num_squares):  # Рисование квадратов
            size = random.randint(50, 100)  # Случайный размер квадрата от 50 до 100
            x1, y1, x2, y2 = self.get_non_overlapping_position(size)
            color = "white" if self.bg_color == "black" else "black"
            square_image = self.create_blurred_square(size, color)
            self.square_info.append((x1, y1, x2, y2))
            self.square_images.append(square_image)  # Добавление изображения квадрата в список
            self.canvas.create_image(x1, y1, image=square_image, anchor=tk.NW, tags="square")

    def create_blurred_square(self, size, color):
        # Создание квадрата с размытыми краями
        image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, size, size), fill=color)
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))
        return ImageTk.PhotoImage(blurred_image)

    def get_non_overlapping_position(self, size):
        # Генерация неперекрывающегося положения для нового квадрата
        while True:
            x1 = random.randint(0, self.width - size)
            y1 = random.randint(0, self.height - size)
            x2 = x1 + size
            y2 = y1 + size
            if not self.is_overlapping(x1, y1, x2, y2):
                return x1, y1, x2, y2

    def is_overlapping(self, x1, y1, x2, y2):
        # Проверка перекрытия с уже существующими квадратами
        for (sx1, sy1, sx2, sy2) in self.square_info:
            if not (x2 < sx1 or x1 > sx2 or y2 < sy1 or y1 > sy2):
                return True
        return False

    def stop_animation(self, event):
        # Функция остановки анимации при нажатии кнопки мыши
        self.animation_running = False

    def start_animation(self, event):
        # Функция возобновления анимации при отпускании кнопки мыши
        self.animation_running = True


if __name__ == "__main__":
    # Запуск приложения
    root = tk.Tk()
    app = AnimatedGif(root)
    root.mainloop()
