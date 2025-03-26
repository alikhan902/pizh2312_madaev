import random
import pygame
from game import GameObject

CELL_SIZE = 20
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Apple(GameObject):
    """
    Класс для представления яблока, его случайной генерации и отображения на экране.
    """

    def __init__(self):
        """
        Инициализирует яблоко, но не вызывает randomize_position, потому что для этого нужен объект змейки.
        """
        self.position = (0, 0)

    def randomize_position(self, snake):
        """
        Генерирует случайную позицию для яблока, проверяя, чтобы оно не попадало на тело змейки.

        Args:
            snake (Snake): Объект змейки для проверки на пересечение с её телом.
        """
        valid_position = False
        while not valid_position:
            x = random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            self.position = (x, y)
            valid_position = True
            # Проверка, не совпадает ли позиция яблока с телом змеи
            for pos in snake.positions:
                if self.position == pos:
                    valid_position = False  # Если яблоко попало на тело змеи, пробуем заново
                    break

    def draw(self, surface):
        """
        Отображает яблоко на экране.

        Args:
            surface (pygame.Surface): Поверхность, на которой рисуется яблоко.
        """
        rect = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (255, 0, 0), rect)
