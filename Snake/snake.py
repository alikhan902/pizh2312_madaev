import random
import pygame
from apple import Apple 
from game import GameObject

# Направления движения змейки
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

CELL_SIZE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
SPEED = 40

class Snake(GameObject):
    """
    Класс для представления змейки, её движения, увеличения длины и подсчёта очков.
    """

    def __init__(self):
        """
        Инициализирует начальное состояние змейки.
        Змейка начинается в центре экрана, имеет длину 1 и счёт 0.
        """
        self.position = (CELL_SIZE * (WINDOW_WIDTH // 2) // CELL_SIZE, CELL_SIZE * (WINDOW_HEIGHT // 2) // CELL_SIZE)
        self.positions = [self.position]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1
        self.score = 0  # Счёт змейки
        self.last_move_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)  # Шрифт для отображения счёта

    def get_head_position(self):
        """
        Возвращает текущую позицию головы змейки.

        Returns:
            tuple: Позиция головы змейки (x, y).
        """
        return self.positions[0]

    def turn(self, direction):
        """
        Меняет направление движения змейки, если оно не противоположное текущему.

        Args:
            direction (tuple): Направление (x, y), в котором должна двигаться змейка.
        """
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def move(self):
        """
        Перемещает змейку в заданном направлении, обновляет её позицию.
        Если змейка сталкивается с собой, вызывает сброс игры.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time >= SPEED:  # Проверка времени
            cur = self.get_head_position()
            x, y = self.direction
            new_pos = ((cur[0] + (x * CELL_SIZE)) % WINDOW_WIDTH, (cur[1] + (y * CELL_SIZE)) % WINDOW_HEIGHT)
            if new_pos in self.positions[2:]:
                self.reset()  # Столкновение с телом змеи — сброс игры
            else:
                self.positions.insert(0, new_pos)
                if len(self.positions) > self.length:
                    self.positions.pop()
            self.last_move_time = current_time

    def reset(self):
        """
        Сбрасывает змейку в начальное состояние: длина 1, позиция в центре экрана, счёт 0.
        """
        self.__init__()  # Сбрасываем змейку и начинаем игру с начальной длиной

    def draw(self, surface):
        """
        Отображает змейку на экране.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется змейка.
        """
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)

    def handle_keys(self):
        """
        Обрабатывает нажатия клавиш для управления змейкой.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_ESCAPE:  # Выход из игры
                    pygame.quit()
                    quit()  # Закрыть игру при нажатии Esc

    def increase_score(self):
        """
        Увеличивает счёт на 10 за каждое съеденное яблоко.
        """
        self.score += 10

    def get_score(self):
        """
        Возвращает текущий счёт змейки.

        Returns:
            int: Текущий счёт.
        """
        return self.score

    def draw_score(self, surface):
        """
        Отображает счёт на экране.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется счёт.
        """
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))  # Отображение счёта в левом верхнем углу