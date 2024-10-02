import arcade

# Константы для игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong"

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 5


class PongGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Начальные позиции
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT // 2
        self.ball_dx = BALL_SPEED
        self.ball_dy = BALL_SPEED

        self.left_paddle_y = SCREEN_HEIGHT // 2
        self.right_paddle_y = SCREEN_HEIGHT // 2

        # Управление
        self.left_paddle_change_y = 0
        self.right_paddle_change_y = 0

    def on_draw(self):
        arcade.start_render()

        # Рисуем мяч
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 10, arcade.color.WHITE)

        # Рисуем ракетки
        arcade.draw_triangle_filled(50, self.left_paddle_y,
                                    70, self.left_paddle_y + 20,
                                    30, self.left_paddle_y - 20,
                                    arcade.color.WHITE)

    def update(self, delta_time):
        # Обновляем позицию мяча
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy

        # Отскок от верхней и нижней границ экрана
        if self.ball_y < 10 or self.ball_y > SCREEN_HEIGHT - 10:
            self.ball_dy *= -1

        # Отскок от ракеток
        if self.ball_x < 60 and abs(self.ball_y - self.left_paddle_y) < PADDLE_HEIGHT // 2:
            self.ball_dx *= -1
        if self.ball_x > SCREEN_WIDTH - 60 and abs(self.ball_y - self.right_paddle_y) < PADDLE_HEIGHT // 2:
            self.ball_dx *= -1

        # Обновляем позицию ракеток
        self.left_paddle_y += self.left_paddle_change_y
        self.right_paddle_y += self.right_paddle_change_y

        # Ограничиваем ракетки внутри экрана
        self.left_paddle_y = max(PADDLE_HEIGHT // 2, min(SCREEN_HEIGHT - PADDLE_HEIGHT // 2, self.left_paddle_y))
        self.right_paddle_y = max(PADDLE_HEIGHT // 2, min(SCREEN_HEIGHT - PADDLE_HEIGHT // 2, self.right_paddle_y))

    def on_key_press(self, key, modifiers):
        # Движение левой ракетки
        if key == arcade.key.W:
            self.left_paddle_change_y = PADDLE_SPEED
        elif key == arcade.key.S:
            self.left_paddle_change_y = -PADDLE_SPEED

        # Движение правой ракетки
        if key == arcade.key.UP:
            self.right_paddle_change_y = PADDLE_SPEED
        elif key == arcade.key.DOWN:
            self.right_paddle_change_y = -PADDLE_SPEED

    def on_key_release(self, key, modifiers):
        # Остановка левой ракетки
        if key == arcade.key.W or key == arcade.key.S:
            self.left_paddle_change_y = 0

        # Остановка правой ракетки
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.right_paddle_change_y = 0


def main():
    PongGame()
    arcade.run()


if __name__ == "__main__":
    main()
