import pygame
import math

# Настройки окна и анимации
width, height = 800, 600
distance_from_cam = 200
K1 = 300  # Увеличиваем коэффициент проекции для большего размера куба
increment_speed = 0.6

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating ASCII Cube")
font = pygame.font.SysFont('Courier', 18)  # Используем моноширинный шрифт для символов
clock = pygame.time.Clock()

A = 0
B = 0
C = 0


def calculateX(i, j, k):
    return j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) + \
        j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C)


def calculateY(i, j, k):
    return j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) - \
        j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) - \
        i * math.cos(B) * math.sin(C)


def calculateZ(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)


def project_3d(x, y, z):
    """Проецируем 3D координаты на 2D плоскость."""
    ooz = 1 / (z + distance_from_cam) if z + distance_from_cam != 0 else 0
    xp = int(width / 2 + K1 * ooz * x)
    yp = int(height / 2 + K1 * ooz * y)
    return xp, yp


def draw_edge(start, end, char):
    """Рисуем ребро куба между двумя точками."""
    pygame.draw.line(screen, (255, 255, 255), start, end)


def main():
    global A, B, C
    run = True

    # Вершины куба в исходной позиции, увеличенные в 2 раза
    vertices = [
        (-2, -2, -2),
        (2, -2, -2),
        (2, 2, -2),
        (-2, 2, -2),
        (-2, -2, 2),
        (2, -2, 2),
        (2, 2, 2),
        (-2, 2, 2)
    ]

    # Ребра куба, соединяющие вершины
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Нижняя грань
        (4, 5), (5, 6), (6, 7), (7, 4),  # Верхняя грань
        (0, 4), (1, 5), (2, 6), (3, 7)  # Вертикальные рёбра
    ]

    while run:
        screen.fill((0, 0, 0))  # Очистка экрана

        # Вычисляем новые позиции вершин куба после вращения
        projected_vertices = []
        for vertex in vertices:
            x, y, z = vertex
            x_rotated = calculateX(x, y, z)
            y_rotated = calculateY(x, y, z)
            z_rotated = calculateZ(x, y, z)
            projected_vertices.append(project_3d(x_rotated, y_rotated, z_rotated))

        # Рисуем рёбра куба
        for edge in edges:
            start = projected_vertices[edge[0]]
            end = projected_vertices[edge[1]]
            draw_edge(start, end, '#')

        # Обновляем углы для вращения
        A += 0.05
        B += 0.05
        C += 0.01

        # Обновляем экран
        pygame.display.flip()

        # Ограничиваем FPS до 60
        clock.tick(60)

        # Проверяем события Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
